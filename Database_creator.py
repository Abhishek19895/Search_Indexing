
"""
Author : Abhishek Singh

To create our search database from APIs, Amazon Public data, Stanford Database & Kaggle datasets
"""


##loading all the concerned libraries for this database packing
import os, sys, pandas as pd
import numpy as np
import json
from collections import defaultdict
import glob



#function for loading data from the 'Emails' csv file
def csv_loader():
    """
    input: The csv file whose text is extracted
    :return: Shall return a list will all the text loaded
    """
    data = pd.read_csv('data/Reviews.csv')
    data1 = data['Text'] #Extracting only the textual information
    return list(data1)





#function for loading data from the Multiple csv files of NYTimes
def multiple_csv_loader():
    """
    input: The list of csv files whose text is extracted
    :return: Shall return a list will all the text loaded
    """
    list1 = glob.glob('data/nyt_data/*.csv')
    dfs = [] #To store all the files
    for filename in list1:
        data = pd.read_csv(filename)
        #reading each row of the csv file
        for i in range(data.shape[0]):
            l = str(data.iloc[i]['headline'])
            if l:
                dfs.append(l)
        #End of Inner loop for a single document
    #End of Outer loop for all the documents
    return dfs





#Function for loading txt files 'Movie' Review
def txt_loader():
    """
    input: The list of txt files whose text is extracted
    :return: Shall return a list will all the text loaded
    """
    list1 = glob.glob('data/test/pos/*.txt')  ;  list2 = glob.glob('data/test/neg/*.txt')
    list3 = glob.glob('data/train/pos/*.txt')  ;  list4 = glob.glob('data/train/neg/*.txt')
    list = list1 + list2 + list3 + list4 #Appending all the files
    all_files = [] #list to store all names
    for fileName in list:
        fin = open( fileName, "r" )
        data_list = fin.readlines()
        all_files.append(data_list)
    return all_files





#Function to load data from Amazon Beauty JSON file
def json_loader1():
    """
    Reading the the reviews JSON file and storing it as a list
    Output: Shall return a list will all the text loaded
    """
    data  =  []
    with  open('data/reviews_Beauty.json')  as  f:
        for  line  in  f:
            data.append(json.loads(line))
    data_list  =  []
    #transforming the json files into a list of tuples
    for i  in  data:
        text  =  i.get('reviewText',None)
        #removing unicodes from the various elements
        if  text:
            text  =  text.encode('utf-8')
        data_list.append(text)
    return  data_list





#Function to load data from Amazon Pets Review JSON file
def json_loader2():
    """
    Reading the the reviews JSON file and storing it as a list
    Output: Shall return a list will all the text loaded
    """
    data  =  []
    with  open('data/reviews_Pet_Supplies.json')  as  f:
        for  line  in  f:
            data.append(json.loads(line))
    data_list  =  []
    #transforming the json files into a list of tuples
    for i  in  data:
        text  =  i.get('reviewText',None)
        #removing unicodes from the various elements
        if  text:
            text  =  text.encode('utf-8')
        data_list.append(text)
    return data_list





#Function to download data from twitter
def twitter_data():
    """
    Reading the the reviews JSON file and storing it as a list
    Output: Shall return a list will all the text loaded
    """
    data  =  []
    with  open('data/twitter.json')  as  f:
        for  line  in  f:
            data.append(json.loads(line))
    data_list  =  []
    #transforming the json files into a list of tuples
    for i  in  data:
        text  =  i.get('text',None)
        #removing unicodes from the various elements
        if  text:
            text  =  text.encode('utf-8')
        data_list.append(text)
    return  data_list








#Running the main function
if __name__ == '__main__':
    """
    Running the main function and Creating our master database
    """
    all_data = [] #Empty list
    a = csv_loader()  #Adding the data from Hillary Clinton's Emails (Kaggle)  (568454 rows)
    a = a + multiple_csv_loader()  #Adding the NYtimes data  (27794 rows)
    a = a + txt_loader()  #Adding the data from Stanford Database  (50000 rows)
    a = a + json_loader1()  #Adding the Amazon beauty product reviews  (2023082 rows)
    a = a + json_loader2()  #Adding the Amazon Pets reviews  (1235329 rows)
    a = a + twitter_data()  #Adding the tweets  (50000 rows)
    all_data = pd.DataFrame(a) #Making a Dataframe of the giant list (4100 rows)
    print " Exporting the dataframe to a txt file"
    all_data
    all_data.to_csv('full_data.txt', header = None, index=False)



