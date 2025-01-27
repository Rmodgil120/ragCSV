# CSV Miner Using Basic RAG 

This project uses RAG to interact with CSV data. It allows users to ask natural language questions about the contents of a CSV file, 
and the system generates SQL queries to extract the relevant information, with integrated Google Generative AI and combining document loaders, 
embeddings, and vector stores for efficient data retrieval.

![image](https://github.com/user-attachments/assets/ea33beac-db76-4289-acb2-e25d6dbd0b4c)

# Learing from this project:
1.	RAG Workflow:
    Learned to integrate a Retrieval-Augmented Generation pipeline effectively by combining embeddings with LLM reasoning.<br /> 
2.	Embedding Management:
   	Understood the importance of efficient storage and retrieval of embeddings (FAISS).<br />
3.	Query Interpretation:
  	Gained insights into parsing natural language queries and mapping them to structured csv data.<br />
4.	LLM Integration:
  	Realized the potential of LLMs to enhance data retrieval and provide responses.<br />

  	
This assignment provided practical experience in building intelligent systems that combine machine learning and natural language processing for data mining tasks.


# How to make this project run on your machine? 

Step 1: Install Jupyter Notebook <br />
Step 2: Get an API key of Google Gemini from here <br />
Step 3: Install the dataset provided with this project <br />
Step 4: install the libraries listed in the requirements.txt file which is present in the folder<br />
Step 5: Run the ragCSV.ipynb file in Jupyter Notebook<br />
Step 6: Inside the ragCSV file, enter the input in the line:<br />
        answer = rag_chain.invoke({"input": "enter the desired input here"})

 
Disclaimer: To run any separate csv file with this model, one needs to modify the system prompt slightly to match the dataset. 
