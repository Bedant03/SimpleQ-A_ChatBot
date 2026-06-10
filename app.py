import streamlit as st;
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key=os.getenv("groq_api_key")


##Langsmith Tracking"
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot with Groq"

##Prompt TEmplate

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant please response to the user queries"), 
        ("user","question:{question}")
    ]
)

def generate_response(question, api_key, llm_model, temperature, max_tokens):

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name=llm_model,
        temperature=temperature,
        max_tokens=max_tokens
    )

    chain = prompt | llm | StrOutputParser()

    return chain.invoke({"question": question})

#Streamlit App
st.title("Enhanced Q&A Chatbot With Llama")

#Sidebar for settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Groq Api key: ",type="password")

#Drop down to select various Models provided by groq
llm=st.sidebar.selectbox("select a Groq Models",["llama-3.3-70b-versatile","llama-3.1-8b-instant","qwen/qwen3-32b"])

#Adjust Response Parameters
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)

st.write("Go ahead and ask any question")

user_input=st.text_input("You:")

submit=st.button("Generate Response")

if submit:
    if user_input:
        if not api_key:
            st.write("please enter your Groq_api key")
        else:
            response=generate_response(user_input,api_key,llm,temperature,max_tokens)
            st.write(response)
    else:
        st.write("please provide the query")