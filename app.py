import streamlit as st
from theme import apply_dark_theme
from database import create_tables
from login import show_login_create_account
from sidebar import show_sidebar
from home import show_home
from style import show_footer  # Import the footer function

def main():
    # Must be the FIRST Streamlit command
    st.set_page_config(page_title="Code for Impact", layout="wide")
    
    # Apply dark theme and ensure the database/tables exist
    apply_dark_theme()
    create_tables()

    # Initialize session state variables if not already set
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # If the user is logged in, show the main app (via the sidebar)
    if st.session_state["logged_in"]:
        selected = show_sidebar()

        if selected == "logout":
            st.session_state["logged_in"] = False
            st.experimental_rerun()

        elif selected == "home":
            show_home()

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

        # Handle Quizzes
        elif selected == "quiz1":
            import quiz1
            quiz1.show()
        elif selected == "quiz2":
            import quiz2
            quiz2.show()

        # Handle Help
        elif selected == "help":
            import help
            help.show()

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
        # For non-logged-in users, first show the Offer page
        if "selected_offer" not in st.session_state:
            import offer
            offer.show_offer()
        else:
            # Based on the chosen course, navigate to the appropriate login page
            if st.session_state["selected_offer"] == "course1":
                show_login_create_account()
            elif st.session_state["selected_offer"] == "course2":
                # Import loginx from the subfolder (ensure your PYTHONPATH is set appropriately)
                import second.appx.loginx as loginx
                loginx.show_login_create_account()
            else:
                st.error("Unknown offer selection.")

    # Global footer for all pages
    show_footer()

if __name__ == "__main__":
    main()
