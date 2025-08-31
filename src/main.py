import os
import json

import  streamlit as st
from  openai import OpenAI



from dotenv import load_dotenv
load_dotenv()

token = os.getenv("GIT_HUB_TOKEN")
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)



#  configuring streamlit page setting

st.set_page_config(
    page_title= "GPT-4o",
    page_icon = "֎",
    layout= "centered"
)


# initialize chat session in streamlit if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# streamlit title
st.title("⚛ GPT-4o")

# Display chat history

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


#  input field for user message
user_prompt = st.chat_input("Ask GPT-4o...")


if user_prompt :
    # add user message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # store it in the current session chat history
    st.session_state.chat_history.append({"role" : "user" , "content" : user_prompt})


    # send user's message to GPT-4o and get a response
    response = client.chat.completions.create(
        model= "gpt-4o-mini",
        messages=[
            {"role" : "system" , "content" : "You are a helpful assistant."},
            *st.session_state.chat_history
        ]
    )

    assistant_response = response.choices[0].message.content

    # display gpt-4o's response

    with st.chat_message("assistant"):
        st.markdown(assistant_response)

    # store the response in the current session chat history
    st.session_state.chat_history.append({"role" : "assistant", "content" : assistant_response})



