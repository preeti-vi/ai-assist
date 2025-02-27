from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

def generate_response(context, query, prompt):
    load_dotenv()

    # llm = GoogleGenerativeAI(model="gemini-1.5-pro")
    llm = GoogleGenerativeAI(model="gemini-1.5-flash-8b")

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({"context":context,"query":query})

    return response