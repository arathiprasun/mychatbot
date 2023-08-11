import streamlit as st

st.title('🎈 Survey chatbot')

st.write('Hello world!')

with st.form('my_form'):
  text = st.text_area('Enter text:', 'How do you feel today? Also, for monitoring purposes, can I ask what's your name, age and sex?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
