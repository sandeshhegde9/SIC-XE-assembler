#The 'checkSYMTAB()' function. checks if a symbol i spresent in the Global SYMTAB.
#If already present returns error. else inserts symbol and its address to SYMTAB.


def checkSYMTAB(symbol,opcode):
	#Check if the symbol i salready present in SYMTAB. If present duplicate symbol error.
	if symbol in SYMTAB:
		return False
	else:
		if opcode='RESW':
			#Get the value and length to store in SYMTAB.
			#increment LOCTR accordingly.
		elif opcode=='RESB':
			#get the value and length to store in SYMTAB.
			#increment LOCTR accordingly.
		elif opcode=='WORD':
			#Get the value and length to store in SYMTAB.
			#increment LOCTR accordingly.
		elif opcode=='BYTE':
			#Get the value and length to store in SYMTAB.
			#increment LOCTR accordingly.
		
		#Insert (symbol,LOCTR,values,length) into SYMTAB.

		#Increment LOCTR by length.

