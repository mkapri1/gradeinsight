import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def display_navbar():
    st.sidebar.title("Assignments")
    assignment_selected = st.sidebar.selectbox("Select Assignment", ("Assignment 1", "Assignment 2", "Assignment 3"))
    return assignment_selected

def display_chatbox():
    st.title("AI Assistant - Professor")
    user_input = st.text_input("Ask a question")

    if st.button("Send"):
        # Logic for handling user input and generating bot response
        bot_response = "This is a bot response."
        st.text_area("Bot", value=bot_response, height=100, disabled=True)

def page_contact():
    col1, col2, col3 = st.columns([1, 3, 2])

    with col1:
        display_navbar()

    with col2:
        display_chatbox()

def main():
    st.sidebar.title("Navigation")
    page_options = ["Home", "About", "Contact"]
    selected_page = st.sidebar.selectbox("Go to", page_options)

    if selected_page == "Home":
        # Home page content
        st.title("Grade Insight")
        st.write("Course Feedback at Scale: This app provides insights into course grading and feedback.")
        st.markdown("[Try Now](#)")  # Placeholder for Try Now button
        st.image("https://example.com/grading_scale_image.jpg", width=300)  # Replace with actual image URL

    elif selected_page == "About":
        # About page content
        st.title("About Page")
        st.write("This is the About Page.")

    elif selected_page == "Contact":
        # Contact page content
        page_contact()

if __name__ == "__main__":
    main()
