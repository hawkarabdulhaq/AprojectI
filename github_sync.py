import requests
import base64
import streamlit as st
from datetime import datetime

def push_db_to_github(db_file: str):
    repo = st.secrets["general"]["repo"]
    token = st.secrets["general"]["token"]
    branch = "main"  # Adjust if your default branch is different
    file_path = db_file  # Ensure this path matches your repo structure
    api_url = f"https://api.github.com/repos/{repo}/contents/{file_path}"

    try:
        with open(db_file, "rb") as f:
            content = f.read()
        encoded_content = base64.b64encode(content).decode("utf-8")
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

        # Get the current file's SHA (if it exists)
        get_response = requests.get(api_url, headers=headers)
        if get_response.status_code == 200:
            sha = get_response.json().get("sha")
        else:
            sha = None

        commit_message = f"Database update: {datetime.now().isoformat()}"
        data = {
            "message": commit_message,
            "content": encoded_content,
            "branch": branch,
        }
        if sha is not None:
            data["sha"] = sha

        put_response = requests.put(api_url, headers=headers, json=data)
        if put_response.status_code in [200, 201]:
            return {"success": True}
        else:
            return {"success": False, "error": put_response.json()}
    except Exception as e:
        return {"success": False, "error": str(e)}
