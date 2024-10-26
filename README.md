
# Resume Ranking System

This project is a Resume Ranking System built with FastAPI (backend) and React (frontend). The system enables users to upload resumes, extracts text, stores them in ChromaDB with metadata, and ranks resumes based on similarity to a job description.

## Features

- **Resume Upload**: Allows uploading of resumes in PDF format.
- **Text Extraction**: Extracts text from uploaded PDFs for further processing.
- **ChromaDB Integration**: Stores resumes in ChromaDB with metadata for similarity search.
- **Job Description Matching**: Accepts a job description as input and ranks resumes based on relevance.
- **SQLite Database**: Stores candidate metadata for persistence.

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI
- **Database**: SQLite (for metadata), ChromaDB (for similarity ranking)
- **PDF Processing**: PyMuPDF
- **Server**: Uvicorn

## Installation

### Prerequisites

- Python 3.8+
- Node.js and npm

### Clone the repository

```bash
git clone <repository-url>
cd resume-ranking-system
```

### Backend Setup

1. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install backend dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install frontend dependencies:

   ```bash
   npm install
   ```

3. Run the React development server:

   ```bash
   npm start
   ```

### Project Structure

```
resume-ranking-system/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── chromadb_client.py    # ChromaDB client setup
│   ├── pdf_extractor.py      # PDF text extraction functions
│   ├── database.py           # SQLite database setup
│   └── requirements.txt      # Backend dependencies
└── frontend/
    ├── public/
    ├── src/
    │   ├── App.js            # Main React component
    │   ├── components/       # Reusable UI components
    │   ├── services/         # API calls to FastAPI backend
    └── package.json          # Frontend dependencies
```

### Usage

1. Open the React application in the browser at [http://localhost:3000](http://localhost:3000).
2. Upload a PDF resume and enter the candidate's name.
3. Submit a job description to rank resumes based on relevance.

### API Endpoints

- `POST /upload_resume`: Uploads a PDF and stores its text and metadata in ChromaDB.
- `POST /rank_resumes`: Accepts a job description and returns a list of ranked resumes.

### Requirements

See [requirements.txt](./backend/requirements.txt) for backend dependencies.

## Contributing

Feel free to submit issues and pull requests. Make sure to follow coding standards.
