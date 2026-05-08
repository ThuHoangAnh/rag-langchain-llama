import re
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


class Str_OutputParser(StrOutputParser):
    def parse(self, text: str) -> str:
        return self.extract_answer(text)

    def extract_answer(
        self,
        text_response: str,
        pattern: str = r"Answer:\s*(.*)"
    ) -> str:
        match = re.search(pattern, text_response, re.DOTALL)

        if match:
            return match.group(1).strip()

        return text_response


class Offline_RAG:
    def __init__(self, llm) -> None:
        self.llm = llm

        self.prompt = ChatPromptTemplate.from_template(
            """You are an assistant for question-answering tasks.
Use the following retrieved context to answer the question.
If you don't know the answer, say that you don't know.

Question: {question}

Context: {context}

Answer:"""
        )

        self.str_parser = Str_OutputParser()

    def get_chain(self, retriever):
        input_data = {
            "context": retriever | self.format_docs,
            "question": RunnablePassthrough()
        }

        rag_chain = (
            input_data
            | self.prompt
            | self.llm
            | self.str_parser
        )

        return rag_chain

    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)