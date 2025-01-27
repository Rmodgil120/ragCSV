from langchain_community.document_loaders.csv_loader import CSVLoader
from pathlib import Path
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
import getpass
import os
import pandas as pd

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass('enter google api key here')

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
file_path = ('enter file locaiton here')
data = pd.read_csv(file_path, encoding='unicode_escape')

loader = CSVLoader(file_path=file_path)
docs = loader.load_and_split()

import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS


embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
index = faiss.IndexFlatL2(len(GoogleGenerativeAIEmbeddings().embed_query(" ")))


vector_store = FAISS(
    embedding_functions=GoogleGenerativeAIEmbeddings(),
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={}
)

vector_store.add_documents(documents=docs)

from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

retriever = vector_store.as_retriever()

system_prompt = (
    """
    You are an expert in converting English questions to SQL query!
    The CSV file has the name sales_data_sample and has the following columns: 
    ORDERNUMBER, QUANTITYORDERED, ORDERLINENUMBER, QTR_ID, MONTH_ID, YEAR_ID, PRICEEACH, SALES, STATUS, CONTACTFIRSTNAME, 
    COUNTRY, DEALSIZE, PRODUCTLINE. 

    For example:
    Example 1 - How many orders have been placed?, 
    the SQL command will be something like this: SELECT COUNT(*) FROM sales_data_sample;
    Example 2 - Show all orders from customers in the USA, 
    the SQL command will be something like this: SELECT * FROM sales_data_sample WHERE COUNTRY = "USA";
    Example 3 - What is the total sales amount?, 
    the SQL command will be something like this: SELECT SUM(SALES) FROM sales_data_sample;

    The SQL code should not include ``` at the beginning or end, and the output should not contain the word "sql".
    """
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

answer = rag_chain.invoke({"input": "What is the average sales?"})
print(answer)




