import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def load_data():
    """Load the Udemy courses dataset."""
    df = pd.read_csv('outputs/datasets/cleaned/cleanedDataset.csv')
    return df


def plot_content_duration_vs_subscribers(df):
    """Plot the relationship between content duration and number of subscribers."""
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='content_duration', y='num_subscribers', hue='level', palette='cool', ax=ax)
    ax.set_title("Content Duration vs Subscribers")
    st.pyplot(fig)


def plot_num_lectures_vs_content_duration(df):
    """Plot the relationship between number of lectures and content duration."""
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='num_lectures', y='content_duration', alpha=0.6, color='orange', ax=ax)
    ax.set_title("Number of Lectures vs Content Duration")
    st.pyplot(fig)


def plot_average_content_duration_by_level(df):
    """Plot the average content duration by course level."""
    level_duration = df.groupby('level')['content_duration'].mean().sort_values()
    fig, ax = plt.subplots()
    level_duration.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title("Average Content Duration by Level")
    ax.set_ylabel("Hours")
    st.pyplot(fig)


def page_bi_case_study_3():
    """Display the BI case study for optimizing course content for engagement and retention."""
    st.title("BI: Optimizing Course Content for Engagement and Retention")

    df = load_data()

    st.subheader("Content Duration vs Subscribers")
    st.markdown(
        '<div style="background-color: #f0f0f0; padding: 10px;">This scatter plot shows the relationship between the content duration of courses and the number of subscribers. It helps in understanding if longer or shorter courses attract more subscribers.</div>',
        unsafe_allow_html=True)
    if st.checkbox("Show Content Duration vs Subscribers Chart"):
        plot_content_duration_vs_subscribers(df)

    st.subheader("Number of Lectures vs Content Duration")
    st.markdown(
        '<div style="background-color: #f0f0f0; padding: 10px;">This scatter plot illustrates the relationship between the number of lectures and the content duration of courses. It helps in understanding how the number of lectures correlates with the total duration of the course.</div>',
        unsafe_allow_html=True)
    if st.checkbox("Show Number of Lectures vs Content Duration Chart"):
        plot_num_lectures_vs_content_duration(df)

    st.subheader("Average Content Duration by Level")
    st.markdown(
        '<div style="background-color: #f0f0f0; padding: 10px;">This bar chart shows the average content duration of courses grouped by their level (e.g., beginner, intermediate, expert). It helps in understanding the typical course duration for each level.</div>',
        unsafe_allow_html=True)
    if st.checkbox("Show Average Content Duration by Level Chart"):
        plot_average_content_duration_by_level(df)
