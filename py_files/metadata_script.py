#!/usr/bin/python3

"""
- Remove the first line if you are running in windows.

- The requirements for this script are firefox browser, "selenium", "pandas" and "youtube_transcript_api".

- The script takes about 30-60 seconds to run for the playlist

- It has been tested on the following playlists and it worked correctly for the time being:
  https://youtube.com/playlist?list=PLUkIJZnuP8Qc6EhYTDjdCbuybsntcvxUl
  https://www.youtube.com/playlist?list=PLlloYVGq5pS677guzwj2KBB0p8SOE-V4p
  https://www.youtube.com/playlist?list=PLAhTBeRe8IhNWqzhdcKz8VOoYH2tE5Pt0
  https://www.youtube.com/playlist?list=PLMilupvERrnDxPdDAOw0q4xpdVIYgxv7J
  https://www.youtube.com/playlist?list=PLSnt4mJGJfGgUmhSYGAklQ3B98Z7xOq8C
  https://www.youtube.com/playlist?list=PLizNJ81QROQfwS9Rb4745S4sseuubQXLN
  https://www.youtube.com/playlist?list=PL2w4TvBbdQ3sMABf317ExCob_v6rW2-4s
  https://www.youtube.com/playlist?list=PL2X2odndvaIcmb5lqB5HmYqBV4QB2DXQD
  https://www.youtube.com/playlist?list=PL5uULy4b0kV6KX3-osKJR4FCdCJdh31cf
  https://www.youtube.com/playlist?list=PLNxd9fYeqXeaUjZaAFlr6O9irsL2ObF_M
  https://www.youtube.com/playlist?list=PLmT1H52OB8n0_9QofKIbIhgH8Dif4HkKP
  https://www.youtube.com/playlist?list=PLgFM5yHV8_w0Us5y_5GpJC7E12mLcBQUI
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pandas import DataFrame as df

list_link= ""

# Initializing the firefox version of the webdriver
driver= webdriver.Firefox()

# opening the youtube playlist
driver.get( list_link )
sleep(4)

# Data strcuture to store all the meta data
info= {'title':[], 'link':[], 'video_id':[], 'thumbnail_link':[]}
start= 0
height= 60

# Taking title, link and the name of the video
query2= driver.find_elements(By.ID, "meta")
videos1= query2[0:len(query2)-1 ]
n1= len(videos1)

# Taking link for thumbnails
temp2= driver.find_elements(By.ID, 'thumbnail')
temp2= temp2[1:len(temp2)-1]
videos2=[]
for i in range(len(temp2)):

  if(temp2[i].tag_name=='a'):
    videos2.append( temp2[i].find_element(By.TAG_NAME, 'img').get_attribute('src') )
  
  driver.execute_script(f"window.scrollTo({start}, {start+height})")
  start += height

for i in range(n1):
  
  link= query2[i].find_element(By.TAG_NAME, "a").get_attribute('href')
  info['link'].append( link )
  info['title'].append( query2[i].find_element(By.TAG_NAME, "a").get_attribute('title') )
  info['video_id'].append( ( link.split("=")[1] ).split("&")[0] )
  info['thumbnail_link'].append( videos2[i] )

driver.close()

# Converting the list into a dataframe
data= df(info)
data.to_csv('./trial1.csv', sep=",", index= False)