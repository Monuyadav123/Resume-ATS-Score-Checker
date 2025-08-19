# Resume ATS Score Checker

This project evaluates how well a resume matches a job description using Google Gemini AI.  
It provides:
- An ATS score (0–100)
- Suggestions to improve the resume
- A simple Gradio interface

## Features
- Paste resume text or extract text from a PDF
- Paste a job description
- Get instant feedback on resume-job match

## Installation
Clone this repository and install dependencies:

```bash
git clone https://github.com/your-username/resume-ats-checker.git
cd resume-ats-checker
pip install -r requirements.txt
```

## Usage
Run the application locally:

```bash
python app.py
```

This will launch a Gradio interface in your browser.

## Example
**Input:**
- Resume: Data Scientist with experience in Python, SQL, Machine Learning, LLMs...
- Job Description: Looking for Data Scientist with skills in NLP, Transformers, and Generative AI.

**Output:**
```
ATS Score: 75
Suggestions:
1. Add NLP project experience
2. Mention Hugging Face or Transformer models
3. Highlight cloud deployment experience
```

## Tech Stack
- Python
- Gradio
- Google Generative AI
- PyMuPDF

## License
MIT License
