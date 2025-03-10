#ROHAN ANAND MILESTONE 2 Project
def convertToDictionaries(keys, values):
    result = []
    for i in range(len(values)):
        d = {}
        for j in range(len(keys)):
            d[keys[j]] = values[i][j]
        result.append(d)
    return result

import csv

def loadRecords(filename):
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        # Skip the header row.
        next(reader)
        return list(reader)

def convertToLists(keys, lod):
  return [ [dict.get(key, "") for key in keys] for dict in lod ]

import csv

def writeRecords(filename, records):
  with open(filename, "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(records)