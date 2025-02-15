# In github_sync.py
import requests, base64, streamlit as st

def push_db_to_github(db_file: str):
    repo = st.secrets["general"]["repo"]
    token = st.secrets["general"]["token"]
    
    with open(db_file, "rb") as f:
        content = f.read()
    encoded_content = base64.b64encode(content).decode("utf-8")
    
    url = f"https://api.github.com/repos/{repo}/contents/{db_file}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    get_response = requests.get(url, headers=headers)
    sha = None
    if get_response.status_code == 200:
        sha = get_response.json().get("sha")
    
    data = {"message": "Update mydatabase.db", "content": encoded_content}
    if sha:
        data["sha"] = sha
    
    put_response = requests.put(url, json=data, headers=headers)
    if put_response.status_code in [200, 201]:
        return {"success": True}
    else:
        error_info = put_response.json()
        return {"success": False, "error": error_info}
