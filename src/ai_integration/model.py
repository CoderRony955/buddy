from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from .providers import (
    OPENAI_MODEL,
    OPENAI_API_KEY,
    GOOGLE_GEN_AI_API_KEY,
    GOOGLE_MODEL,
    ANTHROPIC_API_KEY,
    ANTHROPIC_MODEL,
    OLLAMA_CLOUD_MODEL
)

# for ollama
import ollama


class Chat:
    def __init__(self):
        self.system_prompt = "You are a helpful Gaming Expert AI assistant that provides very concise answers."
        self.template = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", "{question}")
        ])

    def with_google_genai_model(self, query: str):
        try:
            llm = ChatGoogleGenerativeAI(
                model=GOOGLE_MODEL,
                temperature=0.7,
                google_api_key=GOOGLE_GEN_AI_API_KEY
            )

            chain = self.template | llm

            response = chain.invoke({
                "question": query
            })

            return response.content[0]['text']

        except Exception as e:
            return (False, str(e))

    def with_openai_model(self, query: str):
        try:
            llm = ChatOpenAI(
                model=OPENAI_MODEL,
                temperature=0.7,
                openai_api_key=OPENAI_API_KEY
            )

            chain = self.template | llm

            response = chain.invoke({
                "question": query
            })

            return response.content[0]['text']

        except Exception as e:
            return (False, str(e))

    def with_anthropic_model(self, query: str):
        try:
            llm = ChatAnthropic(
                model=ANTHROPIC_MODEL,
                temperature=0.7,
                anthropic_api_key=ANTHROPIC_API_KEY
            )

            chain = self.template | llm

            response = chain.invoke({
                "question": query
            })

            return response.content[0]['text']

        except Exception as e:
            return (False, str(e))

    def with_ollama_cloud_model(self, query: str):
        try:
            messages = [
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": query
                }
            ]
            response = ollama.chat(
                model=OLLAMA_CLOUD_MODEL,
                messages=messages
            )
            return response['message']['content']

        except Exception as e:
            return (False, str(e))
