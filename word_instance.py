import re
import numpy as np

with open('/Users/jackbyun/Documents/cl_lab/restaurants/menu_train.txt', 'r') as f:
    content = f.read()

def vocab(text):
 # remove punctuation
    text = re.sub(r';', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    # tokenize
    tokens = text.lower().split()
    vocab = {}
    types = list(set(tokens))
    return types

res_vocab = vocab(content)

with open('/Users/jackbyun/Documents/cl_lab/restaurants/menu_train.txt', 'r') as f:
    restaurants = f.readlines()

"""warning: works but insane runtime, use sparingly/ with caution!!!"""

def word_instance(docs):
    doc_matrix = []
    for doc in docs:
        doc_types = vocab(doc) # create vocabulary for each restaurant
        doc_dict = {key: 0 for key in res_vocab} # for keeping track of type occurence 
        for type in doc_types:
            if type in res_vocab:
                doc_dict[type] += 1 
        doc_vec = list(doc_dict.values()) # create binary vector from doc_dict values
        doc_matrix.append(doc_vec)
    return np.array(doc_matrix)


