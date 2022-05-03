#An encryptor which should encode the letters of a message to 10 letters ahead from it.
#Essentially a rot10 encrypter 

d = {} #a dictionary to assign each character a different value

for smallCaps in (65,97): #loop a tuple for caps and small letters because ascii of A starts from 65 and a starts from 97 	 
	for char in range(26): #loop from 0 to 25 to because 26 letters
		d[chr((char+10)%26 + smallCaps)] = chr(char + smallCaps) #using chr to get the ascii corresponding value and then assigning it to a different letter in our dictionary

s = input("Enter your message: ")

print(''.join([d.get(char,char) for char in s])) #using join() to join the sequence from the dictionary.
						#here we iterate char over the input for each 
						#letter and then use the dictionary to print
						#the corresponding value to the key	

