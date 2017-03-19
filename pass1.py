#PASS-1 of the SIC-XE assemler. Takes the whole program as input and assigns adress to each line and assigns machine code to all OPCODEs in the program
#Uses OPTAB for fetching machine code of the opcode and length and type of the opcode.
#Uses SYMTAB for storing symbols and their addresses, values and length.
#Writes the intermediate file. 

import re
import pass2
#Global Declaration.
SYMTAB={}
OPTAB={'AD':'18','ADDF':'58','ADDR':'90','AND':'40','CLEAR':'B4','COMP':'28','COMPF':'88','COMPR':'A0','DIV':'24','DIVF':'64','DIVR':'9C','FIX':'C4','FLOAT':'C0','HIO':'F4','J':'3C','JEQ':'30','JGT':'34','JLT':'38','JSUB':'48','LDA':'00','LDB':'68','LDCH':'50','LDF':'70','LDL':'08','LDS':'6C','LDT':'74','LDX':'04','LPS':'D0','MULF':'60','MULR':'98','NORM':'C8','OR':'44','RD':'D8','RMO':'AC','RSUB':'4C','SHIFTL':'A4','SHIFTR':'A8','SIO':'F0','SSK':'EC','STA':'0C','STB':'78','STCH':'54','STF':'80','STI':'D4','STL':'14','STS':'7C','STSW':'E8','STT':'84','STX':'10','SUB':'1C','SUBF':'5C','SUBR':'94','SVC':'B0','TD':'E0','TIO':'F8','TIX':'2C','TIXR':'B8','WD':'DC'}
LOCTR=0
prog=[]

#The 'checkSYMTAB()' function. checks if a symbol is present in the Global SYMTAB.
#If already present returns error. else inserts symbol and its address to SYMTAB.

def checkSYMTAB(symbol,opcode,operator):
	global LOCTR
	global SYMTAB
	#Check if the symbol is already present in SYMTAB. If present duplicate symbol error.
	if symbol in SYMTAB:
		return 1
	else:
		val=[]
		length=-1
		if opcode=='RESW':
			#Get the value and length to store in SYMTAB.
			try:length=3*int(operator)
			except:return 2
			val.append('')

		elif opcode=='RESB':
			#get the value and length to store in SYMTAB.
			try:length=int(operator)
			except:return 2
			val.append('')

		elif opcode=='WORD':
			#Get the value and length to store in SYMTAB.
			values=operator.split(',')
			length=3*len(values)
			for values in values:
				val.append(values)
			#Yet to check for right syntax (num,num,num)
	
		elif opcode=='BYTE':
			#Get the value and length to store in SYMTAB.
			values=operator.split(',')
			length=len(values)
			for values in values:
				val.append(value)
			#Yet to check for right syntax (num,num,num)

	
		
		#Insert (symbol,LOCTR,values,length) into SYMTAB.
		SYMTAB[symbol]=hex(LOCTR)[2:]

		return length+10

#THE checkOPTAB() function. Checks whether an opcode is valid or invalid. Returs machine_code and length of the insruction if opcoe is valid.
def checkOPCODE(opcode,operand):
	global OPTAB
	a=[0,0,'',0]
	#If opcode is not in OPTAB it's an invalid ocpode.
	if opcode.strip('+') not in OPTAB:
		a[0]=1
	else:
		a[2]=OPTAB[opcode.strip('+')]
		if '+' in opcode:	#10 is added to avoid confusin between length and error(1)
			a[1]=4+10
			a[3]=4		#type 4
		elif len(operand)==0:
			a[1]=1+10
			a[3]=1		#type 1
		elif operand.split(',')[0] in 'BSTFAXL':
			a[1]=2+10
			a[3]=2		#typ2
		else:
			a[1]=3+10	
			a[3]=3		#type 3
	return a


#Strucure of the pass-1 of the assembler. Goes through the program line by line, assigning addresses and putting symbols into SYMYAB.
def pass1(program):
	f1=open('intermediate','w')
	global LOCTR
	global prog
	st_ads=0
	lineno=1
	opflag=[0,0,'',0]
	for line in program:
		mccode=''
		length=0
		ins=re.split('[ 	\n]',line)
		if ins[1]=='START':
			try:st_ads=int(ins[2].strip('H'))
			except:print('Syntax error at line no-'+str(lineno))
			LOCTR=st_ads
		elif ins[1]!='END' and ins[1]!='BASE':
			#If label field is not empty,check in SYMTAB.
			if ins[0]!='':
				symflag=checkSYMTAB(ins[0],ins[1],ins[2])
				if symflag==1:
					#DIspaly error(Duplicate symbol)
					print("Error:Duplicate Symbol-"+ins[0])
					continue
				elif symflag==2:
					#display error(Invalid Operand)
					print("Invalid Operand-"+ins[2])
					continue
				else:
					length=symflag-10

			#Check for OPCODE.
			opflag=checkOPCODE(ins[1],ins[2])
			if opflag[0]==1:
			#Check for RESW, RESB, WORD or byte. 
				if ins[1]=='RESW' or ins[1]=='RESB' or ins[1]=='WORD' or ins[1]=='BYTE':
					kfkjfkdh=0
					#Do nothing. It would've been handled by 'checkSYMTAB()'.
				else:
					#Display error mesage(Invalid OPCODE).
					print("Error:Invalid OPCODE-"+ins[1])
			else:
				length=opflag[1]-10
				mccode=opflag[2]
				#Write the intermediate file.
		f1.write(str(hex(LOCTR)[2:])+'\t'+ins[0]+'\t'+ins[1]+'\t'+ins[2]+'\t'+str(mccode)+'\t'+str(length)+'\n')
		prog.append([str(hex(LOCTR))[2:],ins[0],ins[1],ins[2],mccode,opflag[3]])
		#(Format:address label opcode oprerands machinecode_of_OPCODE length). and store the same thing in something for PASS-2.
		LOCTR+=length
		lineno+=1


def main():
	f=open('pgm','r')
	pass1(f)
	global SYMTAB
	f2=open('symtab','w')
	print SYMTAB
	print prog
	pass2.pass2(prog,SYMTAB)
	for key in SYMTAB:
		f2.write(key+'\t'+str(SYMTAB[key])+'\n')

main()
