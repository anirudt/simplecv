import math

#The following function converts a decimal number into a 'bit'long binary number
def bin(num, bit):
	i = 1
	s1 = []
	a = ""
	while(i<=bit):
		s1.append("0")
		i = i + 1
	k = num
	rem = 0
	if k==0:
		return "".join(s1)
	i = 0
	while(num>0):
		rem = num%2
		num = num/2
		s1[i] = str(rem)
		i = i + 1
	return ("".join(s1))[::-1]	

#The following function starts the QM algorithm, and bifurcates the minterms
def start(minterm, minterm_number, dontcare, dontcare_number, n, bit):
	i = 0
	j = 1
	stage1 = []
	for entry in dontcare:
		minterm.append(entry)
	temp = []
	while(i<=bit):
		for entry in minterm:
			if entry.count('1')==i:
				temp.append(entry)
		stage1.append(temp)
		temp = []		
		i = i + 1
	#print("Stage 1 goes like")
	#print(stage1)
	return stage1			

#The following function, checks the form of 2 highly similar functions 
def corelation(s1, s2, bit):
	i = 0
	count = 0
	while(i<bit):
		if s1[i]==s2[i]:
			count = count + 1
		i = i + 1
	if (count == (bit-1)):
		return True
	else:
		return False

#The following function converts into the reduced form
def bind(s1, s2, bit):
	i = 0
	count = 0
	temp = ""
	while(i<bit):
		if s1[i] != s2[i]:
			temp = temp + "x"
		else:
			temp = temp  + s1[i]
		i = i + 1
	return temp		

#The following function removes the redundant bit patterns 
def redundant(stage2, bit):
	for entry in stage2:
		i = 0
		j = 0
		while(i<len(entry)):
			while(j!=i):
				if(entry[i]==entry[j]):
					entry.remove(entry[i])
				
				j = j + 1
			i = i + 1	
	return stage2			
#The following function gets the decimal value of the binary coded number
def dec(s1, bit):
	i = 1
	dec = 0
	while(i<=bit):
		if(s1[i-1]=='1'):
			dec = dec + 2**(bit-i)
		i = i + 1
	return dec		

# The following function expands the required 'x' form into the minterms, for reverse analysis necessary
def simplify(s1,bit):
	i = 0
	listing = []
	count = 0
	doc = []
	
	while(i<bit and (s1.count('x')!=0)):
		if(s1[i]=='x'):
#			print(s1[0:i-1]+"1"+s1[i:])
#			print(s1[0:i-1]+"0"+s1[i:])
			listing.append(simplify(s1[0:i]+"1"+s1[i+1:],bit))
			listing.append(simplify(s1[0:i]+"0"+s1[i+1:],bit))
			
		i = i + 1

	if (s1.count('x')==0):
		listing.append(s1)
#		print(listing)
		return s1

	for entry in listing:
		for subentry in listing:
			doc.append(subentry)
	
	return doc[0:2]
		
		
		

			
def main():
	print("Specify the number of variables in the map")
	n = input()
	minterms = []
	dontcare = []
	minterm = []
	i = 1
	k = 0 
	bit = 0
	stage1 = []
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
	print(minterm)
	i = 0
	while(i<dontcare_number):
		k = input()
		dontcare.append(bin(k,bit))
		i=i+1
	i = 1
	print(dontcare) 
	stage1 = start(minterm, minterm_number, dontcare, dontcare_number, n, bit)	
	i = 0
	j = 1
	c_count = 0
	overall = 0
	stage2 = []
	temp = []
	unlisted = []
	flag = 0
	temp = []
	temp1 = []
	i = 0
	j = 0
	temp = []
	while(flag==0):
		i = 0
		j = 1
		overall = 0
		temp = []
		kad = 0
		subentry_count = 0
		temp1 = []
		while(i<len(stage1)-1):
			temp = []
			c_count = 0
			for entry in stage1[i]:
				
				subentry_count = 0
				for subentry in stage1[j]:
					if corelation(entry,subentry, bit)==True:
						temp.append(bind(entry, subentry, bit))
						temp1.append(entry)
						temp1.append(subentry)
						overall = overall + 1
			kad = 0
			stage2.append(temp)
			j = j + 1
			i = i + 1	
		if overall==0:
			flag = 1
			
			disc = []
			for entry in stage1:
		
				for subentry in entry:
					disc.append(subentry)
			
			#print("disc is")
			#print(disc)
			unlisted = list(set(temp1) - set(disc))
			print("Unlisted Set")
			print(unlisted)
			print("Here we end")
			
			print(redundant(stage1, bit))
		else:
			
			disc = []
			for entry in stage1:
		
				for subentry in entry:
					disc.append(subentry)
			
			#print("disc is")
			#print(disc)
			unlisted = list(set(temp1) - set(disc))
			print("Unlisted Set")
			print(unlisted)
			stage1 = []
			stage1 = stage2
			stage2 = []
			print("Next Stage is")
			
			print(stage1)
	
	print(stage1)
	temp = []
	
	print("unlisted is")
	print(unlisted)	
	jadu2 = list(set(unlisted)-set(disc))
	print("new unlisted is")
	print(jadu2)


	
	prime = []
	prep = []
	for entry in stage1:

		for subentry in entry:
			temp = []
			prep = []
			#print("entry")
			#print(subentry)
			prep = simplify(subentry, bit)
			#print("prep")
			#print(prep)
			for x in prep:
				for y in x:
					temp.append(y)
			prime.append(temp)
	if jadu2:
		prime.append(unlisted)
		
	print(prime)

	i = 0
	j = 0
	prime1 = prime
	while(i<len(prime)):
		print(prime[i])
		j = 0
		while(j<len(prime[i])):
			prime1[i][j] = dec(prime[i][j], bit)
			print(prime1[i][j])
			j = j + 1

		i = i + 1
	print(prime1)	
	i = 0
	j = 0
	k = 0
	count = []
	alpha = []
	stage_alpha = []
	for entry in stage1:
		for subentry in entry:
			stage_alpha.append(subentry)
	#Stage_alpha, is the combination of the final prime implicants (non-redundant)
	print("stage_alpha is")
	print(stage_alpha)	
	dup = stage_alpha	
	flag = 0
	essential = []
	while(flag==0):
		count = []
		alpha = []
		while(i<len(minterms)):
			count.append(0)
			alpha.append(0)
			i = i +1
		i = 0
		print(minterms)
		# Following is the count-alpha computation
		while(i<len(minterms)):
			j =0
			while(j<len(prime1)):
				k = 0
				while(k<len(prime1[j])):
					#print(prime1[j][k])
					#print(minterm[i])
					if(prime1[j][k]==minterms[i]):
						count[i] = count[i] + 1
						alpha[i] = j
					k = k + 1
				j = j + 1
			i = i + 1
		print(count)
		#count is the number of occurences 
		print(alpha)
		#alpha is the index of occurence
		print("prime1")
		#prime1 is the listed set of minterms supplied by every prime implicant
		print(prime1)
		if(count.count(1)==0):
			flag = 1
			break
		i = 0
		
		temp = []
		while(i<len(count)):
			if(count[i]==1):
				
				print(i)
				print("alpha[i]")
				print(alpha[i])
				print(prime1[alpha[i]])
				temp.append(alpha[i])
				count[i] = 0
			

			i = i + 1
		temp1 = list(set(temp))	
		#print("temp")
		#print(temp1)	
		for entry in temp1:
			#print("entry")
			#print(entry)

			essential.append(dup[entry])
			prime1[entry] = -1
			dup[entry] = -1
		i = 0
		while(i<prime1.count(-1)):
			prime1.remove(-1)
			dup.remove(-1)

#		print("new counts")
#		print(count)	
#		print("essential - presenting")
#		print essential		
#		print("prime1")
#		print(prime1)


#	print("end essential")
#	print(essential)

#Do the essential prime implicants part.	
		