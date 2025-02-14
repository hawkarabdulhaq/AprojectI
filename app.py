import streamlit as st
from theme import apply_dark_theme
from database import create_tables
from sidebar import show_sidebar
from home import show_home
from style import show_footer  # Import the footer function

def main():
    # Set page config (for Course 1)
    st.set_page_config(page_title="Code for Impact - Course 1", layout="wide")

    apply_dark_theme()
    create_tables()

    # If the user hasn’t yet chosen a course, show the offer page
    if "course" not in st.session_state:
        import offer
        offer.show_offer()
        st.stop()

    # Route based on course selection
    if st.session_state["course"] == "course1":
        if "logged_in" not in st.session_state:
            st.session_state["logged_in"] = False

        if st.session_state["logged_in"]:
            # Show the course 1 pages using your sidebar
            selected = show_sidebar()
            if selected == "logout":
                st.session_state["logged_in"] = False
                st.experimental_rerun()
            elif selected == "home":
                show_home()
            # ─────────────
            # Additional pages for Course 1
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
            # If not logged in, show Course 1 login page
            import login
            login.show_login_create_account()

    elif st.session_state["course"] == "course2":
        # For course 2, we delegate to the Course 2 files.
        if "logged_in" not in st.session_state:
            st.session_state["logged_in"] = False

        if st.session_state["logged_in"]:
            import appx
            appx.main()
        else:
            import loginx
            loginx.show_login_create_account()
    else:
        st.error("Invalid course selection.")

    # Global footer (applies to all pages)
    show_footer()

if __name__ == "__main__":
    main()
