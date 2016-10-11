#The 'checkSYMTAB()' function. checks if a symbol i spresent in the Global SYMTAB.
#If already present returns error. else inserts symbol and its address to SYMTAB.


def checkSYMTAB(symbol,opcode,operator):
	#Check if the symbol i salready present in SYMTAB. If present duplicate symbol error.
	if symbol in SYMTAB:
		return 1
	val=[]
	else:
		if opcode='RESW':
			#Get the value and length to store in SYMTAB.
			l=operator.split('#')
			try:length=3*(int)l[1]
			except:return 2
			val[0]=''

		elif opcode=='RESB':
			#get the value and length to store in SYMTAB.
			l=operator.split('#')
			try:length=(int)l[1]
			except:return 2
			val[0]=''

		elif opcode=='WORD':
			#Get the value and length to store in SYMTAB.
			values=operator.split(',')
			length=3*len(values)
			for values in values:
				val.append(value)
			#Yet to check for right syntax (num,num,num)
	
		elif opcode=='BYTE':
			#Get the value and length to store in SYMTAB.
			values=operator.split(',')
			length=len(values)
			for values in values:
				val.append(value)
			#Yet to check for right syntax (num,num,num)

	
		
		#Insert (symbol,LOCTR,values,length) into SYMTAB.
		SYMTAB[symbol]=(symbol,LOCTR,val,length)

		#Increment LOCTR by length.
		LOCTR+=length
		return 0
