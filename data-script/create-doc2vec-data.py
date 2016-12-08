import os

with open("data/doc2vec-corpus-shuffled.txt", 'w') as outfile:
    for dirname, direnames, filenames in os.walk('aclImdb/train/neg'):
        for filename in filenames:
            with open(os.path.join(dirname, filename), 'r') as f:
                outfile.write(f.read())
                outfile.write("\n")

    for dirname, direnames, filenames in os.walk('aclImdb/train/pos'):
        for filename in filenames:
            with open(os.path.join(dirname, filename), 'r') as f:
                outfile.write(f.read())
                outfile.write("\n")

    for dirname, direnames, filenames in os.walk('aclImdb/train/unsup'):
        for filename in filenames:
            with open(os.path.join(dirname, filename), 'r') as f:
                outfile.write(f.read())
                outfile.write("\n")

    for dirname, direnames, filenames in os.walk('aclImdb/test/neg'):
        for filename in filenames:
            with open(os.path.join(dirname, filename), 'r') as f:
                outfile.write(f.read())
                outfile.write("\n")

    for dirname, direnames, filenames in os.walk('aclImdb/test/pos'):
        for filename in filenames:
            with open(os.path.join(dirname, filename), 'r') as f:
                outfile.write(f.read())
                outfile.write("\n")