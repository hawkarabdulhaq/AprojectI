import streamlit as st
from theme import apply_dark_theme
from database import create_tables
from sidebar import show_sidebar
from home import show_home
from style import show_footer

def main():
    # Must be the FIRST Streamlit command
    st.set_page_config(page_title="Code for Impact", layout="wide")
    apply_dark_theme()
    create_tables()

    # Initialize session state variables if they don't exist.
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "navigate" not in st.session_state:
        st.session_state["navigate"] = "offer"  # Default to offer page

    # If the user is logged in, proceed as before
    if st.session_state["logged_in"]:
        selected = show_sidebar()

        if selected == "logout":
            st.session_state["logged_in"] = False
            st.session_state["navigate"] = "offer"  # Reset to offer on logout
            st.experimental_rerun()

        elif selected == "home":
            show_home()

        # Handle Assignments, Quizzes, etc.
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
        elif selected == "quiz1":
            import quiz1
            quiz1.show()
        elif selected == "quiz2":
            import quiz2
            quiz2.show()
        elif selected == "help":
            import help
            help.show()
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
        # Not logged in: decide what to show based on navigation flag.
        nav = st.session_state["navigate"]
        if nav == "offer":
            import offer
            offer.show_offer()
        elif nav == "login":
            # Show login/create account page from login.py
            from login import show_login_create_account
            show_login_create_account()
        elif nav == "loginx":
            # Load the alternate login page (for Course 2) via appx.py in the second folder.
            from second import appx
            appx.main()
        else:
            st.error("Unknown navigation state.")

    # Global footer
    show_footer()

if __name__ == "__main__":
    main()
