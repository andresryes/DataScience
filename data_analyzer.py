import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np  # Ensure NumPy is imported

class DataAnalyzer:
    def __init__(self, data_path):
        """
        Initializes the DataAnalyzer with a path to a dataset.
        
        :param data_path: str, the path to the dataset file
        """
        self.data = pd.read_csv(data_path)

    def show_basic_stats(self):
        """
        Prints basic statistics of the dataset.
        """
        print(self.data.describe())

    def plot_histogram(self, column, bins=10):
        """
        Plots a histogram for a specified column in the dataset.
        
        :param column: str, the name of the column to plot
        :param bins: int, the number of bins in the histogram
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[column], bins=bins, kde=True)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    def plot_correlation_matrix(self):
        """
        Plots the correlation matrix of the dataset, considering only numeric columns.
        """
        numeric_cols = self.data.select_dtypes(include=[np.number])
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_cols.corr(), annot=True, fmt=".2f", cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.show()

    def plot_scatter(self, x_column, y_column):
        """
        Plots a scatter plot between two specified columns.
        
        :param x_column: str, the name of the x-axis column
        :param y_column: str, the name of the y-axis column
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.data, x=x_column, y=y_column)
        plt.title(f'Scatter Plot between {x_column} and {y_column}')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.show()
