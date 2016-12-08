import json
import os

with open("data/test-json.txt", 'w') as outfile:
    counter = 1;
    for dirname, direnames, filenames in os.walk('aclImdb/test/pos'):
        counter = counter+1
        if counter > 1000:
            break;
        for filename in filenames:
            with open(os.path.join(dirname, filename), 'r') as f:
                for line in f:
                    data = {}
                    data['content'] = line
                    data['sentiment'] = 'positive'
                    json.dump(data, outfile)
                    outfile.write("\n")