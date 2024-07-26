import requests
import streamlit as st


def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke", 
                json={'input': {'topic': input_text}})
    
    return response.json()['output']['content']


def get_llama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke", 
                json={'input': {'topic': input_text}})

    return response.json()['output']


st.title('Langchain Demo With LLama2 API')
input_text = st.text_input("Write a poem on")

if(input_text):
    st.write(get_llama_response(input_text))
