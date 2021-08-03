from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os

for name, hex in matplotlib.colors.cnames.items():
    print(name,hex)

def count(text):
    skips = [",",".","!","?",":",";",'"',"'"]
    for s in skips:
        text = text.replace(s,"")

    #word_counts = Counter(text.split())
    wordcount = {}
    text = text.lower()
    for word in text.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] +=1
    return wordcount

def read_book(tittle_path):
    with open(tittle_path, "r", encoding="utf-8") as current_file:
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text

eng_text = read_book("books\English\shakespeare\Romeo and Juliet.txt")
ger_text = read_book("books\German\shakespeare\Romeo und Julia.txt")

#ind = text.find("What's in a name?")
#sample_text = text[ind:ind+1000]

def word_stats(wordcount):
    num_unique = len(wordcount)
    counts = sum(wordcount.values())
    return (num_unique,counts)

num_unique1, counts1 = word_stats(count(eng_text))
num_unique2, counts2 = word_stats(count(ger_text))
#print(num_unique1, sum(counts1))
#print(num_unique2, sum(counts2))

df = pd.DataFrame(index=["English","German"], columns=["uniquewords","totalwords"])
df["uniquewords"]= num_unique1, num_unique2
df["totalwords"] = counts1, counts2
print(df)
df.plot(kind = "bar", color=["tomato","steelblue"], figsize = (10,10))
plt.ylabel("Frequency")
plt.xlabel("Translations")
plt.title("For shakespeare's Romeo and juliet")
plt.show()

stats = pd.DataFrame(columns=["language","author","title","length","unique"])
title_num = 1
book_dir = "./books"
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" +language):
        for title in os.listdir(book_dir + "/" +language + "/" + author):
            input_file = book_dir + "/" +language + "/" + author + "/" + title
            #print(input_file)
            text = read_book(input_file)
            num_unique, counts = word_stats(count(text))
            title = title.replace(".txt","")
            stats.loc[title_num] = language,author.capitalize(),title,counts,num_unique
            title_num+=1

print(stats.head())
plt.figure(figsize=(10,10))
ax = stats[stats.language == "English"]
plt.plot(ax.length, ax.unique, "o",label = "English", color = "darkblue")
ax = stats[stats.language == "French"]
plt.plot(ax.length, ax.unique,"o", label = "French", color = "violet")
ax = stats[stats.language == "German"]
plt.plot(ax.length, ax.unique,"o", label = "German", color = "yellowgreen")
ax = stats[stats.language == "Portuguese"]
plt.plot(ax.length, ax.unique,"o", label = "Portuguese", color = "turquoise")
plt.title("Length vs Unique words")
plt.legend()
plt.xlabel("length of the book")
plt.ylabel("number of unique words")
plt.savefig("books_plot.png")
plt.show()


