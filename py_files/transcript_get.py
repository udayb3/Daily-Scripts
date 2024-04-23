from youtube_transcript_api import YouTubeTranscriptApi
from pandas import read_csv, DataFrame as DF

file_read= "info_b4/id4.csv";  file_write="transcript4.csv"
df= read_csv( file_read )

transcript_all= []
id_all= []

n_id=  len( df['title'] )
for i in range( n_id ):

  try:
    subt= YouTubeTranscriptApi.get_transcript( df['title'][i] )
    transcript= ""

    n= len(subt)
    for j in range(n):
      transcript += subt[j]['text'] + " "
    
    id_all.append( df['title'][i] )
    transcript_all.append(transcript)
  except:
    print(f"{i}: {df['title'][i]}")

# Removing new line character from the transcript
n_nid= len(transcript_all)
for i in range(n_nid):
  
  st:str= transcript_all[i]
  transcript_all[i]= ( st.replace('\n',' ') ).replace("|"," ")

# Storing the transcript in the csv files
data= { 'Transcript' : transcript_all, 'Id': id_all }
df= DF(data)
df.to_csv(file_write, index=False , sep="|")