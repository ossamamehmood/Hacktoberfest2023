import gradio as gr
import pandas as pd
import datasets
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_clean_data():
    # Load the dataset and clean it
    df = datasets.load_dataset("merve/supersoaker-failures")
    df = df["train"].to_pandas()
    df.dropna(axis=0, inplace=True)
    return df

def plot(df):
    # Create and save scatter plot
    plt.scatter(df.measurement_13, df.measurement_15, c=df.loading, alpha=0.5)
    scatter_path = "scatter.png"
    plt.savefig(scatter_path)

    # Create and save bar plot
    df['failure'].value_counts().plot(kind='bar')
    bar_path = "bar.png"
    plt.savefig(bar_path)

    # Create and save correlation heatmap
    sns.heatmap(df.select_dtypes(include="number").corr())
    corr_path = "corr.png"
    plt.savefig(corr_path)

    return [corr_path, scatter_path, bar_path]

# Load the data once
df = load_and_clean_data()

inputs = [gr.Dataframe(label="Supersoaker Production Data")]
outputs = [gr.Gallery(label="Profiling Dashboard", columns=(1, 3))]

gr.Interface(plot, inputs=inputs, outputs=outputs, examples=[df.head(100)], title="Supersoaker Failures Analysis Dashboard").launch()
