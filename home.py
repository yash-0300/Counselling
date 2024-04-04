import streamlit as st

def app():
    st.title("Welcome to :violet[Counselling Hub] :sunglasses:")
    st.info("Welcome to our website! We are delighted that you've chosen to take steps towards improving your mental well-being. Before you proceed with our counseling test, we want to ensure that you understand the purpose of this assessment and provide your consent to participate.")
    st.info("The counseling test is designed to help you gain insights into your emotional state and provide you with valuable information regarding your mental health. It consists of a series of questions aimed at understanding your feelings, thoughts, and behaviors. The results of this test can assist you in identifying areas of concern and guide you towards seeking appropriate support or resources.")
    st.warning("By continuing with the counseling test, you acknowledge that:")

    with st.container(border=True):
        st.write("1. The counseling test is not a diagnostic tool and should not replace professional medical advice or treatment.")
        st.write("2. Your responses will remain confidential and will only be used for the purpose of providing you with personalized feedback.")
        st.write("3. Participation in the counseling test is voluntary, and you may choose to withdraw at any time without consequence.")
        st.write("4. You are aware that the counseling test may elicit emotional responses, and it is recommended to have appropriate support available if needed.")
        st.write("5. You understand that the results of the counseling test are not definitive and may vary based on individual circumstances.")
    