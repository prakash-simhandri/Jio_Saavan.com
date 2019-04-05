from bs4 import BeautifulSoup
from urllib.request import urlopen
from pprint import pprint
import webbrowser

saavn_link=urlopen('https://www.jiosaavn.com')
soup=BeautifulSoup(saavn_link,'html.parser')
languags=soup.find('ul')
languags_li=languags.findAll('li')
def All_Languags(saavan):
	All_languags=[]
	count=1
	for i in saavan:
		print(count,i.text)
		count+=1
		All_languags.append(i.text)
	return(All_languags)
Languags_list=All_Languags(languags_li)
# print(Languags_list)
def country_songs_link(saavan):
	First_user_chose=int(input('\033[1;34mWhich country do you want to hear the Songs :) \033[1;m'))
	print(' ')
	join_link=saavan[First_user_chose-1]
	country_link=urlopen('https://www.jiosaavn.com/'+'new-releases/'+join_link.lower())
	soup_2=BeautifulSoup(country_link,'html.parser')
	Album=soup_2.findAll('div',class_='art-wrap')
	count=1
	film_songs=[]
	for data in Album:
		title=''
		movie_title_link=(data.find('a').get('href'))[31::]
		for names in movie_title_link:
			if '/' == names: 
				break
			else:
				title+=names
		print(count,title+'\n')
		count+=1
		film_songs.append(data.find('a').get('href'))
	return(film_songs)
movies_Album=(country_songs_link(Languags_list))
# print(movies_Album)

def movie_total_songs(saavan):
	Second_user_chose=int(input('\033[1;35mWhich movie do you want to hear the Songs ? >\033[1;m'))
	print(' ')
	new_Album=urlopen(saavan[Second_user_chose-1])
	soup_3=BeautifulSoup(new_Album,'html.parser')
	tabal=soup_3.findAll('div',class_="details content-list")
	count_=1
	for li in tabal:
		song_title=li.find('p',class_='song-name ellip')
		film_songs_title=''
		for i in song_title.text:
			if '\n' != i:
				film_songs_title+=i
			else:
				break

		print('\033[1;31m* *  \033[1;m'+'%s}  ' %count_+film_songs_title+'  \U0001F3B5 '+'\033[1;31m  * *\033[1;m'+"\n")
		count_+=1
	movie_link=soup_3.findAll('div',class_='content-cell num')
	All_divs=[]
	movie_songs_links=[]
	for x in movie_link:
		All_divs.append(str(x))
	one_data=[]
	for one in All_divs:
		one_data.append(one.split())
	for tow in (one_data):
		for j in tow:
			saport=(j)[:2]
			if 'hr' == saport:
				if 'href="h' == j[:7]:
					movie_songs_links.append(j)
	return(movie_songs_links)
All_musics=(movie_total_songs(movies_Album))
# print(All_musics)

def  play_the_music(saavan):
	Third_user_chose=int(input('\033[1;34mEnter the your chose song >\033[1;m'))
	play=webbrowser.open(saavan[Third_user_chose-1][6:-2])
	print(play)
	print('Thanks :)')
play_the_music(All_musics)