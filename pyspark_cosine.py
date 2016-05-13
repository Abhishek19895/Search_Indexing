
"""
Author: Tate Campbell
Using the Pyspark environment to to get similar documents on your text search
from a large corpus.
"""

import sys
from itertools import combinations
import numpy as np
from pyspark import SparkContext
from scipy.spatial.distance import cosine 

def parse_features(line, indices):
    """
    Converts a tab separated string into a list of (featureID, value) tuples
    """
    elems = line.split(',')
    return [(i, elems[v]) for i, v in enumerate(indices)]

def assign_indices(line, index):
	index += 1
	return (index.value, line)

def get_unique_word_list(article_str, search_str):
	"""
	Returns the unique list of words which occur in search string and an article string
	"""
	alist, slist = (article_str.split(), search_str.split())
	uniq = list(set(alist + slist))
	uniq = [u.lower().strip('.') for u in uniq]
	return uniq

def get_word_count_vec(unique_word_list, str_to_search):
	"""
	Returns an np.array with the counts of how many times each word in unique_word_list 
	appears in str_to_search
	"""
	counts = [str_to_search.lower().split().count(w) for w in unique_word_list]
	return np.array(counts)

def calc_cosine_sim(line, search_term):
	"""
	Returns a tuple of (cosine_similarity, article_index) given a line from RDD and a search term

	Line format: 
			(0, u'I have bought several of the Vitality canned dog food...')
	"""
	index, article = line[0], line[1]
	uniqs = get_unique_word_list(article, search_term)
	avec, svec = get_word_count_vec(uniqs, article), get_word_count_vec(uniqs, search_term)
	sim = 1 - cosine(avec, svec)
	return (sim, index)

def check_words_in_text(text, search_str):
	search_words = search_str.split()
	match = 0
	for word in search_words:
		if word.lower() in text.lower():
			match += 1
	if match == len(search_words):
		return True
	else:
		return False


index = sc.accumulator(0) 
rdd = sc.textFile('full_data.txt')
data = rdd.zipWithIndex()
master = data.map(lambda l: (l[1], l[0]))



test_article_str = master.take(1)[0][1][1]

#test_article_contents:

"""I have bought several of the Vitality canned dog food products and 
have found them all to be of good quality. The product looks more like a 
stew than a processed meat and it smells better. My Labrador is finicky and 
she appreciates this product better than most.
"""

test_search_str = 'dog food'

test_uniq_word_list = get_unique_word_list(test_article_str, test_search_str)

get_word_count_vec(test_uniq_word_list, test_article_str)

article_counts = get_word_count_vec(test_uniq_word_list, test_article_str)
search_counts = get_word_count_vec(test_uniq_word_list, test_search_str)

print cosine(article_counts, search_counts)

#cosine sim = 1 - 0.8285

test_all_sims = master.map(lambda line: calc_cosine_sim(line, test_search_str)).collect()


## TEST TIMES

start_time = time.time()
test_search_str = 'Dog food'
d = master.filter(lambda line: check_words_in_text(line[1], test_search_str))
d.map(lambda line: calc_cosine_sim(line, test_search_str)).takeOrdered(5, key=lambda line: line[1])
print "Time Taken: %f seconds" % (time.time() - start_time)





