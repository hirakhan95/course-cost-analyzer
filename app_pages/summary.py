import streamlit as st


def page_summary_body():
    st.write("# Course Cost Analyzer")

    st.write("#### Quick Project Summary")

    st.info(
        f"This project analyzes the Udemy courses dataset from Kaggle to uncover trends and insights into online learning. The dataset provides detailed information about course titles, pricing, subscriber counts, reviews, content duration, levels, and subjects.\n"
        f"The analysis focuses on understanding how key factors like content duration, price, and subject category influence engagement metrics, including the number of subscribers and reviews.\n \n"
        
        
        f"**Project Terms & Jargon**\n"
        f"- **Content Duration (hours)**: Total hours of course material.\n"
        f"- **Number of Subscribers**: Total students enrolled in each course.\n"
        f"- **Number of Reviews**: Feedback count provided by students.\n"
        f"- **Price**: Course cost (if paid).\n"
        f"- **Subject**: The category or topic of the course (e.g., Programming, Business).\n"
        f"- **Level**: Course difficulty (e.g., Beginner, Intermediate, Expert).\n")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/hirakhan95/course-cost-analyzer).")

    st.success(
        f"The project has 3 business requirements:\n"
        f"* 1 - The client is interested in adjusting the pricing of paid courses to maximize revenue while maintaining competitive advantage in the market.\n"
        f"* 2 - The client wants to know the best-performing courses to feature in marketing campaigns to drive more traffic and sales. \n"
        f"* 3 - The client is interested in optimizing the course content (e.g., number of lectures, content duration) to improve engagement and student retention."
    )
