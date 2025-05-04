import random
with open('/Users/jackbyun/Documents/cl_lab/restaurants/menu_dev-predicted.txt', 'r') as f:
    gold = [line.strip() for line in f.readlines()] #create list of labels from file of only labels, remove whitespaces

shuffled = gold.copy() # baseline: random labels
random.shuffle(shuffled)

def f1(correct, predicted):
    labels = ['$', '$$', "$$$", '$$$$']
    f1_scores = {}
    
    for label in labels: # calculate f1 scores for each label
        tp = tn = fp = fn = 0
        for label_a, label_b in zip(correct, predicted): # zip() creates tuples with elements from same indexes from two iterators
            if label_a == label and label_b == label: # count true positives
                tp += 1
            elif label_a != label and label_b != label: # count true negatives
                tn += 1
            elif label_a != label and label_b == label: # count false positives
                fp += 1
            elif label_a == label and label_b != label: # count false negatives
                fn += 1
            else:
                print('ERROR: check file formatting')       
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        f1_scores[label] = f1

    return f1_scores, f"Average : {(f1_scores['$'] + f1_scores['$$'] + f1_scores['$$$'] + f1_scores['$$$$'])/len(labels)}"
    # dataset labels/f1 scores imbalanced; weight average by label?

print("Sanity Check #1: eval, eval -", f1(gold, gold))
print("Sanity Check #2: eval, random -", f1(gold, shuffled))
# print("Sanity Check #3: eval, predicted -", f1(gold, dev_pred))
