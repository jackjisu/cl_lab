import re
import random

with open('/Users/jackbyun/Documents/cl_lab/restaurants/menu_train.txt', 'r') as f:
    content = f.read()

def tokenize(text):
    # remove punctuation
    text = re.sub(r';', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    # tokenize
    tokens = text.lower().split()
    return tokens

def vocab(text):
 # remove punctuation
    text = re.sub(r';', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    # tokenize
    tokens = text.lower().split()
    vocab = {}
    types = list(set(tokens))
    return types

res_tokens = tokenize(content)
res_vocab = vocab(content)

with open('/Users/jackbyun/Documents/cl_lab/restaurants/menu_train.txt', 'r') as f:
    restaurants = f.readlines()

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
    return len(doc_matrix[0])

print(word_instance(restaurants))

'''
vocab = {}
for word in content_tokenized:
    if word not in vocab:
        vocab[word] = 1
    else:
        vocab[word] += 1
print(vocab['$'], vocab['$$'], vocab['$$$'], vocab['$$$$'])
'''

with open('/Users/jackbyun/Documents/cl_lab/restaurants/menu_dev-predicted.txt', 'r') as f:
    a = [line.strip() for line in f.readlines()]


