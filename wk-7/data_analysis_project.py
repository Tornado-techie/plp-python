import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np

def load_data():
    try:
        iris = load_iris(as_frame=True)
        df = iris.frame
        print("Dataset loaded successfully!\n")
        return df
    except Exception as e:
        print("Error loading dataset:", e)
        return None

def inspect_data(df):
    print("First 5 rows of the dataset:")
    print(df.head(), "\n")

def explore_structure(df):
    print("Data Types:")
    print(df.dtypes, "\n")
    
    print("Missing Values:")
    print(df.isnull().sum(), "\n")

def clean_data(df):
    df_clean = df.dropna()
    print("Cleaned data shape:", df_clean.shape)
    return df_clean

def basic_statistics(df):
    print("Descriptive Statistics:")
    print(df.describe(), "\n")

def group_analysis(df):
    print("Mean measurements grouped by species:")
    print(df.groupby('target').mean(), "\n")

def line_chart(df):
    df_sorted = df.sort_values(by='sepal length (cm)')
    plt.figure(figsize=(8,5))
    plt.plot(df_sorted['sepal length (cm)'], label='Sepal Length over samples')
    plt.title('Line Chart: Sepal Length over sorted samples')
    plt.xlabel('Sample Index')
    plt.ylabel('Sepal Length (cm)')
    plt.legend()
    plt.tight_layout()
    plt.show()

def bar_chart(df):
    means = df.groupby('target')['petal length (cm)'].mean()
    plt.figure(figsize=(7,5))
    sns.barplot(x=means.index, y=means.values)
    plt.title('Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length (cm)')
    plt.tight_layout()
    plt.show()

def histogram(df):
    plt.figure(figsize=(7,5))
    sns.histplot(df['sepal width (cm)'], bins=15, kde=True)
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

def scatter_plot(df):
    plt.figure(figsize=(7,5))
    sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='target', data=df)
    plt.title('Sepal Length vs Petal Length by Species')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species')
    plt.tight_layout()
    plt.show()

def observations():
    print("Key Observations:")
    print("- Sepal and petal lengths increase together — strong positive correlation.")
    print("- Species differ significantly in petal size.")
    print("- Sepal width is more evenly distributed compared to petal measurements.\n")

if __name__ == "__main__":
    df = load_data()
    if df is not None:
        inspect_data(df)
        explore_structure(df)
        df_clean = clean_data(df)
        basic_statistics(df_clean)
        group_analysis(df_clean)
        line_chart(df_clean)
        bar_chart(df_clean)
        histogram(df_clean)
        scatter_plot(df_clean)
        observations()
