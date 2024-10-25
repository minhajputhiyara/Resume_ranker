# FastAPI Backend (main.py)
from fastapi import FastAPI, File, UploadFile, Form
from typing import List
from pydantic import BaseModel
import fitz  # PyMuPDF
import chromadb
from fastapi.middleware.cors import CORSMiddleware

# Define request model
class JobDescription(BaseModel):
    description: str

# Initialize FastAPI and ChromaDB
app = FastAPI()
client = chromadb.PersistentClient()
collections = client.get_or_create_collection(name="resume_collections")

def FNdatabase():
    client = chromadb.PersistentClient()
    collections = client.get_or_create_collection(name="resume_collections")
    return collections

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def extract_text_from_pdf(pdf_file: UploadFile):
    try:
        # Read the file content
        content = await pdf_file.read()
        
        # Create PDF document object
        doc = fitz.open(stream=content, filetype="pdf")
        
        # Extract text
        text = ""
        for page in doc:
            text += page.get_text()
        
        # Close the document
        doc.close()
        
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")
        raise

@app.post("/add_resume/")
async def add_resume(candidate_name: str = Form(...), file: UploadFile = File(...)):
    FNdatabase()
    resume_text = await extract_text_from_pdf(file)
    if not isinstance(resume_text, str):
        resume_text = str(resume_text)

    collections.add(
        documents=[resume_text],
        ids=[candidate_name],
        metadatas=[{"name": candidate_name}]
    )
    return {"message": f"Resume for {candidate_name} uploaded and saved!"}

@app.post("/rank_resumes/")
async def rank_resumes(job_desc: JobDescription):
    try:
        # Get the current count of documents in the collection
        current_docs = collections.get()
        if not current_docs["ids"]:
            return {"error": "No resumes found in the database"}
            
        results = collections.query(
            query_texts=[job_desc.description],
            n_results=len(current_docs["ids"])
        )
        
        # Create a list of dictionaries with name and score
        ranked_candidates = [
            {"name": metadata["name"], "score": (1/(1+float(score)))*100}
            for metadata, score in zip(results['metadatas'][0], results['distances'][0])
        ]
        
        # Sort by score (lower distance means better match)
        ranked_candidates.sort(key=lambda x: x["score"],reverse=True)
        
        return {"ranked_candidates": ranked_candidates}
    except Exception as e:
        return {"error": str(e)}

@app.delete("/delete_collection/")
async def delete_collection():
    client.delete_collection(name="resume_collections")
    collections = client.get_or_create_collection(name="resume_collections")
    return {"message": "Your Resume Database is cleared!"}