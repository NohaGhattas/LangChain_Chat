import streamlit as st
from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

def init():
    # Streamlit configuration MUST run before any other Streamlit UI commands
    st.set_page_config(page_title="Welcome To Noha Chat", page_icon="🤖")
    
    load_dotenv()
    if not os.getenv("GOOGLE_API_KEY"):
        st.error("GOOGLE_API_KEY is not set in your .env file")
        st.stop()

def main():
    init()
    
    # Updated to a supported, active model version
    chat = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

    st.header("Welcome To Noha Chat 🤖")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]

    for msg in st.session_state.messages:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)

    if user_input := st.chat_input("Type your message here..."):
        with st.chat_message("user"):
            st.write(user_input)
        
        st.session_state.messages.append(HumanMessage(content=user_input))
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chat.invoke(st.session_state.messages)
                st.write(response.content)
        
        st.session_state.messages.append(AIMessage(content=response.content))
        
        st.rerun()

if __name__ == '__main__':
    main()