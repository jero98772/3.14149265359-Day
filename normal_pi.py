print("       _____  _ _  _   _ ____  ___ ____   __  ____ _________  ___     ____              ")
print("      |___ / / | || | / | ___|/ _ \___ \ / /_| ___|___ / ___|/ _ \   |  _ \  __ _ _   _ ")
print("        |_ \ | | || |_| |___ \ (_) |__) | '_ \___ \ |_ \___ \ (_) |  | | | |/ _` | | | |")
print("       ___) || |__   _| |___) \__, / __/| (_) |__) |__) |__) \__, |  | |_| | (_| | |_| |")
print("      |____(_)_|  |_| |_|____/  /_/_____|\___/____/____/____/  /_/   |____/ \__,_|\__, |")
print("\t "*10,"|___/ ")

import math
roundnum=500
n =eval(input("\nNúmero de lados máximo del polígono : "))
r=1
A=4*math.sqrt(2)*r
B=8*r
m=4;
while m*2<=n :
 B=2*A*B/(A+B)
 A=math.sqrt(A*B)

 m=m*2
m=round(m,roundnum)
pi= round((A/2/r + B/2/r  )/2,roundnum)
pi=round(pi,roundnum)
err = round((  A/2/r - B/2/r  )/2,roundnum)
err=round(err,roundnum)
print (err)
print (pi)

#print("  ╔════════════════════════════════════════════════════════════════════════════════════════╗")
#print("  ║                Con un polígono de ",m," lados, obtenemos:")
#print("  ║")
#print("  ║                       ","Pi = ",pi,"  +/-  ",err)
#print("  ║")
#print("  ║                ","o, dicho de otra manera, el valor de pi se encuentra entre")
#print("  ║                       ",pi+err,"   y   ",pi-err)
#print("  ╚════════════════════════════════════════════════════════════════════════════════════════╝")
