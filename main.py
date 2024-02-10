import streamlit as st
import ko_encoding_utf8
import streamlit_refer
import gpt_main

from dotenv import load_dotenv


def main():
    load_dotenv()
    
    st.set_page_config(
        page_title="jy_test",
        page_icon=":books:")
    
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["QA chatbot", "Encoding"])

    if selection == "QA chatbot":
        #streamlit_refer.main()
        gpt_main.main()
        

    elif selection == "Encoding":
        ko_encoding_utf8.main()

if __name__ == "__main__":
    main()
    
    
