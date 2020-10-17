import requests
from bs4 import BeautifulSoup
from time import sleep
import sys

print('Live Cricket Matches:')
print('=====================')
url = "http://static.cricinfo.com/rss/livescores.xml"
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

i = 1
for item in soup.findAll('item'):
 print(str(i) + '. ' + item.find('description').text)
 print('------------------------------------------')
 i = i + 1

links = []    
for link in soup.findAll('item'):
 links.append(link.find('guid').text)

print('Enter match number or enter 0 to exit:')
while True:
 try:
  userInput = int(input())
 except NameError:
  print('Invalid input. Try Again!')
  continue
 except SyntaxError:
  print('Invalid input. Try Again!')
 if userInput < 0 or userInput > 30:
  print('Invalid input. Try Again!')
  continue
 elif userInput == 0:
  sys.exit()      
 else:
  break

url = links[userInput - 1]
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')  

while True:
 matchUrl = links[userInput - 1]
 r = requests.get(matchUrl)
 soup = BeautifulSoup(r.text,'lxml') 
 score = soup.findAll('title')       
 try:
  r.raise_for_status()
 except Exception as exc:
  print ('Connection Failure. Try again!')
  continue
 print(score[0].text + '\n')
 sleep(20)

