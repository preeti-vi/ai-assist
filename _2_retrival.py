from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from chromadb import PersistentClient
from langchain_chroma import Chroma

def get_query_category(user_query: str):
    load_dotenv()

    # Convert the query to a category
    system_prompt = """
        Your are my personal resume assistant. User would ask queries about me, my career, technical skills, experience and you have to map it to one of the resume sections categories.
        So analyze the query in triple backticks. Perform the task in 2 steps and only return the answer without explanation. Do not mention the steps also.: 
        
        Step 1: Analyze If the query is about me and my career, my technical skills, my experience etc. 
        
        Step 2: 
        If yes, then map it to one of the categories mentioned in triple single quotes.
        If no, then return "None"
        
        '''Categories:
            1. Profile
            2. Technical skills
            3. Experience
            4. Projects
            5. Hobbies
    
        If the query does not map to any of the categories above, return "None"
        '''  
    
        Query: {user_query}
    
        
        Example:
        User: Tell me about yourself
        AI: Profile
        
        User: What are your expertise?
        AI: Technical skills
        
        User: What is JQuery
        AI: None 
    """

    prompt = ChatPromptTemplate.from_template(system_prompt)

    llm_gemini = GoogleGenerativeAI(model="gemini-1.5-flash-8b")

    chain = prompt | llm_gemini | StrOutputParser()

    response = chain.invoke({"user_query": user_query})

    # print("\n\nUser query : ", user_query)
    # print(f"Category is : {response}")

    return response


def get_relevant_doc(query_category: str):
    db_client = PersistentClient()
    chroma_db = Chroma(
        client=db_client,
        collection_name="my_resume",
        embedding_function=OpenAIEmbeddings(model="text-embedding-3-small")
    )
    # print(f"Looking for {query_category} in the database")
    search_res = chroma_db.similarity_search(query_category, k=1)
    # print("Result: ",search_res)
    return search_res