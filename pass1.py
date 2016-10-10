#PASS-1 of the SIC-XE assemler. Takes the whole program as input and assigns adress to each line and assigns machine code to all OPCODEs in the program.
#Uses OPTAB for fetching machine code of the opcode and length and type of the opcode.
#Uses SYMTAB for storing symbols and their addresses, values and length.
#Writes the intermediate file. Also stores the information required for PASS-2 in a variable.

import re

def pass1(program):
	lineno=1
	for line in program:
		ins=re.split('[ 	\n]',line)
		#If label field is not empty,check in SYMTAB.
		if ins[0]!='':
			symflag=checkSYMTAB(ins[0],ins[1])
		if symflag==False:
			#DIspaly error(Duplicate symbol)

		#Check for OPCODE.
		opflag=checkOPCODE(ins[1])
		if opflag==False:
		#Check for RESW, RESB, WORD or byte. 
			if ins[1]=='RESW' or ins[1]=='RESB' or ins[1]=='WORD' or ins[1]=='BYTE':
				#Do nothing. It would've been handled by 'checkSYMTAB()'.
			else:
				#Display error mesage(Invalid OPCODE). 
		else:
			#Write the intermediate file. 
			#(Format:lineno address label opcode oprerands machnecode_of_OPCODE format length). and store the same thing in something for PASS-2.

