import os
import streamlit as st
import openai
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchahin.callbacks import get_openai_callback

# Main function - you should set the page title before calling any other Streamlit function
def main():
  load_dotenv()

  st.set_page_config(page_title="Ask your PDF")
  st.header("Ask your PDF")

  # Uploading the file
  pdf = st.file_uploader("Upload your PDF", type="pdf")

  # Extract the text 
  if pdf is not None:
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
      text += page.extract_text()

    # split into chunks
    text_splitter = CharacterTextSplitter(
      separator="\n",
      chunk_size=1000,
      chunk_overlap = 200,
      length_function=len
    )
    chunks = text_splitter.split_text(text)

    # create embeddings 
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings) 

    # Show user input
    user_question = st.text_input("Ask a question about your PDF file:")
    if user_question:
      docs = knowledge_base.similarity_search(user_question)

      # Now lets bring in our language model
      llm = OpenAI(model_name="gpt-3.5-turbo")
      chain = load_qa_chain(llm, chain_type="stuff")
      with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=user_question)
        print(cb)

      st.write(response)



if __name__ == '__main__':
  load_dotenv()
  openai.api_key = os.getenv("OPENAI_API_KEY")
  main()
