#INGEST INPUT
input_file = open('input.txt', 'r')
Lines = input_file.readlines()

#SET VARIABLES
off=0
on=0
offy=0
ony=0
x=0
xlist=[]
ylist=[]

#Process FILE


for i in range (12):
	off=0
	on=0
	line=0
	for line in Lines:
		move=line.strip()
		#BINARY COUNTER
		if move[x]=="0":
			off += 1
		if move[x]=="1":
			on += 1
	#SETTING PRIMARY BIT
	if off>on:
		bit=0
		x+=1
		xlist.append(bit)
	else:
		bit=1
		x+=1
		xlist.append(bit)

print(xlist)

#REMOVE COMMAS AND JOIN ITEMS AS A LIST
x1=''.join(str(xlist).split(','))

x2=''
x3=(x2.join(x1)).strip('[]').strip()

def remove(string):
	return string.replace(" ","")

string = x3
x4= (remove(string))
print (x4)
x5=int(x4,2)
print ('Xvalue is equal to:{}'.format(x5))

#SECOND PORTION
bity=0
x=0
input_file = open('input.txt', 'r')
Lines = input_file.readlines()
for i in range (12):
	offy=0
	ony=0
	line=0
	for line in Lines:
		move=line.strip()
		#BINARY COUNTER
		if move[x]=="0":
			ony += 1
		if move[x]=="1":
			offy += 1
	#SETTING PRIMARY BIT
	if offy>ony:
		bity=0
		x+=1
		ylist.append(bity)
	else:
		bity=1
		x+=1
		ylist.append(bity)
print (ylist)

#REMOVE COMMAS AND JOIN ITEMS AS A LIST
y1=''.join(str(ylist).split(','))

y2=''
y3=(y2.join(y1)).strip('[]').strip()

def remove(string):
	return string.replace(" ","")

string = y3
y4= (remove(string))
print (y4)
y5=int(y4,2)
print ('Yvalue is equal to:{}'.format(y5))

print ('FINALvalue is equal to:{}'.format(y5*x5))

#y3.replace(" ","")
#print (y3)

#print (ylist[0])
#if ylist(x)=1:


#2 4 8 16 32 64 128 192 256 512 1024 2048 4096









print("off:{}, on:{} ".format(off,on))
#print("bit{}".format(bit))
#print("off2:{}, on2:{} ".format(off2,on2))
#print("2nd_bit{}".format(bit2))




