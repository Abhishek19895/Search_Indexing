
"""
Author : Abhishek Singh

To create Box plots of the search times results from the 3 environments.
"""


#Importing the libraries
import numpy as np
import seaborn as sns, pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager





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
    plt.title("Document search time on " + title, fontsize = 16)
    plt.xlabel("Framework", fontsize = 12)
    plt.ylabel("Search time (secs)", fontsize = 12)
    plt.show();






def line_chart():
    title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} # Bottom vertical alignment for more space
    axis_font = {'fontname':'Arial', 'size':'14', 'color':'brown'}
    x = [1.5, 15, 60000]  ;  y = [4.2, 1, .2]  ;  xlabels = ['1.5 GB', '15 GB', '60,000 GB']
    ylabels = ['4.2 secs', '1 secs', '.2 secs'] ; a = [np.log10(i) for i in x]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim([0,200000])
    ax.set_ylim([0,5])
    plt.semilogx(x, y, basex = 10, linestyle = '--', marker = 'o', color = 'g')
    plt.xticks(a, xlabels)  ;   plt.yticks(y, ylabels)
    plt.xlabel('Database Size in Log Scale',**axis_font)
    plt.ylabel('Search time (secs)',**axis_font)
    ax.text(1, 4.3, 'Our search speed', style = 'italic', color='green', fontsize = 10)
    ax.text(1, 3.9, '1.5 GB', style = 'italic', color='blue', fontsize = 10)
    ax.text(15, 1.1, 'Wikipedia speed', style = 'italic', color='green', fontsize = 10)
    ax.text(12, 0.8, '15 GB', style = 'italic', color='blue', fontsize = 10)
    ax.text(30000, .4, 'Google speed', style = 'italic', color='green', fontsize = 10)
    ax.text(30000, 0, '60,000 GB', style = 'italic', color='blue', fontsize = 10)
    plt.title('Turnaround time in Search',  **title_font)
    plt.draw()









#Running the main function
if __name__ == '__main__':
    """
    Running the main function and Creating our box plots
    """
    #data from the local setup
    data_local = pd.DataFrame({
        'Python' : [26.8934, 23.0234, 106.5818, 110.2918, 22.5786, 25.8258, 26.7582, 145.5498, 22.7224, 24.0873],
        'Spark' : [105.4671, 22.6995 ,28.0056, 26.6647, 32.7345, 27.2541, 35.5522, 23.6273, 23.2861, 31.1599],
        'HIVE':[28.627, 29.309, 25.129, 25.091, 27.092, 25.099, 29.078, 25.09, 28.118, 24.029]})
    box_plot(data_local,  "Local setup")

    #data from the Distributed setup
    data_distributed = pd.DataFrame({
        'Spark' : [18.8136, 2.8560, 3.8339, 3.8396, 14.0846, 3.7468, 5.5799, 2.8850, 4.0924, 4.2536],
        'Python' : [16.0543, 12.6289, 22.7972, 23.0048, 13.3926, 11.3113, 11.6870, 22.6051, 11.4237, 11.3292],
        'HIVE':[19.145, 15.885, 15.777, 15.798, 15.776, 15.773, 15.779, 15.733, 15.713, 15.702]})
    box_plot(data_distributed,  "Distributed setup 16 nodes")