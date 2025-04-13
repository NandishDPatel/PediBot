**AI-Powered RAG-Based Chatbot for Pediatricians**

<img src="https://github.com/user-attachments/assets/f560103b-9ede-47a9-96d6-6abb34eec391" width="600">

# Please check our app at hugging face HUB- https://huggingface.co/spaces/Satya-bit/MEDICALBOT

# Motivation

_We have made this RAG Chatbot for Satya's sister._

Hi, I’m Satya. I come from a family of doctors, especially pediatricians. This app is a small tribute to all the dedicated pediatricians out there—especially my sister.

My sister is currently pursuing her Master’s in Pediatrics and handles numerous cases every day. Sometimes, for complex or critical cases, she needs to refer to textbooks for accurate and reliable information.

Instead of spending time searching through Google or flipping through heavy books, this app helps her quickly fetch relevant information directly from the textbook. It’s designed to save time and provide accurate references in moments that matter.

# Credits

Nelson is the most famous textbook in Pediatrics. We were not able to upload the textbook on github because it was very large.

Nelson Textbook 8th Edition - https://dl.cafepezeshki.ir/book/Nelson-Essentials-of-Pediatrics-8th-Edition(www.CafePezeshki.IR).pdf

# Overview

This project is an AI-powered Retrieval-Augmented Generation (RAG) chatbot designed to assist pediatricians with instant, context-aware medical insights. By leveraging advanced retrieval and language modeling techniques, the chatbot provides quick and accurate responses, supporting clinical decision-making with an average response time of under 3 seconds.

# Key Features

Instant Medical Insights: Delivers fast and relevant responses to pediatricians' queries.

Context-Aware Retrieval: Uses state-of-the-art embedding and vector search techniques for accurate information retrieval.

Optimized Performance: Achieves response times under 3 seconds, ensuring efficiency in clinical workflows.

User-Friendly Interface: Designed with a simple and intuitive frontend for seamless interaction.

# Tech Stack

Vector Database: Pinecone (for efficient similarity search and retrieval)

<img src="https://github.com/user-attachments/assets/6521bdd8-39d3-4d9d-a16a-ea889bccbea4" width="600">

Embeddings: Hugging Face embeddings (to generate high-quality vector representations)

![image](https://github.com/user-attachments/assets/28945560-fa78-4202-adb9-9cab8ab3dc0f)

LLM: Groq’s Mistral LLM (for generating accurate and context-aware responses)

![image](https://github.com/user-attachments/assets/64786034-bc05-435a-9287-77043235816d)

Deployment: Dockerized and deployed on Hugging Face Spaces

![image](https://github.com/user-attachments/assets/d853509d-b4a4-4625-bc4b-757e12da451b)

CI/CD: Automated deployment using GitHub Actions

![image](https://github.com/user-attachments/assets/ad8416ec-f696-49d4-82c5-8f1a9a21541d)

Frontend: HTML, CSS, and JavaScript (for a smooth user experience)

![image](https://github.com/user-attachments/assets/aba3173a-ec6b-463d-ab03-ea59f982a69c)

APIs- Flask

![image](https://github.com/user-attachments/assets/79ad0dc8-4c37-4249-a6f6-c39e50cca78a)

# Output

In the first image you can see we get the results exactly same that is written in the textbook(highlighted) but in a different language.

![image](https://github.com/user-attachments/assets/0491d097-0bf2-4671-86c9-e948c82d024b)

![image](https://github.com/user-attachments/assets/c8be897d-c7df-453f-a58b-95cbbd0f9b17)

![image](https://github.com/user-attachments/assets/1d7f499c-6977-4b67-827b-7c4e97bb283e)

![image](https://github.com/user-attachments/assets/440329d6-0270-42e8-a9ef-62e8f57df5c1)

# Future Works

We would definitely like to add more textbooks of pediatrics in future and make this app as reliable as possible.

# Limitation

The one and only limitation of this Pedibot is that it will answer questions related to Pediatric field only. Suppose user asks question like "What is the weather today?" or even if asks "How are you?" then the chatbot will respond with "I don't know.". 