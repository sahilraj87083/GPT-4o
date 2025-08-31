import os
import json

import  streamlit as st
import  openai


from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPEN_API_KEY")
