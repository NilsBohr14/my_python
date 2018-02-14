
# Using loop

def palin2(word):
	x = ''
	for element in range(len(word)):
		x += word[len(word)-1-element]
		return x
	
word = raw_input("Enete your text")

x = palin2(word)

if x == word:
	print "this is palindrome"
else:
	print "no, it is not"
	
	













# Using indexing
def palin1():
	user_palin = raw_input("\nplease write a text and see magic: ")
	
	print "\nYour input: ", user_palin
	
	print "\n\nIs your input palindrome ??? \nmirror of you text: ", user_palin[::-1]
	
	print "\nso, your text palindrome ???"
	
	if user_palin[::-1] == user_palin: 
		print "\nYes it is, see: %r = %r" %(user_palin[::-1], user_palin)
		print"\nThe text: %r is palindrome"%user_palin
	else:
		print "\nNope, you are not very much intelligent: %r != %r " %(user_palin[::-1], user_palin)
		print"\nThe text: %r is not palindrome"%user_palin
	
	

	
palin1()
	
	