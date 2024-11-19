import streamlit as st


def page_summary_body():
    st.title("Quick Project Summary")

    st.markdown(
        """
        <div style="background-color: #f0f8ff; padding: 10px; border-radius: 5px;">
            <h2 style="color: #00008b;">Project Overview</h2>
            <p>This project analyzes the Udemy courses dataset to understand various trends and insights. The dataset contains information about:</p>
            <ul>
                <li>Course titles</li>
                <li>URLs</li>
                <li>Whether the course is paid or free</li>
                <li>Price</li>
                <li>Number of subscribers</li>
                <li>Reviews</li>
                <li>Lectures</li>
                <li>Level</li>
                <li>Content duration</li>
                <li>Published timestamp</li>
                <li>Subject</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background-color: #e6ffe6; padding: 10px; border-radius: 5px;">
            <h2 style="color: #006400;">Exploratory Data Analysis (EDA)</h2>
            <p>The EDA page provides visual insights into the dataset, including:</p>
            <ul>
                <li>Distribution of courses by subject</li>
                <li>Paid vs. free courses</li>
                <li>Price distribution of paid courses</li>
                <li>Top 10 courses by subscribers</li>
                <li>Reviews vs. subscribers</li>
                <li>Average content duration by level</li>
                <li>Number of courses published each month</li>
                <li>Total subscribers by subject</li>
                <li>Lectures vs. duration</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background-color: #fff0f5; padding: 10px; border-radius: 5px;">
            <h2 style="color: #8b0000;">Model Training and Testing</h2>
            <p>The Model Training and Testing page allows users to:</p>
            <ul>
                <li>Train a model to predict course prices</li>
                <li>View feature importance</li>
                <li>Test the model with sample data</li>
                <li>Get price recommendations based on the model</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )