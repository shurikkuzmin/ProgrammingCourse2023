import csv
import pytube
import os

with open('music.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        file_name = row[0] + "_" + row[1] + ".mp3"
        file_name = file_name.replace(" ","")
        
        if os.path.exists(file_name):
            print("Skipping " + file_name)
            continue
        yt = pytube.YouTube(row[2])
        audio = yt.streams.filter(only_audio=True).first() 
        out_file = audio.download(filename=file_name)          
        print("Downloaded " + file_name)
