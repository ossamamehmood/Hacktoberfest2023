import gradio as gr
import pandas as pd
import datasets
import seaborn as sns
import matplotlib.pyplot as plt

df = datasets.load_dataset("merve/supersoaker-failures")
df = df["train"].to_pandas()
df.dropna(axis=0, inplace=True)

def plot(df):
  plt.scatter(df.measurement_13, df.measurement_15, c = df.loading,alpha=0.5)
  plt.savefig("scatter.png")
  df['failure'].value_counts().plot(kind='bar')
  plt.savefig("bar.png")
  sns.heatmap(df.select_dtypes(include="number").corr())
  plt.savefig("corr.png")
  plots = ["corr.png","scatter.png", "bar.png"]
  return plots

inputs = [gr.Dataframe(label="Supersoaker Production Data")]
outputs = [gr.Gallery(label="Profiling Dashboard", columns=(1,3))]

gr.Interface(plot, inputs=inputs, outputs=outputs, examples=[df.head(100)], title="Supersoaker Failures Analysis Dashboard").launch()