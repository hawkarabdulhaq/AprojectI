import requests
import base64
import streamlit as st

def push_db_to_github(db_file: str):
    repo = st.secrets["general"]["repo"]
    token = st.secrets["general"]["token"]
    branch = "main"  # Adjust if your default branch is different
    file_path = db_file  # Ensure this path matches your repo structure
    api_url = f"https://api.github.com/repos/{repo}/contents/{file_path}"

    with open(db_file, "rb") as f:
        content = f.read()
    encoded_content = base64.b64encode(content).decode("utf-8")

    # Get the current file's SHA (if it exists)
    headers = {"Authorization": f"token {token}"}
    get_response = requests.get(api_url, headers=headers)
    if get_response.status_code == 200:
        sha = get_response.json().get("sha")
    else:
        sha = None

    commit_message = "Update grade in database"
    data = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch,
    }
    if sha:
        data["sha"] = sha

    put_response = requests.put(api_url, headers=headers, json=data)
    if put_response.status_code in [200, 201]:
        st.success("Database successfully updated on GitHub!")
        return {"success": True}
    else:
        error_info = put_response.json()
        st.error(f"Error updating database on GitHub: {error_info}")
        return {"success": False, "error": error_info}
