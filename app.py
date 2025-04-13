# This is app.py
from flask import Flask, render_template, jsonify,request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
###
###

app=Flask(__name__)
load_dotenv()
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

embeddings=download_hugging_face_embeddings()
index_name="medibot"
docsearch=PineconeVectorStore.from_existing_index(index_name=index_name,embedding=embeddings)

retriever=docsearch.as_retriever(search="similarity",serach_kwargs={"k":3})


llm=ChatGroq(
    model="Mistral-Saba-24b",
    temperature=0.4,
    max_tokens=3000
)


prompt=ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),
        ("human","{input}")
    ]
)
question_answer_chain=create_stuff_documents_chain(llm,prompt)# combines the retrieved documents with the input query and uses a language model to generate a concise and relevant answer based on the provided context.
rag_chain=create_retrieval_chain(retriever,question_answer_chain)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get",methods=["GET","POST"])
def chat():
    msg=request.form["msg"]
    input=msg
    print(input)
    response=rag_chain.invoke({"input":msg})
    print("Response:",response["answer"])
    return str(response["answer"])

if __name__=="__main__":
    app.run(host="0.0.0.0",port=7860,debug=True)
