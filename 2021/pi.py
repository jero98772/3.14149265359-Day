import sys
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
	#imgstr = []	
	imgstr = ""
	#imgstr = asarray(imgresized , dtype= str)
	for count in range(len(imgresized)):
		#imglist.append([])		
		for cont in range(len(imgresized[count]))  :
				if imgresized[count,cont]//intensity == replaceItem:
					#imgstr[count,cont]= next(items[0])
					#imgstr[count].append(next(items[0]))
					imgstr += next(items[0])
				else:
					#imgstr[count,cont] = items[1]
					#imgstr[count].append(items[1])
					imgstr += items[1]
		imgstr += "\n"
	return imgstr
def main():
	try:
		url = str(sys.argv[1]) 
		print("verifies settings like \n * image size and image quality \n * color and transparency \nalso the url\n"+url+"\n"*2)
	except:
		url = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.phys.org%2Fnewman%2Fgfx%2Fnews%2Fhires%2Fpi.jpg&f=1&nofb=1"
	getImg(url)
	img = img2asciiart(IMGNAME,size = 50,items=[iter(readtxt(DIGITS))," "])
	writetxt(IMG2TXT, "<pre>"+img+"</pre>")
	print(img)
main()