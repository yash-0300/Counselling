import streamlit as st

# Define questions and their respective choices
questions = [
    {
        #index = 0
        "question": "Hi, How are you feeling?",
        "choices": ["Good", "Somewhat Good", "Not so Good", "feeling low"],
        "next_question": {"Good" : 1, "Somewhat Good": 1, "Not so Good": 2, "feeling low": 2},
        "answer": ""
    },
    {
        #index = 1
        "question": "Sounds great. So is there anything which is bothering you?",
        "choices": ["Friends", "Family", "Financial", "Carrer", "Relationships", "Other"],
        "next_question": {"Friends" : 3, "Family": 3, "Financial": 3, "Carrer": 3, "Relationships": 3, "Other": 3},
        "answer": ""
    },
    {
        #index = 2
        "question": "Its sad to hear about that. What is the reason for that?",
        "choices": ["Friends", "Family", "Financial", "Carrer", "Relationships", "Other"],
        "next_question": {"Friends" : 3, "Family": 3, "Financial": 3, "Carrer": 3, "Relationships": 3, "Other": 3},
        "answer": ""
    },
    {
        #index = 3
        "question": "You can trust me, and discuss your issues feely?",
        "choices": [],
        "next_question": {"temp": 4},
        "answer": ""
    },
    {
        #index = 4
        "question": "Have you experienced this type of feelings before?",
        "choices": ["YES", "NO"],
        "next_question": {"YES": 5, "NO": 6},
        "answer": ""
    },
    {
        #index = 5
        "question": "So, How do you used to handle this at that time?",
        "choices": [],
        "next_question": {"temp": 7},
        "answer": ""
    },
    {
        #index = 6
        "question": ": Oh, its your first time, sorry to hear that. Have you taken any professional help regarding this?",
        "choices": ["YES", "NO"],
        "next_question": {"YES": 11, "NO": 10},
        "answer": ""
    },
    {
        #index = 7
        "question": "So, Can you use the same technique this time?",
        "choices": ["YES", "NO"],
        "next_question": {"YES": 8, "NO": 9},
        "answer": ""
    },
    {
        #index = 8
        "question": "",
        "choices": [],
        "next_question": {"temp": 11},
        "answer": "Oh great!!, So if you feel like you can again take a professional help.."
    },
    {
        #index = 9
        "question": "",
        "choices": [],
        "next_question": {"temp": 11},
        "answer": "Oh I am sorry to hear that, you can consult some other professional if it didn’t work for you in previous expeience..)"
    },
    {
        #index = 10
        "question": "",
        "choices": [],
        "next_question": {"temp": 11},
        "answer": "You can take some Professional help, it would help you for a long run.."
    },
    {
        #index = 11
        "question": "How do you typically manage stress or difficult emotions?",
        "choices": [],
        "next_question": {"temp": 12},
        "answer": "See, you are able to manage your stress and your hard times. That means you are a self dependent person, so don’t feel sad or upset, you can fight back and came out as a fighter."
    },
    {
        #index = 12
        "question": "Who is your support system?",
        "choices": ["Family", "Friends", "Others", "None"],
        "next_question": {"Family": 13, "Friends": 13, "Others": 13, "None": 14},
        "answer": ""
    },
    {
        #index = 13
        "question": "",
        "choices": [],
        "next_question": {"temp": 15},
        "answer": "Its good to know that there are people who are there to help you and support you. So you can feel lucky, as many of them don’t even have that support."
    },
    {
        #index = 14
        "question": "",
        "choices": [],
        "next_question": {"temp": 15},
        "answer": "I am sorry for that, but look on the other side, it means you are self-sufficient and can look after your self. There are so many people who have to be dependent on others."
    },
    {
        #index = 15
        "question": "How do you view yourself and your strengths?",
        "choices": [],
        "next_question": {"temp": 16},
        "answer": "So, use your strength as coping mechanism. You would find a lot of difference after doing that."
    },
    {
        #index = 16
        "question": "Are there any barriers or obstacles you anticipate facing in reaching your goals?",
        "choices": ["YES", "NO"],
        "next_question": {"YES": 17, "NO": 18},
        "answer": ""
    },
    {
        #index = 17
        "question": "What are those barriers?",
        "choices": [],
        "next_question": {"temp": 19},
        "answer": "Its ok to have some barriers, or challenges. Challenges make a man more harder and successful in life."
    },
    {
        #index = 18
        "question": "",
        "choices": [],
        "next_question": {"temp": 19},
        "answer": "Oh that’s great, that means you able to deal with any barriers of your life, and that amazing."
    },
    {
        #index = 19
        "question": "How do you feel about making changes or exploring new ways of thinking or behaving?",
        "choices": [],
        "next_question": {"temp": 20},
        "answer": "Life is unpredictable, and we have to move with the flow. "
    },
    {
        #index = 20
        "question": "Is there anything else you would like to discuss? ",
        "choices": [],
        "next_question": {"temp": 21},
        "answer": "I am glad that you shared your feelings with me. Don’t forget that you are a self suffiecient person and you can come out like a fighter. Identify your inner courage and live a fruitful life. Hope this session was helpful to you."
    },
    {
        #index = 21
        "question": "Please rate our conversation between 1-5 according to your experience.",
        "choices": ["Not Satisfied at all", "Not so Satisfied, could have been better talking to a human counsellor", "somewhat satisfied", "very much satisfied", "Had an excellent session"],
        "next_question": {"temp": 22},
        "answer": ""
    },
]

def app():

    st.title("Welcome to :violet[Counselling Test] 💁")
    current_question = 0
    j = 1
    ques_asked = []
    response = []


    while current_question < len(questions):
        #Display Questions
        ai_ques = questions[current_question]["question"]
        options = questions[current_question]["choices"]
        chat_feedback = questions[current_question]["answer"]

        if ai_ques != "":
            st.info("Question from AI: " + ai_ques)
            ques_asked.append(ai_ques)
        
        if len(options) == 0:
            if ai_ques != "":
                user_input = st.text_input(f"Enter Your Response {j}: ")
                response.append(user_input)
            next_question_index = questions[current_question]["next_question"].get("temp", None)
            # current_question = next_question_index
            j = j + 1

        else:
            
            selected_option = st.selectbox(f"Choose an Option {current_question}", options, index = None, placeholder="Choose an Option...")
            if selected_option != "Other":
                response.append(selected_option)
            if selected_option == "Other":
                user_input = st.text_input(f"Enter Your Response {j}: ")
                response.append(user_input)
                j = j + 1
            next_question_index = questions[current_question]["next_question"].get(selected_option, None)
            
        if chat_feedback != "":
            st.warning(chat_feedback)

        if next_question_index is None:
            break
        else:
            current_question = next_question_index

    submit = st.button('Submit')
    if submit:
        st.info("Thank you for Completing the Questionnaire.")
        st.write("Here are your Responses:")
        with st.container(border = True):
            for i, j in zip(ques_asked, response):
                st.write(f"Question from AI: {i}")
                st.write(f"Response from User: {j}")


