import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def page_eda_body():
    # Load the dataset
    df = pd.read_csv(f"outputs/datasets/cleaned/cleanedDataset.csv")

    # Convert published_timestamp to datetime
    df['published_timestamp'] = pd.to_datetime(df['published_timestamp'])

    st.title("Exploratory Data Analysis (EDA)")

    st.subheader("Dataset Information")

    st.subheader("First 5 Rows of the Dataset")
    st.write(df.head())

    st.subheader("Distribution of Courses by Subject")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='subject', palette='Set2', ax=ax)
    plt.title("Number of Courses by Subject")
    st.pyplot(fig)

    st.subheader("Paid vs. Free Courses")
    fig, ax = plt.subplots()
    df['is_paid'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'orange'],
                                      ax=ax)
    plt.title("Paid vs Free Courses")
    plt.ylabel('')
    st.pyplot(fig)

    st.subheader("Price Distribution of Paid Courses")
    fig, ax = plt.subplots()
    paid_courses = df[df['is_paid'] == 1]
    sns.histplot(paid_courses['price'], bins=30, kde=True, color='blue', ax=ax)
    plt.title("Price Distribution of Paid Courses")
    st.pyplot(fig)

    st.subheader("Top 10 Courses by Subscribers")
    top_courses = df.nlargest(10, 'num_subscribers')[['course_title', 'num_subscribers']]
    st.write(top_courses)
    fig, ax = plt.subplots()
    sns.barplot(data=top_courses, y='course_title', x='num_subscribers', palette='viridis', ax=ax)
    plt.title("Top 10 Courses by Subscribers")
    st.pyplot(fig)

    st.subheader("Reviews vs Subscribers")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='num_reviews', y='num_subscribers', alpha=0.7, ax=ax)
    plt.title("Reviews vs Subscribers")
    st.pyplot(fig)

    st.subheader("Average Content Duration by Level")
    fig, ax = plt.subplots()
    avg_duration = df.groupby('level')['content_duration'].mean().sort_values()
    avg_duration.plot(kind='bar', color='skyblue', ax=ax)
    plt.title("Average Content Duration by Level")
    plt.ylabel("Hours")
    st.pyplot(fig)

    st.subheader("Number of Courses Published Each Month")
    df['month'] = df['published_timestamp'].dt.month
    fig, ax = plt.subplots()
    monthly_courses = df['month'].value_counts().sort_index()
    monthly_courses.plot(kind='bar', color='green', ax=ax)
    plt.title("Number of Courses Published Each Month")
    plt.xlabel("Month")
    plt.ylabel("Number of Courses")
    st.pyplot(fig)

    st.subheader("Total Subscribers by Subject")
    fig, ax = plt.subplots()
    subject_subscribers = df.groupby('subject')['num_subscribers'].sum().sort_values()
    subject_subscribers.plot(kind='barh', color='purple', ax=ax)
    plt.title("Total Subscribers by Subject")
    st.pyplot(fig)

    st.subheader("Lectures vs Duration")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='num_lectures', y='content_duration', hue='level', palette='cool', ax=ax)
    plt.title("Lectures vs Duration")
    st.pyplot(fig)