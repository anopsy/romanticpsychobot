import csv
import time

file= open("romanticpsycho.csv", "r")
data = list(csv.reader(file, delimiter=','))
file.close()
clean=[]
for song in data:
    for lyrics in song:
        text = lyrics.split("<br/>")
        for line in text:
            line=line.replace("</div>")
            line=line.replace("<div class=\"\"lyrics--text\"\">","")
        clean.append(text)
with open('quebott.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(clean)


print(type(song), type(lyrics), type(text), type(line), type(clean))
  
# file= open("romanticpsychoclean.csv", "r")
# data = list(csv.reader(file, delimiter=","))
# file.close()

# for verse in data:
#     print(verse)