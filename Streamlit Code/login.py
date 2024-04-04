import streamlit as st

def creds_entered():
    if st.session_state["user"].strip() == "admin" and st.session_state["passwd"].strip() == "admin":
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state["passwd"]:
            st.warning("Please enter Password..")
        elif not st.session_state["user"]:
            st.warning("Please enter username..")
        else:
            st.error("Invalid Username/Password: face_with_raised_eyebrow:")

def app():
    st.title("Welcome to :violet[Login Page] 💁")

    if "authenticated" not in st.session_state:
        st.text_input(label="Username: ", value="", key="user", on_change=creds_entered)
        st.text_input(label="Password: ", value="", key="passwd", type= "password", on_change=creds_entered)
        return False
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input(label="Username: ", value="", key="user", on_change=creds_entered)
            st.text_input(label="Password: ", value="", key="passwd", type= "password", on_change=creds_entered)
            return False
