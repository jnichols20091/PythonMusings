import random

suit_tuple = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
rank_tuple = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

ncards = 8

def getcards(deckListIn):
	thisCard = deckListIn.pop()
	return thisCard

def shuffle(deckListIn):
	deckListOut = deckListIn.copy()
	random.shuffle(deckListOut)
	return deckListOut

print('Welcome to Higher or Lower.')
print('You have to chose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start')
print()

startingDeckList = []
for suit in suit_tuple:
	for thisValue, rank in enumerate(rank_tuple):
		cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
		startingDeckList.append(cardDict)

score = 50

while True:
	print()
	gameDeckList = shuffle(startingDeckList)
	currentCardDict = getcards(gameDeckList)
	currentCardRank = currentCardDict['rank']
	currentCardValue = currentCardDict['value']
	currentCardSuit = currentCardDict['suit']
	print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
	print()

	for cardNumber in range(0, ncards):
		answer = input('Will the next card be higher or lower than the ' + currentCardRank + ' of ' + currentCardSuit + '? (enter h or l):')
		answer = answer.casefold() # force lowercase
		nextCardDict = getcards(gameDeckList)
		nextCardRank = nextCardDict['rank']
		nextCardSuit = nextCardDict['suit']
		nextCardValue = nextCardDict['value']
		print('Next card is:', nextCardRank + ' of ' +nextCardSuit)
		if answer == 'h':
			if nextCardValue > currentCardValue:
				print('You got it right, it was higher')
				score = score + 20
			else:
				print('Sorry, it was not higher')
				score = score - 15 
		elif answer == 'l':
			if nextCardValue < currentCardValue:
				score = score + 20
				print('You got it right, it was lower')
			else:
				score = score - 15
				print('Sorry, it was not lower')
			print('Your score is:', score)
			print()
			currentCardRank = nextCardRank
			currentCardValue = nextCardValue
	goAgain = input('To play again, press ENTER, or "q" to quit: ')
	if goAgain == 'q':
		break
	print('OK bye')