

"""
Author : Abhishek Singh

To get top 5 documents in a distributed setup using Cosine Similarity
#I have used "https://www.snip2code.com/Snippet/672299/pandas-DataFrame-apply-multiprocessing" for implementation
"""



#Importing the libraries
import string, re, math, time, sys, pandas as pd
from operator import itemgetter
from collections import Counter
import numpy as np
import multiprocessing as mp






#Function for converting string to vectors
WORD = re.compile(r'\w+')
def text_to_vector(text):
    """
    :param text:
    :return: vectors
    """
    words = WORD.findall(text)
    return Counter(words)






#Function for measuring consine similarity
def cosine_sim(text1):
    """
    :param text1:
    :return: Cosine similarity based on TF-IDF score
    """
    vec1 = text_to_vector(text1.lower())
    vec2 = text_to_vector(search_text.lower())
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator





#Subsetting
def _apply_df(df):
    return df[df.String.str.contains(search_text, case = False)]





def _apply_df1(df):
    return df[df.String.str.contains(pattern, case = False)]
    
    



#Multiprocessing function
def apply_by_multiprocessing(df, **kwargs):
    workers = kwargs.pop('workers')
    pool = mp.Pool(processes=workers)
    result = pool.map(_apply_df, [(d) for d in np.array_split(df, workers)])
    pool.close()
    return pd.concat(list(result))





#function to get the best 5 strings
def similar_strings():
    """
    :return: 'n' most similar string to the search string
    The function will look for the most similar strings in our database.
    First as 1 string & later as a combination of words
    """
    df = pd.DataFrame(results , columns = ['String'], index = None)
    df0 = apply_by_multiprocessing(df, workers = 16)
    if (df0.shape[0] > 4):
        sim_scores = [] #List to store all similarity scores
        result = list(df0['String'])
        for i in range(len(result)):
            sim_scores.append(cosine_sim(result[i]))
        #Storing the scores
        d = dict(zip(result, sim_scores))
        best_5 = sorted(d.keys(), key = itemgetter(1), reverse = True)[:5]
    else:
        pattern = '|'.join(list(search_text.split(' '))) #Splitting the search string
        #Subsetting the large corpus to look for key strings
        df1 = apply_by_multiprocessing(df, workers = 16)
        sim_scores = [] #List to store all similarity scores
        result = list(df1['String'])
        for i in range(len(result)):
            sim_scores.append(cosine_sim(result[i]))
        #Storing the scores
        d = dict(zip(result, sim_scores))
        best_5 = sorted(d.keys(), key = itemgetter(1), reverse = True)[:5]
    #Return 5 strings
    for i in range(len(best_5)):
        print "\n" + best_5[i]





#Running the main function
if __name__ == '__main__':

    #Catching the input string
    search_text = sys.argv[-1]
    #Loading the database
    results = []
    with open("full_data.txt") as inputfile:
        for line in inputfile:
            results.append(line)
    print "Database Loaded"
    print "Print 5 most similar strings"
    start_time = time.time()
    similar_strings()
    print("--- %s seconds ---" % (time.time() - start_time))
    