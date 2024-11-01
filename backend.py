import os
import bs4
import getpass
from langchain import hub
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

def response(user_query):

    # Load environment and get your openAI api key
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    # Select a webpage to load the context information from
    loader = WebBaseLoader(
        web_paths=("https://www.space.com/large-hadron-collider-particle-accelerator",),
    )
    docs = loader.load()
    # print(type(docs))
    # print(type(docs[0]))
    # print(docs)
    # print(len(docs))

    # Restructure to process the info in chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    # print(text_splitter)
    # print(type(text_splitter))
    
    splits = text_splitter.split_documents(docs)
    # print(type(splits))
    # print(len(splits))
    # print(splits)
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)


    # Retrieve info from chosen source
    retriever = vectorstore.as_retriever(search_type="similarity")
    prompt = hub.pull("rlm/rag-prompt")
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=openai_api_key)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)



    template = """Use the following pieces of context to answer the question at the end.
    Say that you don't know when asked a question you don't know, donot make up an answer. Be precise and concise in your answer.

    {context}

    Question: {question}

    Helpful Answer:"""

    # Add the context to your user query
    custom_rag_prompt = PromptTemplate.from_template(template)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | custom_rag_prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain.invoke(user_query) 