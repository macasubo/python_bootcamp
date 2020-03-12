import sys
import string


def text_analyzer(*text):

	'''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'''
	char = 0
	upper = 0
	lower = 0
	punct = 0
	space = 0
	if len(text) > 1:
		print("ERROR")
	else:
		if len(text) == 0 or len(text[0]) == 0:
			text = (input("What is the text to analyse?\n>> "), "")
		for cur in text[0]:
			char += 1
			if cur.isupper():
				upper += 1
			if cur.islower():
				lower += 1
			if cur in string.punctuation:
				punct += 1
			if cur == ' ':
				space += 1
		print("The text contains " + str(char) + " characters:\n")
		print("- " + str(upper) + " upper letters\n")
		print("- " + str(lower) + " lower letters\n")
		print("- " + str(punct) + " punctuation marks\n")
		print("- " + str(space) + " spaces")
