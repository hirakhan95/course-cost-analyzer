import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def load_data():
    """Load the Udemy courses dataset."""
    df = pd.read_csv('outputs/datasets/cleaned/cleanedDataset.csv')
    return df


def plot_top_courses_by_subscribers(df):
    """Plot the top 10 courses by number of subscribers."""
    top_courses = df.nlargest(10, 'num_subscribers')[['course_title', 'num_subscribers']]
    fig, ax = plt.subplots()
    sns.barplot(data=top_courses, y='course_title', x='num_subscribers', palette='viridis', ax=ax)
    ax.set_title("Top 10 Courses by Subscribers")
    st.pyplot(fig)


def plot_total_subscribers_by_subject(df):
    """Plot the total number of subscribers by subject."""
    subject_performance = df.groupby('subject')['num_subscribers'].sum().sort_values()
    fig, ax = plt.subplots()
    subject_performance.plot(kind='barh', color='purple', ax=ax)
    ax.set_title("Total Subscribers by Subject")
    st.pyplot(fig)


def plot_reviews_vs_subscribers(df):
    """Plot the relationship between reviews and subscribers."""
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='num_reviews', y='num_subscribers', alpha=0.7, color='green', ax=ax)
    ax.set_title("Reviews vs Subscribers")
    st.pyplot(fig)


def display_paid_vs_free_courses_performance(df):
    """Display the performance of paid vs free courses."""
    performance_paid = df[df['is_paid'] == True].nlargest(10, 'num_subscribers')[['course_title', 'num_subscribers']]
    performance_free = df[df['is_paid'] == False].nlargest(10, 'num_subscribers')[['course_title', 'num_subscribers']]
    st.write("Top 10 Paid Courses by Subscribers")
    st.dataframe(performance_paid)
    st.write("Top 10 Free Courses by Subscribers")
    st.dataframe(performance_free)


def page_bi_case_study_2():
    """Display the BI case study for identifying top performing courses for marketing campaigns."""
    st.title("BI: Identifying Top Performing Courses for Marketing Campaigns")

    df = load_data()

    st.subheader("Top 10 Courses by Subscribers")
    st.write(
        "This chart shows the top 10 courses based on the number of subscribers. It helps in identifying the most popular courses.")
    if st.checkbox("Show Top 10 Courses by Subscribers Chart"):
        plot_top_courses_by_subscribers(df)

    st.subheader("Total Subscribers by Subject")
    st.write(
        "This bar chart shows the total number of subscribers for each subject. It helps in understanding which subjects are more popular among students.")
    if st.checkbox("Show Total Subscribers by Subject Chart"):
        plot_total_subscribers_by_subject(df)

    st.subheader("Reviews vs Subscribers")
    st.write(
        "This scatter plot illustrates the relationship between the number of reviews and the number of subscribers. It helps in identifying if courses with more reviews attract more subscribers.")
    if st.checkbox("Show Reviews vs Subscribers Chart"):
        plot_reviews_vs_subscribers(df)

    st.subheader("Paid vs Free Courses Performance")
    st.write(
        "This section displays the performance of paid and free courses by showing the top 10 courses in each category based on the number of subscribers.")
    if st.checkbox("Show Paid vs Free Courses Performance"):
        display_paid_vs_free_courses_performance(df)
