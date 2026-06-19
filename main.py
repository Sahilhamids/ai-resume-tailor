from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os

# Importing the functions you already built!
from extractor import extract_text_from_pdf
from ai_agent import generate_tailored_resume

app = FastAPI(title="AI Resume Tailor API")

@app.post("/tailor-resume")
async def tailor_resume(
    job_description: str = Form(...), 
    resume_file: UploadFile = File(...)
):
    # 1. Save the uploaded resume temporarily so our extractor can read it
    temp_file_path = f"temp_{resume_file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(resume_file.file, buffer)
    
    try:
        # 2. Extract the text using your existing function
        resume_text = extract_text_from_pdf(temp_file_path)
        
        # 3. Send to Gemini AI using your existing function
        ai_response = generate_tailored_resume(resume_text, job_description)
        
        # 4. Return the AI's analysis
        return {
            "status": "success",
            "filename": resume_file.filename,
            "ai_analysis": ai_response
        }
        
    finally:
        # 5. Clean up by deleting the temporary file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)