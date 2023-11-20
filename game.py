__author__ = 'xuanzee'

#Aspects to improve:
#showing Chinese in each system/terminal?
#auto set picture frame and command line window location
#auto compile a list of animal names
#then auto search size and res suitable and royalty free pictures of it (though need to keep local?)
#graphic user interface setup; bubbly font.
#default a terminal opening folder?
#set up easier push and pull sync update, between a certain local and the remote hub?
#hide the list of words part?, or in a different script
#set up a testing code, e.g. check each step's different command and scenario.
#put things in a different script and read-in?
#scripts in different folder
#a list of steps to complete
#major release log add in MD~~
#not constant prompting!

from matplotlib import pyplot as plt
from matplotlib import image as mpimg

print('\nHi, Forrest!') #remove for public version.
print('Let\'s type a word and see its picture!')
print('(Hint: Try an animal or a transportation tool.)')


#personal list; remove for the public version
l0 = ['baba', 'forrest', 'mama', 'nainai', 'waigong', 'waipo', 'yeye', 'yongchen']

#animal list, covering all letters except u and x; may separate into more detailed separations.
l1 = ['ant', 'bat', 'bear', 'beaver', 'bee', 'bird', 'cat', 'cow', 'cheetah', 'dog', 'duck', 
			'eagle', 'elephant', 
			'fox', 'frog',
			'giraffe', 'gorilla', 'hamster', 'hippo', 'horse', 'hyena', 'iguana', 'jellyfish', 
			'kangaroo',
			 'koala', 
			'lion', 'monkey', 'mouse', 'newt', 'octopus', 'owl', 'panda', 'peacock',
			'pig', 'penguin', 'quail', 'rabbit', 'shark', 'sloth', 'snail', 'snake', 
			'spider', 
			'tiger', 'turkey', 'turtle', 'vulture', 'woodpecker', 'yak', 'zebra']

#nature
l2 = ['tree']

#food
l3 = ['apple', 'banana', 'cake', 'orange', 'pear']

#transportation
l4 = ['bike', 'boat', 'bus', 'car', 'taxi', 'train', 'plane']

#others
l5 = ['kite','ring']

#add all words together; to edit the l0 portion out for public version
word_list = l0 + l1 + l2 + l3 + l4 + l5

prompt = 1
while prompt ==	1:
	check_play = input('\nKeep playing? (y/n) ')
	if check_play == 'y':
		word = input('OK. Try spell a word! ')
		word = word.lower()
		if word in word_list:
			image_str = word + '.jpeg'
			image = mpimg.imread(image_str)
			plt.close()
			plt.figure()
			plt.imshow(image)
			plt.axis('off')
			plt.show(block=False)
		else:
			print('I don\'t have the word \"' + word + '\" yet. Sorry!')
	elif check_play == 'n':
		prompt = 0
		print('OK. Bye!')
	else:
		print('Please enter either "y" or "n".')