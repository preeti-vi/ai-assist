from langchain_core.prompts import ChatPromptTemplate

def get_prompt():
    system_prompt = """
        You are an interviewee. The interviewer asks you a question given in  triple backticks.  
        Answer the question in a precise and professional manner using the following context.  
        
        {context}
        
        
        ~~~
        Query: {query}
        ~~~
        
        Answer as if you are a human and not a chatbot who refers a document or 
        a context to answer the queries.
    """

    prompt = ChatPromptTemplate.from_template(system_prompt)
    return prompt
