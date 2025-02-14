import streamlit as st
from theme import apply_dark_theme
from database import create_tables
from style import show_footer

# Import Course 2–specific sidebar and home page modules.
from sidebar_x import show_sidebar_x
from home_x import show_home_x

def main():
    st.set_page_config(page_title="Code for Impact - Course 2", layout="wide")

    apply_dark_theme()
    create_tables()

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.session_state["logged_in"]:
        selected = show_sidebar_x()
        if selected == "logout":
            st.session_state["logged_in"] = False
            st.experimental_rerun()
        elif selected == "home":
            show_home_x()
        else:
            st.warning("Unknown selection.")
    else:
        # If not logged in, show the Course 2 login page.
        import loginx
        loginx.show_login_create_account()

    show_footer()

if __name__ == "__main__":
    main()
