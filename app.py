import streamlit as st
import home, bdi, login, counsel

def main():
    # Code for Home Page
    if "page" not in st.session_state:
        st.session_state.page = 0
    
    def nextpage(): st.session_state.page += 1
    def restart(): st.session_state.page = 0
    placeholder = st.empty()

    if st.session_state.page == 0:
        with placeholder.container():
            auth = login.app()
            if auth:
                st.info("Welcome User!! You are Logged in..")
                st.button("Move to Home Page!!",on_click=nextpage,disabled=(st.session_state.page > 3))
                st.button("Logout",on_click=restart)

    elif st.session_state.page == 1:
        with placeholder.container():
           home.app()
           st.warning("Do you want to provide your consent and continue: ")
           st.button("Move to Beck-Depression-Inventory Test!!",on_click=nextpage,disabled=(st.session_state.page > 3))
           st.button("NO, I don't want to Proceed!!",on_click=restart)
           st.button("Logout",on_click=restart)

    elif st.session_state.page == 2:
        with placeholder.container():
            bdi.app()
            st.button("Move to Counselling Section",on_click=nextpage,disabled=(st.session_state.page > 3))
            st.button("Back to Home Page",on_click=restart)
            st.button("Logout",on_click=restart)
    
    elif st.session_state.page == 3:
        with placeholder.container():
            counsel.app()
            st.button("Back to Home Page",on_click=restart)
            st.button("Logout",on_click=restart)

if __name__ == "__main__":
    main()