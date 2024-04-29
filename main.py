from data_analyzer import DataAnalyzer

def main():
    # Path to the CSV file
    csv_file_path = 'data.csv'
    
    # Create an instance of DataAnalyzer
    analyzer = DataAnalyzer(csv_file_path)
    
    # Display basic statistics of the dataset
    print("Basic Statistics:")
    analyzer.show_basic_stats()
    
    # Plot histogram for the 'Salary' column
    print("Plotting Histogram for Salary...")
    analyzer.plot_histogram('Salary')
    
    # Plot correlation matrix
    print("Plotting Correlation Matrix...")
    analyzer.plot_correlation_matrix()
    
    # Plot scatter plot between 'Years_of_Experience' and 'Salary'
    print("Plotting Scatter Plot between Years of Experience and Salary...")
    analyzer.plot_scatter('Years_of_Experience', 'Salary')

if __name__ == '__main__':
    main()
