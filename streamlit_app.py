#import streamlit as st

#st.title('🎈 Survey chatbot')

#st.write('Hello world!')

#with st.form('my_form'):
  #text = st.text_area('Enter text:', 'How do you feel today? Also, for monitoring purposes, can I ask what is your name, age and sex?')
  #submitted = st.form_submit_button('Submit')
  #if not openai_api_key.startswith('sk-'):
    #st.warning('Please enter your OpenAI API key!', icon='⚠')
  #if submitted and openai_api_key.startswith('sk-'):
    #generate_response(text)
import streamlit as st
from langchain.llms import OpenAI
st.set_page_config(page_title="🦜🔗 Quickstart App")
st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
