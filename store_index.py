#Step-1
from src.helper import load_pdf_file,text_splitter,download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


extracted_data=load_pdf_file(data='Data/') #Extracting data
text_chunks=text_splitter(extracted_data)#Splitting data
embeddings=download_hugging_face_embeddings()#Initializing embeddings

#Creating index at Pinecone

pc=Pinecone(api_key=PINECONE_API_KEY)

index_name="medibot"

if not pc.has_index(index_name):

    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

#Creating embeddings and storing in Pinecone
docsearch=PineconeVectorStore.from_documents(documents=text_chunks, embedding=embeddings, index_name=index_name)