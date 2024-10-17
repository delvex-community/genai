from langchain_openai import OpenAI
from langchain_openai import  OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import  VectorStoreRetriever 
from dotenv import load_dotenv 
from langchain_community.document_loaders.csv_loader import  CSVLoader
import os 
import pandas as pd 
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA 
import numpy as np 
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("gpt_api_key")


def to_create_faiss():
    # File paths for the CSV files
    qa_file_path = r"D:\Achievements\freelancing\GenerativeAI\Domain_specific_with_RAG\Data\questin_answering.csv"
    upflairs_qa_file_path = r"D:\Achievements\freelancing\GenerativeAI\Domain_specific_with_RAG\Data\upflairs_question_answer.csv"

    # Reading the CSV files into DataFrames
    df1 = pd.read_csv(qa_file_path)
    df2 = pd.read_csv(upflairs_qa_file_path)

    combine_dataset = pd.concat([df2,df1])
    print("No of question and answers in the dataset : ",combine_dataset.shape[0])

    final_data_file_path = r"D:\Achievements\freelancing\GenerativeAI\Domain_specific_with_RAG\Data\final_data.csv"
    combine_dataset.to_csv(final_data_file_path,index=False)
    print("successfully save your final dataset at : ",final_data_file_path)

    loader = CSVLoader(file_path=final_data_file_path, source_column="Question")
    data = loader.load()

    vectordb_file_path = "fais_index"
    embeding = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(data,embeding)

    vectordb_retriever = vectordb.as_retriever(score_threshold=0.7)

    return vectordb_retriever


def get_qa_chain(retriever):

    prompt_template = """ 
    You are a coding assistant specializing **only in Python programming**, particularly within the EdTech domain. Your response should cover both theoretical and coding aspects while ensuring examples are simple and beginner-friendly. If the question is unrelated to Python, politely refuse by saying: 
    'I only provide support for Python programming topics. Please ask something related to Python.'

    For each response, follow this structure:

    1. **Theoretical Explanation**: Provide a brief and clear explanation of the concept.
    2. **Code Snippet**: If a code snippet is relevant to the question, provide a small, simple code snippet related to the topic. If not, skip this section.
    3. **Example**: Show a clear and easy-to-understand example that illustrates the concept.

    **Important**: 
    - If no specific programming language is mentioned, assume the question is about Python and proceed accordingly.
    - If a different programming language is explicitly mentioned, politely refuse with the predefined message.
    - If the question is related to Upflairs (its courses, internships, or offerings), provide relevant information about Upflairs as well, alongside the Python programming support.

    **CONTEXT**: {context}
    **My question is**: {question}
    """




    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context","question"]
    )

    chain = RetrievalQA.from_chain_type(llm=OpenAI(),
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain

