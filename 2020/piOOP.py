print("    ╔"+("="*83)+"╗")
print("       _____  _ _  _   _ ____  ___ ____   __  ____ _________  ___     ____              ")
print("      |___ / / | || | / | ___|/ _ \___ \ / /_| ___|___ / ___|/ _ \   |  _ \  __ _ _   _ ")
print("        |_ \ | | || |_| |___ \ (_) |__) | '_ \___ \ |_ \___ \ (_) |  | | | |/ _` | | | |")
print("       ___) || |__   _| |___) \__, / __/| (_) |__) |__) |__) \__, |  | |_| | (_| | |_| |")
print("      |____(_)_|  |_| |_|____/  /_/_____|\___/____/____/____/  /_/   |____/ \__,_|\__, |")
print("\t "*10,"|___/ ")
print("    ╚"+("="*83)+"╝")
class pi():
	def __init__(self,roundnum,n):
		self.roundnum = roundnum
		self.n = n

	def poligonos(self):
		self.r=1
		self.A=4*((2)**(1/2))*self.r
		self.B=8*self.r
		self.m=4;
		while self.m*2 <= self.n :
 			self.B=2*self.A*self.B/(self.A+self.B)
 			self.A=(self.A*self.B)**(1/2)
 			self.m=self.m*2
		self.pi = round((self.A/2/self.r + self.B/2/self.r  )/2,self.roundnum)
		self.err = round((  self.A/2/self.r - self.B/2/self.r  )/2,self.roundnum)
		return self.pi

n = int(input("\nNúmero de lados máximo del polígono : "))
pi = pi(500,n)
numpi =  pi.poligonos() 		
#print (err)
print (numpi)
