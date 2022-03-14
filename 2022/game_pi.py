import sys
import time
IMGNAME = "img.jpg"
IMG2TXT = "PI.html"
DIGITS = "digitsPI.txt"

def writetxt(name,msg):
	with open(name, "w") as file:
		file.write(msg)
		file.close()

def readtxt(name):
	with open(name, "r") as file:
		return file.readline()

def getImg(url):
	import requests
	imgrequ = requests.get(url).content
	with open(IMGNAME, "wb") as file:
		file.write(imgrequ)

def img2asciiart(img,size = 15,intensity = 255,replaceItem = 0,items = ["@"," "]):
	import cv2
	from numpy import asarray 
	dataFile = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
	imgresized  = cv2.resize(dataFile , (size, size)) 
	imgstr = ""
	for count in range(len(imgresized)):
		for cont in range(len(imgresized[count]))  :
				if imgresized[count,cont]//intensity == replaceItem:
					imgstr += next(items[0])
				else:
					imgstr += items[1]
		imgstr += "\n"
	return imgstr

def printscoreTable(scoreTable):
	txt="\n\nScore table:"
	txt+="\n"+("-"*50)+"\n"
	for i in range(len(scoreTable)):
		txt+="Name:\t"+str(scoreTable[i][0])+"  playstatus:"+str(scoreTable[i][5])
		txt+="\n"+("-"*50)+"\n"
		txt+="\nLevel:\t"+str(scoreTable[i][1])+"\nScore:\t"+str(round(scoreTable[i][2],5))
		txt+="\n"+("-"*50)+"\n\n"
	print(txt)

def betterPlayer(score):
	name=score[0][0]
	betterScore=score[0][2]
	for i in range(len(score)):
		if betterScore<score[i][2]:
			betterScore=score[i][2]
			name=score[i][0]
	return name,str(round(betterScore,10))

def timecount(turn,msg):
	print("next player is:\n\t"+turn)
	time1=time.time()
	num=input(msg+"?:\n")
	time2=time.time()
	return num,(time2-time1)

def game(digitspi):
	banner="""
 _____  _ _  _        
|___ / / | || |       
  |_ \ | | || |_      
 ___) || |__   _| _ _ 
|____(_)_|  |_|(_|_|_)
                      
	"""
	instruccions="""
	[RULES]:
* writes characters 1 by 1
* only use 0123456789 and .

\nPi hero
who know next digit of pi

\nPi competition
who know more digits of pi
"""

	print(banner+instruccions)
	gamemode=input("Chose game mode\npi hero[H] or pi competition[C]").lower()
	players=input("number of players(default=1)")

	score=0
	level=0
	try:
		players=int(players)
	except:
		players=1
	if not players:
		players=1

	if players>=0:
		scoreTable=[]
		for ii in range(players):
			username=input("Username (default=player"+str(ii+1)+"):")
			if not username or username=="":
				username="player"+str(ii)
			scoreTable.append([username,0,0,"","",True])

	if not gamemode:
		gamemode="h"
	if gamemode=="h" or gamemode=="pi hero" or gamemode=="pihero" or gamemode=="hero":
		i=0
		picolective=""
		diedPlayerscounter=0
		while True:
			if scoreTable[i%players][5]:
				num,timer=timecount(str(scoreTable[i%players][0]),"\nnext digit of"+picolective)
				diedPlayerscounter=0
			else:
				if diedPlayerscounter>players:
					name,bestScore=betterPlayer(scoreTable)
					print(diedPlayerscounter,players)
					try:
						img=img2asciiart(IMGNAME,size=int(bestScore),items=[iter(digitspi)," "])
					except:
						img=""
					print("congratularions "+name+" you socore was "+str(bestScore)+"\n\n"+img)
					print("your pi is"+str(picolective))
					printscoreTable(scoreTable)
					break
				diedPlayerscounter+=1
				i+=1
				continue

			if num==digitspi[level]:
				score+=(i+0.1*level)/(timer)
				scoreTable[i%players][1]=level
				scoreTable[i%players][2]=((i+0.1*level)/(timer))+int(score/10)
				picolective+=digitspi[level]
				level+=1
			else:
				print("Wrong answer "+scoreTable[i%players][0]+", you typed "+num+", the answer is:\n"+digitspi[level])
				scoreTable[i%players][5]=False

			if i%players==0:
				printscoreTable(scoreTable)
			elif i%5==0:
				printscoreTable(scoreTable)
			i+=1
	if gamemode=="c" or gamemode=="pi competition" or gamemode=="picompetition" or gamemode=="competition":
		for i in range(len(scoreTable)):
			nums,timer=timecount(str(scoreTable[i%players][0]),"please enter your pi digits")
			if nums==digitspi[:len(nums)]:
				scoreTable[i%players][2]=((len(nums)/(timer))*10*players)
			else:
				print("wrong answer, answer must be"+str(digitspi[:len(nums)]))
				scoreTable[i%players][2]=0
		try:
			img=img2asciiart(IMGNAME,size=int(bestScore),items=[iter(digitspi)," "])
		except:
			img=""
		name,bestScore=betterPlayer(scoreTable)
		print("congratularions "+name+" you socore was "+str(bestScore)+"\n\n"+img)
		printscoreTable(scoreTable)


def main():
	digitspi = readtxt(DIGITS)
	game(digitspi)
	
main()