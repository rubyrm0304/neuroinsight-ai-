import gradio as gr
from pdf_utils import extract_text_from_pdf
from summarizer import summarize_text

def process_pdf(uploaded_file):
    text = extract_text_from_pdf(uploaded_file.name)
    summary = summarize_text(text)
    return summary

with gr.Blocks() as app:
    gr.Markdown("## 📚 NeuroInsight — PDF & Document Summary AI")
    uploader = gr.File(label="Upload PDF or DOCX")
    output = gr.Textbox(label="Summary", lines=15)
    uploader.upload(process_pdf, uploader, output)

app.launch(share=True)
