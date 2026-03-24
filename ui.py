import gradio as gr
import os
import shutil



from src.rag import (
    index_pdf,
    ask_question,
    reset_history,
)



def index_file(file):

    if file is None:
        return "No file selected"

    name = file.name.split("\\")[-1].split("/")[-1]

    save_path = os.path.join("data", "pdfs", name)

    shutil.copy(file.name, save_path)

    index_pdf(name)

    return f"Indexed: {name}"


def ask(q):

    if not q:
        return ""

    return ask_question(q)


def reset():

    return reset_history()


theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="purple",
)


with gr.Blocks(theme=theme) as demo:

    gr.Markdown(
        """
# 📄 PDF RAG AI
### Chat with your PDF using Gemini + LangChain + ChromaDB
"""
    )

    with gr.Row():

        with gr.Column(scale=1):

            gr.Markdown("### 📂 Index PDF")

            file = gr.File(label="Upload PDF")

            btn_index = gr.Button("Index PDF", variant="primary")

            out_index = gr.Textbox(label="Status")

            btn_index.click(
                fn=index_file,
                inputs=file,
                outputs=out_index,
            )

            btn_reset = gr.Button("Reset Chat", variant="secondary")

        with gr.Column(scale=2):

            gr.Markdown("### 💬 Ask Question")

            question = gr.Textbox(
                placeholder="Ask something about PDF...",
                lines=2,
            )

            btn_ask = gr.Button("Ask", variant="primary")

            answer = gr.Textbox(
                label="Answer",
                lines=15,
            )

            btn_ask.click(
                fn=ask,
                inputs=question,
                outputs=answer,
            )

            btn_reset.click(
                fn=reset,
                outputs=answer,
            )


demo.launch()