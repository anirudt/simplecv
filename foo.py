import math
def bin(num, bit):
	i = 1
	s1 = []
	a = ""
	while(i<=bit):
		s1.append("0")
		i = i + 1
	k = num
	rem = 0
	print("Initial form")
	if k==0:
		return "".join(s1)
	i = 0
	while(num>0):
		rem = num%2
		num = num/2
		s1[i] = str(rem)
		i = i + 1

	
	return ("".join(s1))[::-1]	


#def start(minterm, minterm_number, dontcare, dontcare_number, n):
#	i = 1
#	j = 1
#	while(i<=minterm_number):





def main():
	print("Specify the number of variables in the map")
	n = input()
	minterms = []
	dontcare = []
	minterm = []
	i = 1
	k = 0 
	bit = 0
	print("Enter number of minterms")
	minterm_number = input()
	print("Enter number of don't care")
	dontcare_number = input()
	while(i<=minterm_number):
		k = input()
		if k>bit:
			bit = k
		minterms.append(k)
		i=i+1
	bit = int(math.log(bit*1.0,2)+1)
	print("No. of bits")
	print(bit)
	i = 0
	while(i<minterm_number):
		minterm.append(bin(minterms[i], bit))
		
		i = i + 1
#	print(minterm)
	i = 0
	while(i<=dontcare_number):
		k = input()
		dontcare.append(bin(k,bit))
		i=i+1
	i = 1
#	print(dontcare) 	
    
    

	
		