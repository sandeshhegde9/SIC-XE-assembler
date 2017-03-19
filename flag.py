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
