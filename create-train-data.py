import json
import os

with open("data/train-json.txt", 'w') as outfile:
    counter = 1;
    for dirname, direnames, filenames in os.walk('aclImdb/train/pos'):
        counter = counter+1
        if counter > 20000:
            break;
        for filename in filenames:
            with open(os.path.join(dirname, filename), 'r') as f:
                for line in f:
                    data = {}
                    data['content'] = line
                    data['sentiment'] = 'positive'
                    json.dump(data, outfile)
                    outfile.write("\n")

    for dirname, direnames, filenames in os.walk('aclImdb/train/neg'):
        counter = counter+1
        if counter > 40000:
            break;
        for filename in filenames:
            with open(os.path.join(dirname, filename), 'r') as f:
                for line in f:
                    data = {}
                    data['content'] = line
                    data['sentiment'] = 'negative'
                    json.dump(data, outfile)
                    outfile.write("\n")

    for dirname, direnames, filenames in os.walk('aclImdb/train/unsup'):
        counter = counter+1
        if counter > 40000:
            break;
        for filename in filenames:
            with open(os.path.join(dirname, filename), 'r') as f:
                for line in f:
                    data = {}
                    data['content'] = line
                    data['sentiment'] = 'unsupported'
                    json.dump(data, outfile)
                    outfile.write("\n")