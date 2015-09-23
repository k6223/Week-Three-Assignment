# name = "Kollin"
#CIS-125-82A
#PIGLATIN.py
#
#Converts English Words to simple Pig Latin

#Write program code here

vowels = "aeiouAEIOU"
word = input("enter an English word to translate: ")

if word[0] in vowels :
	print (word + "yay")
else :
	print (word[1:] + word[0] + "ay")
		
#Input- yello, hello, awesome, scratch

#Process

#Output- elloyay, elloyay, awesomeyay, cratchsay
