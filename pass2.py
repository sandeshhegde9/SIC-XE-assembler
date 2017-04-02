#Pass-2 of the SIC-XE assebbler. Takes the intermediate format and SYMTAB as input and writes the object file.

#This functions decides all the flags for an instruction. Takes a line of code as input returns a sring 'nixbpe'
def getFlag(line,disp):
	n=i=x=b=p=e=0
	#If '#' in operands then it's intermediate addressing.
	if '#' in line[3]:
		i=1
	#if '@' in operands then it's indirect addressing.
	elif '@' in line[3]:
		n=1
	#For type-3 'n' and 'i' both are 1.
	elif line[5]==3:
		n=i=1
	#For indexed addressing.
	if ',X' in line[3]:
		x=1
	#Decide whether base relative or PC relative.
	if disp=='p':
		p=1
	elif disp=='b':
		b=1
	#For type-4 e=1.
	if line[5]==4:
		e=1
	flag=str(n)+str(i)+str(x)+str(b)+str(p)+str(e)
	return flag
	
#Pass-2 method..!s	
def pass2(prog,SYMTAB):
	sym={'B':01,'S':02,'T':03,'F':04,'A':05,'X':05,'L':06}
	for i in range(len(prog)):

		#If the instruction has a machine code convert to 6 bit binary.
		if prog[i][4]!='':
			bin_str= bin(int(prog[i][4],16))[2:].zfill(len(prog[i][4]*4))[:6]
			print bin_str

	
		#Check instuction type and get the required target address correspondingly.
		'''elif len(operand)==0:
                        a[1]=1+10
                        a[3]=1          #type 1
                elif operand.split(',')[0] in 'BSTFAXL':
                        a[1]=2+10
                        a[3]=2          #typ2
                else:
                        a[1]=3+10
                        a[3]=3          #type 3'''
		
		b=''
		if prog[i][-1]==4:
		#For type four 20 bit address.

		#Flag needs to be checked and flag needs to be aded to bin_string..
			flags=getFlag(prog[i],'p')
			bin_str+=flags
			print bin_str


			if '#' in prog[i][3]:
			#Immediate addressing.
				operand=prog[i][3].strip('#')
				b=bin((int(operand,16)))[2:].zfill(20)

			elif '@' in prog[i][3]:
			#Indirect addressing.
				operand=prog[i][3].strip('@')
				b=(bin(int(SYMTAB[operand],16)))[2:].zfill(20)
				

			else:
			#Normal addressing..
				operand=prog[i][3]
				b=bin(int((operand,16)))[2:].zfill(20)
		
		#TYPE 3
		disp=0
		if prog[i][-1]==3:
		#Type 3. Need to calculate Displacement. -_-
		#Flag needs to be checked and flag needs to be aded to bin_string..
			flags=getFlag(prog[i],'p')
			bin_str+=flags
			print bin_str

			if '#' in prog[i][3]:
			#Immediate addressing.
				operand=prog[i][3].strip('#')
				disp=int(operand,16)

			elif '@' in prog[i][3]:
			#Indirect addressing.
				operand=prog[i][3].strip('@')
				if i<len(prog)-1:
					disp=int(SYMTAB[operand],16)-int(prog[i+1][0],16)
				else:
					disp=int(SYMTAB[operand],16)-int(prog[i][0],16)
				

			else:
			#Normal addressing.
				if i<len(prog):
					disp=int(SYMTAB[prog[i][3]],16)-int(prog[i+1][0],16)
				else:
					disp=int(SYMTAB[prog[i][3]],16)-int(prog[i][0],16)

			#RANGE OF DISP NEEDS TO BE CHECKED HERE.
			#AND DEPENDING ON THE RANGE FLAG P/B has to be set..
			#DO IT LATER -_-
			#CRAP


			#Convert disp to binary and add to bin_srting..
			if disp>0:
				disp=bin(disp)[2:].zfill(12)
			else:
				disp='blah'
				#HANDLE HERE> Have to get 2's complement..!
			bin_str+=disp
			print bin_str

			#TYPE 2
			if prog[i][-1]==2:
				#Type 2. Get code for registers. 8 bit opcode and 8 bit register code.
				reg=prog[i][3].split(',')
				reg_code1=sym[reg[0]]
				reg_code2=sym[reg[1]]
				bin_str=bin(int(prog[i][4],16))[2:].zfill(len(prog[i][4]*4))[:8]
				bin_str+=bin(reg_code1)[2:].zfill(4)+bin(reg_code2)[2:].zfill(4)
				print bin_str
				#DONE  B-).. i mean type 2.. -_-

			if prog[i][-1]==1 and prog[i][2]!='BASE':
				bin_str=bin(int(prog[i][4],16))[2:].zfill(8)
				print bin_str



		#NOW HANDLE VARIABLE DECLERATION and blah blah.....
		if prog[i][2] in ['BYTE','WORD','RESW','RESB']:
			#Variable Decleration or array..
			if prog[i][2]=='WORD':
				dat=prog[i][3].split(',')
				bin_str=''
				for j in range(len(dat)):
					dat[j]=int(dat[j],16)
					bin_str+=bin(dat[j])[2:].zfill(24)+'^'
			if prog[i][2]=='BYTE':
				dat=prog[i][3].split(',')
				bin_str=''
				for j in range(len(dat)):
					dat[j]=int(dat[j],16)
					bin_str+=bin(dat[j])[2:].zfill(8)+'^'

			if prog[i][2]=='RESW':
				bin_str=''
				jh=int(prog[i][3])
				for d in range(jh*24):
					bin_str+=' '
					if d%24==0 and d!=0:
						bin_str+='^'

			if prog[i][2]=='RESB':
				bin_str=''
				jh=int(prog[i][3])
				for d in range(jh*8):
					bin_str+=' '
					if d%8==0 and d!=0:
						bin_str+='^'

			print bin_str
