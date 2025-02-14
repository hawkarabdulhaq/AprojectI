import streamlit as st
from theme import apply_dark_theme
from database import create_tables
import offer  # New import for the offer page
from login import show_login_create_account
from sidebar import show_sidebar
from home import show_home
from style import show_footer  # Import the footer function

def main():
    # Must be the FIRST Streamlit command
    st.set_page_config(page_title="Code for Impact", layout="wide")

    # Apply dark theme and ensure tables exist
    apply_dark_theme()
    create_tables()

    # Check for a query parameter; default to "offer"
    query_params = st.experimental_get_query_params()
    page = query_params.get("page", ["offer"])[0]

    # If the user is already logged in, show the main sidebar & pages.
    if st.session_state.get("logged_in", False):
        selected = show_sidebar()

        if selected == "logout":
            st.session_state["logged_in"] = False
            st.experimental_rerun()

        elif selected == "home":
            show_home()

        # ─────────────────────────────────────────────────────────────
        # Handle Assignments
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

        # ─────────────────────────────────────────────────────────────
        # Handle Quizzes
        elif selected == "quiz1":
            import quiz1
            quiz1.show()

        elif selected == "quiz2":
            import quiz2
            quiz2.show()

        # ─────────────────────────────────────────────────────────────
        # Handle Help
        elif selected == "help":
            import help
            help.show()

        # ─────────────────────────────────────────────────────────────
        # Handle Modules
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
        # If not logged in, display pages based on the query parameter.
        if page == "offer":
            offer.show()
        elif page == "login":
            show_login_create_account()
        elif page == "loginx":
            import loginx
            loginx.show()
        else:
            # Fallback to the offer page if the query parameter is unrecognized.
            offer.show()

    # Add the global footer (this will appear on all pages)
    show_footer()

if __name__ == "__main__":
    main()
