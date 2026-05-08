import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import gradio as gr

from src.base.llm_model import get_hf_llm
from src.rag.main import build_rag_chain


llm = get_hf_llm(
    model_name="meta-llama/Llama-3.2-1B-Instruct",
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


demo = gr.Interface(
    fn=ask_question,
    inputs=gr.Textbox(
        label="Question",
        placeholder="Ask something about AI..."
    ),
    outputs=gr.Textbox(label="Answer"),
    title="Generative AI Q&A",
    description="RAG System with LangChain"
)

demo.launch()