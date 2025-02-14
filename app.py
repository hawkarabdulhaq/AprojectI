import streamlit as st
from theme import apply_dark_theme
from database import create_tables
from sidebar import show_sidebar
from home import show_home
from style import show_footer

def main():
    st.set_page_config(page_title="Code for Impact", layout="wide")
    apply_dark_theme()
    create_tables()

    if "page" not in st.session_state:
        st.session_state["page"] = "offer"

    if st.session_state.get("logged_in", False):
        selected = show_sidebar()
        if selected == "logout":
            st.session_state["logged_in"] = False
            st.session_state["page"] = "offer"
            st.rerun()
        elif selected == "home":
            show_home()
        # Add other navigation sections here...
        else:
            st.warning("Unknown selection.")
    else:
        if st.session_state["page"] == "offer":
            import offer
            offer.show()
        elif st.session_state["page"] == "login":
            import login
            login.show_login_create_account()
        elif st.session_state["page"] == "loginx":
            from second.appx import loginx
            loginx.show()
        elif st.session_state["page"] == "course2_app":
            from second.appx import appx
            appx.show()
        else:
            import login
            login.show_login_create_account()

    show_footer()

if __name__ == "__main__":
    main()
