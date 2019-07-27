import glob
import json
import numpy as np
import csv

def toDataFrame(file):
    target_labels = ['Muscle', 'Chest', 'Bodybuilder', 'Abdomen',
                     'Fitness professional', 'Bodybuilding', 'Stomach',
                     'Model', 'Arm', 'Shoulder', 'Waist']

    data = file
    dic = {}
    for label in data['labelAnnotations']:
        dic[label['description']] = label['score']
    result = []
    for label in target_labels:
        if label in dic:
            result.append(dic[label])
        else:
            result.append(np.nan)

    return ({target_labels[0]: result[0],
             target_labels[1]: result[1],
             target_labels[2]: result[2],
             target_labels[3]: result[3],
             target_labels[4]: result[4],
             target_labels[5]: result[5],
             target_labels[6]: result[6],
             target_labels[7]: result[7],
             target_labels[8]: result[8],
             target_labels[9]: result[9],
             target_labels[10]: result[10]})
