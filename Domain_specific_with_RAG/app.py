import streamlit as st
import os
from dotenv import load_dotenv
from helper import to_create_faiss, get_qa_chain

# Load environment variables
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("gpt_api_key")

# Initialize only once using Streamlit's session state
if 'chain' not in st.session_state:
    # Create the vector retriever and QA chain only once
    vector_retriever = to_create_faiss()
    chain = get_qa_chain(vector_retriever)
    st.session_state.chain = chain  # Store the chain in session state

# Streamlit app configuration and UI
st.set_page_config(page_title="Upflairs ChatBot")
st.header("Upflairs ChatBot 🤖🤖")
question = st.text_input("Ask your question ...", key="question")
submit = st.button("SUBMIT")

if submit:
    # Retrieve the stored chain from session state
    chain = st.session_state.chain
    response = chain(question)
    st.subheader("Your response is:")
    st.write(response['result'])
