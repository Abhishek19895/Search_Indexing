
"""
Author : Abhishek Singh

To create Box plots of the search times results from the 3 environments.
"""


#Importing the libraries
import seaborn as sns, pandas as pd
import matplotlib.pyplot as plt




#Function to generate box plot from the data passed
def box_plot(df, title):
    """
    param: The input dataframe
    param: title of the chart
    :return: Outputs a Box plot from the dataframe passed
    """
    df = pd.melt(df, id_vars=None, value_vars=['Python', 'Spark', 'HIVE'])
    ax = sns.boxplot(x = df['variable'], y = df['value'],  width = .5, fliersize = 10
                , order = ["Spark", "Python", "HIVE"]);
    plt.title("Document search time on " + title, fontsize = 24)
    plt.xlabel("Framework", fontsize = 16)
    plt.ylabel("Search time (secs)", fontsize = 16)
    plt.show();






#Running the main function
if __name__ == '__main__':
    """
    Running the main function and Creating our box plots
    """
    #data from the local setup
    data_local = pd.DataFrame({
        'Python' : [26.8934, 23.0234, 106.5818, 110.2918, 22.5786, 25.8258, 26.7582, 145.5498, 22.7224, 24.0873],
        'Spark' : [105.4671, 22.6995 ,28.0056, 26.6647, 32.7345, 27.2541, 35.5522, 23.6273, 23.2861, 31.1599],
        'HIVE':[49, 61, 53, 43, 56, 44, 41, 31, 59, 34]})
    box_plot(data_local,  "Local setup")

    #data from the Distributed setup
    data_distributed = pd.DataFrame({
        'Spark' : [18.8136, 2.8560, 3.8339, 3.8396, 14.0846, 3.7468, 5.5799, 2.8850, 4.0924, 4.2536],
        'Python' : [16.0543, 12.6289, 97.7773, 89.9739, 13.3926, 11.3113, 11.6870, 135.3012, 11.4237, 11.3292],
        'HIVE':[19, 18, 16, 20, 21, 11, 15, 19, 17, 13]})
    box_plot(data_distributed,  "Distributed setup 16 nodes")