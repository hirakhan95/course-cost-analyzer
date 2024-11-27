import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def load_data():
    """Load the Udemy courses dataset."""
    df = pd.read_csv('outputs/datasets/cleaned/cleanedDataset.csv')
    return df[df['is_paid'] == True]


def plot_price_distribution(paid_courses):
    """Plot the price distribution of paid courses."""
    fig, ax = plt.subplots()
    sns.histplot(paid_courses['price'], bins=30, kde=True, color='blue', ax=ax)
    ax.set_title("Price Distribution of Paid Courses")
    st.pyplot(fig)


def plot_subscribers_vs_price(paid_courses):
    """Plot the relationship between subscribers and course price."""
    fig, ax = plt.subplots()
    sns.scatterplot(data=paid_courses, x='price', y='num_subscribers', alpha=0.6, color='orange', ax=ax)
    ax.set_title("Subscribers vs Course Price")
    st.pyplot(fig)


def plot_average_price_by_subject(paid_courses):
    """Plot the average price by subject."""
    subject_price = paid_courses.groupby('subject')['price'].mean().sort_values()
    fig, ax = plt.subplots()
    subject_price.plot(kind='barh', color='skyblue', ax=ax)
    ax.set_title("Average Price by Subject")
    st.pyplot(fig)


def plot_average_price_by_level(paid_courses):
    """Plot the average price by course level."""
    level_price = paid_courses.groupby('level')['price'].mean().sort_values()
    fig, ax = plt.subplots()
    level_price.plot(kind='bar', color='green', ax=ax)
    ax.set_title("Average Price by Level")
    ax.set_ylabel("Price")
    st.pyplot(fig)


def page_bi_case_study_1():
    """Display the BI case study for pricing strategy of paid courses."""
    st.title("BI: Pricing Strategy for Paid Courses")

    paid_courses = load_data()

    st.subheader("Price Distribution")
    st.write(
        "This chart shows the distribution of prices for paid courses. It helps in understanding the common price points and the spread of course prices.")
    if st.checkbox("Show Price Distribution Chart"):
        plot_price_distribution(paid_courses)

    st.subheader("Subscribers vs Course Price")
    st.write(
        "This scatter plot illustrates the relationship between the number of subscribers and the price of the courses. It helps in identifying if higher-priced courses attract more or fewer subscribers.")
    if st.checkbox("Show Subscribers vs Course Price Chart"):
        plot_subscribers_vs_price(paid_courses)

    st.subheader("Average Price by Subject")
    st.write(
        "This bar chart shows the average price of courses grouped by subject. It helps in understanding which subjects have higher or lower average prices.")
    if st.checkbox("Show Average Price by Subject Chart"):
        plot_average_price_by_subject(paid_courses)

    st.subheader("Average Price by Level")
    st.write(
        "This bar chart displays the average price of courses grouped by their level (e.g., beginner, intermediate, expert). It helps in understanding the pricing strategy based on course difficulty.")
    if st.checkbox("Show Average Price by Level Chart"):
        plot_average_price_by_level(paid_courses)
