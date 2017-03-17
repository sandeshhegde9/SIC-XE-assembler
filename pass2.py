#Pass-2 of the SIC-XE assebbler. Takes the intermediate format and SYMTAB as input and writes the object file.

def pass2(prog,SYMTAB):
	for i in range(len(prog)):

		#If the instruction has a machine code convert to 6 bit binary.
		if prog[i][4]!='':
			bin_str= bin(int(prog[i][4],16))[2:].zfill(len(prog[i][4]*4))[:6]
			print bin_st

		#Flag needs to be checked and flag needs to be aded to binstring..
		#I have this code in my laptop.. Just have to copy paste.
		#

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
		if prog[i][-1]=='4':
		#For type four 20 bit address.

			if '#' in prog[i][3]:
			#Immediate addressing.
				operand=prog[i][3].strpi('#')
				b=bin((int(operand,16))[2:].zfill(20)

		if prog[i][-1]=='3':
		#Type 3. Need to calculate Displacement. -_-

