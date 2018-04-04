import random
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)
	

def insanity():
	i = 0
	insanity_metric = int(input('Enter a positive integral insanity metric:\t'))
	#
	txt1 = 	"Imagine that...\nYou just had a conversation with your friends. You would like to "
	txt1 += "graph this conversation, perhaps in terms of the topics touched, "
	txt1 += "intersection of ideas, and jumps from topic to topic.\n"
	txt1 += "Unfortunately for your sanity, this graph is something you can have a "
	txt1 += "conversation about...\n\nBrace yourself...\n"
	delay_print(txt1)
	#
	#
	verbwords = ['plotting', 'having']
	nounwords = ['graph', 'conversation']
	#
	mindbender = ''
	#
	for i in range(insanity_metric):
		if i == 0:
			mindbender = "Imagine {} the {} {}...".format(verbwords[i%2], nounwords[(i+1)%2], nounwords[i%2])
		elif i%2==1:
			mindbender = "Imagine {} the {} {}...".format(verbwords[i%2], mindbender, nounwords[i%2])
		else:
			mindbender = "Imagine {} the {} {}...".format(verbwords[i%2], mindbender, nounwords[i%2])
		print(mindbender)
		mindbender = '\"' + mindbender[:-3] + '\"'
		continue
		a, b, c = random.randint(0, 10**10), random.randint(0, 10**10), random.randint(0, 10**10)
		answer = (a*b)%c
		t1 = time.time()
		check = input('\tPress any key to continue, or enter the result of ({}x{})%{} within 10 seconds to exit\n\t'.format(a, b, c))
		t2 = time.time()
		if check.isnumeric() and int(check) == answer:
			if t2-t1<10:
				#delay_print('\tYou have successfully escaped insanity. Goodbye.')
				return 0
			else:
				#delay_print('\tToo late. Give up. Now...')
		else:
			if len(check) > 1:
				#print('\tResistance is futile. Better embrace insanity than struggle meaninglessly...')
	delay_print("\nYou have successfully lost your mind. But that's alright, you don't need it any more.\n\n")

if __name__=="__main__":
	insanity()
