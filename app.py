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
        # Display the sidebar (which updates st.session_state["page"])
        show_sidebar()
        selected = st.session_state.get("page", "home")

        if selected == "logout":
            st.session_state["logged_in"] = False
            st.session_state["page"] = "offer"
            st.experimental_rerun()  # or st.rerun() if your version supports it
        elif selected == "home":
            show_home()
        else:
            # Dynamically import and show the module based on the selected page
            try:
                module = __import__(selected)
                if hasattr(module, "show"):
                    module.show()
                else:
                    st.warning("The selected module does not have a 'show()' function.")
            except ImportError:
                st.warning("Unknown selection.")
    else:
        # Logged out routing remains unchanged
        if st.session_state["page"] == "offer":
            import offer
            offer.show()
        elif st.session_state["page"] == "login":
            import login
            login.show_login_create_account()
        elif st.session_state["page"] == "loginx":
            st.warning("Course 2 Login is not available yet.")
            if st.button("Go Back"):
                st.session_state["page"] = "offer"
                st.experimental_rerun()
        elif st.session_state["page"] == "course2_app":
            from second.appx import appx
            appx.show()
        else:
            import login
            login.show_login_create_account()

    show_footer()

if __name__ == "__main__":
    main()
