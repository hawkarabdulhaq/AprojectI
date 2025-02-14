import streamlit as st
from loginx import show  # Import the loginx module

def main():
    st.set_page_config(page_title="Login - Course 2", layout="wide")
    show()

if __name__ == "__main__":
    main()
