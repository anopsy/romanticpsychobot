import csv
import time

file= open("romanticpsycho.csv", "r")
data = list(csv.reader(file, delimiter=","))
file.close()
clean=[]
for song in data:
    for lyrics in song:
        text = lyrics.split("<br/>")
        clean.append(text)
with open('romanticpsychoclean.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(clean)
  
# file= open("romanticpsychoclean.csv", "r")
# data = list(csv.reader(file, delimiter=","))
# file.close()

# for verse in data:
#     print(verse)