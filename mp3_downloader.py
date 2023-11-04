import csv
import pytube

with open('music.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        file_name = row[0] + "_" + row[1] + ".mp3"
        file_name = file_name.replace(" ","")
        yt = pytube.YouTube(row[2])
        print(file_name)


#yt = YouTube( 
#    str(input("Enter the URL of the video you want to download: \n>> "))) 
  
# extract only audio 
#video = yt.streams.filter(only_audio=True).first() 
  
# check for destination to save file 
#print("Enter the destination (leave blank for current directory)") 
#destination = str(input(">> ")) or '.'
  
# download the file 
#out_file = video.download(output_path=destination) 