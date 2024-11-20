import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.stats import f_oneway
import numpy as np


def load_data():
    """Load the Udemy courses dataset."""
    df = pd.read_csv('outputs/datasets/cleaned/cleanedDataset.csv')
    return df


def preprocess_data(df):
    """Converts columns to appropriate datatypes and handles missing values if any."""
    df['published_timestamp'] = pd.to_datetime(df['published_timestamp'])
    df['year_published'] = df['published_timestamp'].dt.year
    return df


def explore_data(df):
    """Provides summary statistics and visualizations."""
    st.write("Summary Statistics:")
    st.write(df.describe())
    st.write("Missing Values:")
    st.write(df.isnull().sum())

    st.subheader("Distribution of Content Duration")
    fig, ax = plt.subplots()
    sns.histplot(df['content_duration'], kde=True, bins=20, color='skyblue', ax=ax)
    ax.set_title("Distribution of Content Duration")
    ax.set_xlabel("Duration (hours)")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    st.subheader("Distribution of Number of Subscribers")
    fig, ax = plt.subplots()
    sns.histplot(df['num_subscribers'], kde=True, bins=20, color='green', ax=ax)
    ax.set_title("Distribution of Number of Subscribers")
    ax.set_xlabel("Subscribers")
    ax.set_ylabel("Frequency")
    ax.set_xscale('log')
    st.pyplot(fig)

    st.subheader("Content Duration by Subject")
    fig, ax = plt.subplots()
    sns.boxplot(x='subject', y='content_duration', data=df, palette='Set2', ax=ax)
    ax.set_title("Content Duration by Subject")
    ax.set_xlabel("Subject")
    ax.set_ylabel("Duration (hours)")
    plt.xticks(rotation=45)
    st.pyplot(fig)


def cluster_courses_by_duration(df):
    """Clusters courses into short, medium, and long categories."""
    scores = []
    for k in range(2, 6):
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(df[['content_duration']])
        score = silhouette_score(df[['content_duration']], labels)
        scores.append(score)
    optimal_k = np.argmax(scores) + 2

    kmeans = KMeans(n_clusters=optimal_k, random_state=42)
    df['duration_cluster'] = kmeans.fit_predict(df[['content_duration']])

    cluster_mapping = {i: f"Cluster {i + 1}" for i in range(optimal_k)}
    df['duration_category'] = df['duration_cluster'].map(cluster_mapping)

    # Ensure each cluster has a minimum number of data points
    min_cluster_size = 10
    for cluster in cluster_mapping.values():
        if df[df['duration_category'] == cluster].shape[0] < min_cluster_size:
            st.write(f"Cluster {cluster} has less than {min_cluster_size} data points. Adjusting clusters.")
            return None

    st.subheader("Content Duration Clusters")
    fig, ax = plt.subplots()
    sns.boxplot(x='duration_category', y='content_duration', data=df, palette='Set3', ax=ax)
    ax.set_title("Content Duration Clusters")
    ax.set_xlabel("Duration Category")
    ax.set_ylabel("Content Duration (hours)")
    st.pyplot(fig)
    st.write(f"Optimal Number of Clusters: {optimal_k}")
    return df


def analyze_performance_metrics(df):
    """Analyzes ratings, reviews, and subscribers across duration categories."""
    summary = df.groupby('duration_category')[['num_subscribers', 'num_reviews', 'price']].mean().round(2)
    st.write("Performance Metrics by Duration Category:")
    st.write(summary)

    metrics = ['num_subscribers', 'num_reviews', 'price']
    for metric in metrics:
        st.subheader(f"Average {metric} by Duration Category")
        fig, ax = plt.subplots()
        sns.barplot(x='duration_category', y=metric, data=df, palette='coolwarm', ax=ax)
        ax.set_title(f"Average {metric} by Duration Category")
        ax.set_xlabel("Duration Category")
        ax.set_ylabel(f"Average {metric}")
        st.pyplot(fig)
    return summary


def analyze_yearly_trends(df):
    """Examines trends in course metrics over years."""
    yearly_trends = df.groupby('year_published')[['num_subscribers', 'num_reviews', 'content_duration']].mean().round(2)
    st.write("Yearly Trends in Metrics:")
    st.write(yearly_trends)

    st.subheader("Yearly Trends in Course Metrics")
    fig, ax = plt.subplots()
    yearly_trends.plot(kind='line', figsize=(10, 6), marker='o', ax=ax)
    ax.set_title("Yearly Trends in Course Metrics")
    ax.set_xlabel("Year Published")
    ax.set_ylabel("Average Metrics")
    ax.legend(loc='upper left')
    ax.grid(True)
    st.pyplot(fig)
    return yearly_trends


def hypothesis_test(df):
    """Conducts ANOVA to determine if there's a significant difference in metrics across clusters."""
    short = df[df['duration_category'] == 'Cluster 1']['num_subscribers']
    medium = df[df['duration_category'] == 'Cluster 2']['num_subscribers']
    long = df[df['duration_category'] == 'Cluster 3']['num_subscribers']

    # Check the length and unique values of each group
    st.write(f"Cluster 1 (short) count: {len(short)}, unique values: {short.nunique()}")
    st.write(f"Cluster 2 (medium) count: {len(medium)}, unique values: {medium.nunique()}")
    st.write(f"Cluster 3 (long) count: {len(long)}, unique values: {long.nunique()}")

    if len(short) < 2 or len(medium) < 2 or len(long) < 2:
        st.write("Not enough data in one or more clusters to perform ANOVA.")
        return None, None

    stat, p_value = f_oneway(short, medium, long)
    st.write(f"ANOVA Test Statistic: {stat:.2f}, P-Value: {p_value:.5f}")
    if p_value < 0.05:
        st.write("There is a significant difference in the number of subscribers across duration categories.")
    else:
        st.write("No significant difference in subscribers across duration categories.")
    return stat, p_value


def analysis():
    """Display the BI case study for content duration vs. engagement and retention analysis."""
    st.title("BI: Content Duration vs. Engagement and Retention Analysis")

    df = load_data()
    df = preprocess_data(df)

    st.subheader("Exploratory Data Analysis")
    st.markdown(
        '<div style="background-color: #f0f0f0; padding: 10px;">This section provides summary statistics and visualizations to understand the distribution of content duration and number of subscribers.</div>',
        unsafe_allow_html=True)
    explore_data(df)

    st.subheader("Clustering Courses by Content Duration")
    st.markdown(
        '<div style="background-color: #f0f0f0; padding: 10px;">This section clusters courses into short, medium, and long categories based on content duration.</div>',
        unsafe_allow_html=True)
    df = cluster_courses_by_duration(df)
    if df is None:
        st.write("Clustering failed due to insufficient data in one or more clusters.")
        return

    st.subheader("Performance Metrics Analysis")
    st.markdown(
        '<div style="background-color: #f0f0f0; padding: 10px;">This section analyzes the performance metrics (ratings, reviews, subscribers) across different duration categories.</div>',
        unsafe_allow_html=True)
    analyze_performance_metrics(df)

    st.subheader("Yearly Trends Analysis")
    st.markdown(
        '<div style="background-color: #f0f0f0; padding: 10px;">This section examines trends in course metrics over the years.</div>',
        unsafe_allow_html=True)
    analyze_yearly_trends(df)

    st.subheader("Hypothesis Testing")
    st.markdown(
        '<div style="background-color: #f0f0f0; padding: 10px;">This section conducts ANOVA to determine if there is a significant difference in metrics across clusters.</div>',
        unsafe_allow_html=True)
    hypothesis_test(df)