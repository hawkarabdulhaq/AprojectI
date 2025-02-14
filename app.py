import streamlit as st
from theme import apply_dark_theme
from database import create_tables
from sidebar import show_sidebar
from home import show_home
from style import show_footer

def main():
    st.set_page_config(page_title="Code for Impact", layout="wide")

    # Apply dark theme and ensure the required tables exist
    apply_dark_theme()
    create_tables()

    # Initialize navigation page if not already set
    if "page" not in st.session_state:
        st.session_state["page"] = "offer"

    # If the user is logged in, render the sidebar and main content
    if st.session_state.get("logged_in", False):
        selected = show_sidebar()

        if selected == "logout":
            st.session_state["logged_in"] = False
            st.session_state["page"] = "offer"
            st.rerun()
        elif selected == "home":
            show_home()

        # ─────────────────────────────────────────────────────────────────
        # Handle Assignments
        # ─────────────────────────────────────────────────────────────────
        elif selected == "as1":
            import as1
            as1.show()
        elif selected == "as2":
            import as2
            as2.show()
        elif selected == "as3":
            import as3
            as3.show()
        elif selected == "as4":
            import as4
            as4.show()

        # ─────────────────────────────────────────────────────────────────
        # Handle Quizzes
        # ─────────────────────────────────────────────────────────────────
        elif selected == "quiz1":
            import quiz1
            quiz1.show()
        elif selected == "quiz2":
            import quiz2
            quiz2.show()

        # ─────────────────────────────────────────────────────────────────
        # Handle Help (if available)
        # ─────────────────────────────────────────────────────────────────
        elif selected == "help":
            import help
            help.show()

        # ─────────────────────────────────────────────────────────────────
        # Handle Modules
        # ─────────────────────────────────────────────────────────────────
        elif selected == "modules_intro":
            import modules_intro
            modules_intro.show()
        elif selected == "modules_week1":
            import modules_week1
            modules_week1.show()
        elif selected == "modules_week2":
            import modules_week2
            modules_week2.show()
        elif selected == "modules_week3":
            import modules_week3
            modules_week3.show()
        elif selected == "modules_week4":
            import modules_week4
            modules_week4.show()
        elif selected == "modules_week5":
            import modules_week5
            modules_week5.show()
        else:
            st.warning("Unknown selection.")
    else:
        # Navigation for users who are not logged in based on session page value
        if st.session_state["page"] == "offer":
            import offer
            offer.show()
        elif st.session_state["page"] == "login":
            import login
            login.show_login_create_account()
        elif st.session_state["page"] == "loginx":
            # Assuming loginx.py is located in second/appx directory and has a show() function
            from second.appx import loginx
            loginx.show()
        else:
            import login
            login.show_login_create_account()

    show_footer()

if __name__ == "__main__":
    main()
