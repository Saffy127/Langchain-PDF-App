
Ask Your PDF - Streamlit Application
Welcome to the repository for "Ask Your PDF", a simple and interactive web application that allows users to upload PDFs and ask questions about their contents. The application leverages the power of OpenAI's language model to provide useful responses. This is my first project using Streamlit, an awesome tool that allows you to turn data scripts into shareable web apps in minutes.

Table of Contents
Introduction
Features
Setup and Installation
Usage
Contributing
Introduction
This application uses several technologies:

Streamlit to build the web application
OpenAI for natural language understanding and processing
PDFReader for parsing PDF files
langchain for text splitting, embeddings, vector storage, question answering and callbacks
Features
Upload PDF files and extract text content
Interactively ask questions about the content of the uploaded PDF
Natural language understanding powered by OpenAI's language model
Setup and Installation
This project requires Python 3.6+.

Clone this repository to your local machine.
Install the required packages: pip install -r requirements.txt
Run the application: streamlit run app.py
Note: This project uses OpenAI's API, which requires an API key. Please make sure to have your OpenAI API key set as an environment variable (OPENAI_API_KEY).

Usage
Simply upload a PDF and ask questions about its contents! The application will extract the text from your PDF, and you can interactively ask questions about the content using the OpenAI model.

Contributing
I'm always open to suggestions and improvements! Please feel free to raise issues or pull requests.

