import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import gradio as gr

from src.base.llm_model import get_hf_llm
from src.rag.main import build_rag_chain


llm = get_hf_llm(
    model_name="meta-llama/Llama-3.2-3B-Instruct",
    temperature=0.7
)

genai_chain = build_rag_chain(
    llm,
    data_dir="./data_source/generative_ai",
    data_type="pdf"
)


def ask_question(question):
    if not question.strip():
        return "Please enter a question."

    answer = genai_chain.invoke(question)
    return answer


examples = [
    "What is the main idea of the Attention Is All You Need paper?",
    "Explain the difference between BERT and GPT.",
    "What are the key innovations introduced in DeepSeek-V3?",
]


css = """
.gradio-container {
    max-width: 1100px !important;
    margin: auto !important;
}

#title {
    text-align: center;
    margin-bottom: 8px;
}

#subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 30px;
}

.card {
    border-radius: 18px;
    padding: 24px;
    background: #1f2937;
    box-shadow: 0 8px 30px rgba(0,0,0,0.25);
}

button {
    border-radius: 12px !important;
}
"""


with gr.Blocks(css=css, theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🤖 Generative AI Q&A
        """,
        elem_id="title"
    )

    gr.Markdown(
        """
        Ask questions about your Generative AI papers using a LangChain RAG system.
        """,
        elem_id="subtitle"
    )

    with gr.Row():
        with gr.Column(scale=1):
            question = gr.Textbox(
                label="Your Question",
                placeholder="Ask something about Attention, BERT, DeepSeek...",
                lines=5
            )

            submit_btn = gr.Button("🚀 Ask Question", variant="primary")
            clear_btn = gr.Button("🧹 Clear")

            gr.Examples(
                examples=examples,
                inputs=question
            )

        with gr.Column(scale=1):
            answer = gr.Textbox(
                label="Answer",
                lines=12,
                show_copy_button=True
            )

    submit_btn.click(
        fn=ask_question,
        inputs=question,
        outputs=answer
    )

    clear_btn.click(
        fn=lambda: ("", ""),
        inputs=None,
        outputs=[question, answer]
    )


demo.launch()