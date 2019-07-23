import pandas as pd
from collections import Counter
from constants1 import STOPWORDS
from tabulate import tabulate

file = input("What is the filename? ")
print("**\n{}\n**".format(file))
df = pd.read_csv('./{}'.format(file), encoding="ISO-8859-1")
cnt = Counter()
col = int(input("What column would you like me to read? "))


for row in df.itertuples(index=False):
    line = row[col - 1].lower()
    for word in line.split():
        word = word.replace(".", "")
        word = word.replace("-", "")
        word = word.replace(",", "")
        word = word.replace(":", "")
        word = word.replace("\"", "")
        word = word.replace("!", "")
        word = word.replace("(", "")
        word = word.replace(")", "")
        word = word.replace("*", "")
        word = word.replace("?", "")
        if len(word) <= 1:
            continue
        if word not in STOPWORDS:
            if word not in cnt:
                cnt[word] = 1
            else:
                cnt[word] += 1


n_print = int(input("How many of the most common words would you like to print: "))
word_counter = Counter(cnt)
for word, count in word_counter.most_common(n_print):
    print(word, ":", count)
lst = word_counter.most_common(100)
filename = input("what would you like the file to be named? Include ./ if it's in the same directory: ")
df2 = pd.DataFrame(lst, columns=['Word', 'Count'])
print(tabulate(df2, headers='word', showindex='never'))
export_csv = df2.to_csv(filename, index=None, header=True)

