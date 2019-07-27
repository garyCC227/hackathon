import google_vision
import analyze
import classification
import sys
import numpy as np


if __name__ == '__main__':
    model = classification.Classifier()
    filename = sys.argv[1]
    json_labels = google_vision.getJson(filename)
    selected_labels = analyze.toDataFrame(json_labels)
    # print (selected_labels)
    labels = []
    for key, value in selected_labels.items():
        labels.append(value)
    labels = np.array(labels)
    print (labels)
    model.classify(labels)
    # classification.naive_bayes(selected_labels)
