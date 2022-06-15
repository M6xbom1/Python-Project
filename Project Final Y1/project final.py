import csv
import os

with open("News for project test.txt","r") as a:
    Project = a.read()
    clear = Project.replace(".","").replace(",","").replace('''"''',"").lower().split()

a = {}
word = []
feq = []

for i in clear:
  if i.isalpha():
    a.update({i: clear.count(i)})
    a = dict(sorted(a.items(), key=lambda item: item[1], reverse=True ))

for i in range(len(a)):
    word.append(list(a.keys())[i])
    feq.append(list(a.values())[i])


file = open("ProjectFinal.csv","w")

file.write("Word,Fequency\n")

for i in range(len(word)):
    file.write("%s,  %s\n" %(word[i], feq[i]))

file.close()
