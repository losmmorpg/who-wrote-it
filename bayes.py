# Bayes classifier.
# Andrew Wang

import os
import tally

NUM_WORDS = 25

# classifies testWords based on the model in modelData
def bayes(testWords, modelData):
    totalWords = 0
    totalFiles = 0
    for category, (words, numWords, numFiles) in modelData.items():
        totalWords += numWords
        totalFiles += numFiles

    prob = {}
    totalProb = 0.0
    for category, (words, numWords, numFiles) in modelData.items():
        p = 1.0
        for word in testWords:
            count = words[word] if word in words else 1
            p *= count / (numWords if numWords > 0 else 1)
        p *= numFiles / totalFiles
        prob[category] = p
        totalProb += p

    predictions = {}
    for category in modelData:
        predictions[category] = prob[category] / totalProb

    return predictions

def print_percents(dict, total):
    items = list(dict.items())
    items = tally.slice_top(items, 0)

    percents = []
    for word, count in items.items():
        percents.append((word, round(count / total, 3)))

    print(sorted(percents, key=lambda x: x[1], reverse=True))

# train model using authors found in categories.txt
file = open("categories.txt", "r")
categories = []
for line in file:
    line = line.strip().lower()
    if line:
        categories.append(line)

model = {}
for category in categories:
    subdir = category + "/"
    filenames = os.listdir(subdir)

    topWords = {}
    totalWords = 0
    totalFiles = len(filenames)
    for filename in filenames:
        file = open(subdir + filename, "r", encoding="utf-8")
        topWords = tally.merge_tallies(topWords, tally.tally(file, NUM_WORDS), NUM_WORDS)
        file.seek(0)
        totalWords += tally.wordcount(file)

    print("Probability model for", category, end=": ")
    print_percents(topWords, totalWords)
    model[category] = topWords, totalWords, totalFiles
# output results
print()
print("Finished learning model for categories:", categories)
print("--")

# testing phase
print("Prediction model ready.")
while True:
    print("Enter name of file to be classified: ", end="")
    filename = input()
    file = open(filename, "r", encoding="utf-8")
    words = tally.tally(file, NUM_WORDS)
    if len(words) > 0:
        file.seek(0)
        total = tally.wordcount(file)

        predictions = bayes(words, model)   # use the Bayes model to predict which category the file is in

        # decide which prediction to go with (the one with highest probability)
        max_probability = 0
        cur_prediction = ""
        for prediction in predictions:
            probability = predictions[prediction]
            if probability > max_probability:
                max_probability = probability
                cur_prediction = prediction
        print()
        print("*** Predicted category:", cur_prediction, "***")
        print()


'''
filenames = os.listdir("test/")
success = 0
fail = 0
for filename in filenames:
    file = open("test/" + filename, "r", encoding="utf-8")

    words = tally.tally(file, NUM_WORDS)
    if len(words) > 0:
        file.seek(0)
        total = tally.wordcount(file)

        dict = bayes(words, model)
        if dict["shakespeare"] > 0.5:
            success += 1
        else:
            print("failed", filename)
            fail += 1
print("success:", success, " / fail:", fail, " / ratio:", success/fail if fail > 0 else "inf")
'''
