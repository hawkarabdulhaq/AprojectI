from github import Github
import base64
import streamlit as st

def push_db_with_pygithub(db_file: str):
    token = st.secrets["general"]["token"]
    repo_name = st.secrets["general"]["repo"]
    branch = "main"  # or your branch name

    g = Github(token)
    repo = g.get_repo(repo_name)
    
    with open(db_file, "rb") as f:
        content = f.read()
    encoded_content = base64.b64encode(content).decode("utf-8")
    
    try:
        file_content = repo.get_contents(db_file, ref=branch)
        repo.update_file(
            path=db_file,
            message="Update grade in database",
            content=encoded_content,
            sha=file_content.sha,
            branch=branch
        )
    except Exception as e:
        # If file doesn't exist, create it
        repo.create_file(
            path=db_file,
            message="Create database file",
            content=encoded_content,
            branch=branch
        )
    st.success("Database file updated on GitHub using PyGithub!")
