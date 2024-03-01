import subprocess
import csv

PATH = "ak\AquesTalkPlayer.exe"
RC="れいむ"
LC="まりさ"


n=0
def AQtalk(word,preset):
    global n
    output="on/"+str(n)+"_"+preset+"_"+word+".wav"
    subprocess.run(" ".join(["start", PATH, "/T", "\""+word+"\"", "/P", preset, "/W", output]), shell=True)
    n+=1





with open('serif.csv',encoding="UTF-8") as f:
    reader = csv.reader(f)
    for tang in  reader:
        AQtalk(tang[0],tang[1])
        print(tang)
    