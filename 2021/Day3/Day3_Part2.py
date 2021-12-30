import sys
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

print("off:{}, on:{} ".format(off,on))


#DAY3 PART2

#print (xlist[0])
#print (xlist[1])


#SET INPUT FILE VARIABLE

#SET X_POSITION
x=0
#OXYGEN_GENERATOR
with open ('input.txt', 'r') as fin, open('output0.txt', 'w') as fout:
	Lines = fin.readlines()
	for line in Lines:
		move=line.strip()
		if move[x] == "0":
			sys.stdout = fout
			print (move)

#START HERE WITH LOOP!!
x=1
y=0
for i in range (1,12):
	sys.stdout = sys.__stdout__
	with open('output{}.txt'.format(y), 'r') as fin, open('output{}.txt'.format(x), 'w') as fout:
			offxx = 0
			onxx = 0
			Lines = fin.readlines()
			for line in Lines:
				move = line.strip()
				# BINARY COUNTER
				if move[x] == "0":
					offxx += 1
				if move[x] == "1":
					onxx += 1
			print("OXYGENoff:{}, OXYGENon:{} ".format(offxx, onxx))
			if onxx >= offxx:
				bity = 1
				print("OXYGEN SETTING IS ON")
			else:
				bity = 0
				print("OXYGEN SETTING IS OFF")
			with open('output{}.txt'.format(y), 'r') as fin, open('output{}.txt'.format(x), 'w') as fout:
				for line in Lines:
					move=line.strip()
					if bity == 0:
						if move[x]=='0':
							sys.stdout=fout
							print(move)
					else:
						if move[x] == '1':
							sys.stdout=fout
							print(move)
				x+=1
				y+=1

#
sys.stdout = sys.__stdout__
with open('output11.txt'.format(x),'r') as fin3:
	Lines=fin3.readlines()
	for line in Lines:
		move2=line.strip()
		x50 = int(move2, 2)
print('Day3 part2 oxygen value is equal to:{}'.format(x50))
# #CO2_SCRUBBER
x=0
with open ('input.txt', 'r') as fin, open('outputy0.txt', 'w') as fout:
	Lines = fin.readlines()
	for line in Lines:
		move=line.strip()
		if move[x] == "1":
			sys.stdout = fout
			print (move)

#START HERE WITH LOOP!!
x=1
y=0
for i in range (1,12):
	sys.stdout = sys.__stdout__
	with open('outputy{}.txt'.format(y), 'r') as fin, open('outputy{}.txt'.format(x), 'w') as fout:
			offxx = 0
			onxx = 0
			Lines = fin.readlines()
			for line in Lines:
				move = line.strip()
				# BINARY COUNTER
				if move[x] == "0":
					offxx += 1
				if move[x] == "1":
					onxx += 1
			print("CARBONoff:{}, CARBONon:{} ".format(offxx, onxx))
			if offxx <= onxx:
				bity = 0
				print("CARBON SETTING#{} IS OFF".format(x))
			else:
				bity = 1
				print("CARBON SETTING{} IS ON".format(x))
			with open('outputy{}.txt'.format(y), 'r') as fin, open('outputy{}.txt'.format(x), 'w') as fout:
				for line in Lines:
					move=line.strip()
					if bity == 0:
						if move[x]=='0':
							sys.stdout=fout
							print(move)
					else:
						if move[x] == '1':
							sys.stdout=fout
							print(move)
				x+=1
				y+=1
sys.stdout = sys.__stdout__
with open('outputy7.txt'.format(x),'r') as fin3:
	Lines=fin3.readlines()
	for line in Lines:
		move2=line.strip()
		x60 = int(move2, 2)
print('Day3 part2 CARBON value is equal to:{}'.format(x60))
print("Day 3 Part 2 FINAL ANSWER IS {}".format(x50*x60))


