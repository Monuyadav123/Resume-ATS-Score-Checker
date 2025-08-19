import google.generativeai as genai
import fitz  # PyMuPDF
import gradio as gr

# Configure Gemini API
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-1.5-pro')

# Extract text from PDF
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Get ATS Score
def get_ats_score(resume, job_desc):
    prompt = f"""
    Act like an Applicant Tracking System (ATS).
    Compare the resume and job description below.
    Return a score (0 to 100) based on how well the resume matches the job.
    Also provide 3-5 suggestions to improve the resume for this role.

    Resume:
    {resume}

    Job Description:
    {job_desc}
    """
    response = model.generate_content(prompt)
    return response.text

# Gradio App
with gr.Blocks() as demo:
    gr.Markdown("# Resume ATS Score Checker")
    resume_input = gr.Textbox(lines=10, label="Paste Your Resume")
    jd_input = gr.Textbox(lines=10, label="Paste Job Description")
    output = gr.Textbox(lines=10, label="ATS Score & Feedback")
    run_button = gr.Button("Get ATS Score")
    run_button.click(fn=get_ats_score, inputs=[resume_input, jd_input], outputs=output)

demo.launch()
