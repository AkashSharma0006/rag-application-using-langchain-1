from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st


st.header("Learning langchain genrative AI")


load_dotenv()

llm = ChatGoogleGenerativeAI(model= "gemini-2.0-flash")


promt = PromptTemplate(
    template = "you are an intelligent ai assistant .summarize the following text: {question}"
,input_variables=["question"])


query = st.text_area("Enter your question")

chain = promt|llm

if st.button("Submit"):
    res = chain.invoke(query)
    st.write(res.content)




