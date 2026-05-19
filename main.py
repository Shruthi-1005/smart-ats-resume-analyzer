from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel

from app.analyzer import analyze_resume
from app.file_reader import read_resume_file


app = FastAPI(
    title="ResumeFit API",
    description="ATS Resume Analyzer for IBM ASE preparation"
)


class ResumeRequest(BaseModel):
    resume: str
    job_description: str


@app.get("/")
def home():
    return {
        "message": "ResumeFit API is running"
    }


@app.post("/analyze")
def analyze(data: ResumeRequest):

    result = analyze_resume(
        data.resume,
        data.job_description
    )

    return result


@app.post("/upload-resume")
def upload_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    resume_text = read_resume_file(resume)

    if not resume_text:
        return {
            "error": "Only PDF and TXT files are supported"
        }

    result = analyze_resume(
        resume_text,
        job_description
    )

    return result