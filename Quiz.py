print("Welcome to Quiz 2018")
def quizzard(q1,q2,a1,a2):
	start=input("Wanna begin?(Y/N)")
	c=2
	if start=='Y':
		print("Lets Begin now")
		while c:	
			print(q1)
			answer=input("What do you think: ")
			if answer==a1:
				print("Good job you are qualified for next round\n")
			else:
				print("You got it wrong.\nThank you for participating")
				break
	
			print(q2)
			answer=input("What do you think: ")
			if answer==a2:
				print("Great job you are qualified for next round\n")
			else:
				print("You got it wrong.\nThank you for participating")
				break
	else:
		print("Bye")
def participant():
	q1=("1.How many agreements are signed between India and Uganda?\nA.6\nB.4\nC.5\nD.8")
	a1='B'
	q2=("Which country has become a popular hub of medical tourism?\nA.Mexico\nB.India\nC.Malaysia\nD.Brazil")
	a2='B'
	quizzard(q1,q2,a1,a2)
def master():
	q1=input("Enter your Question: ")
	a1=input("Required answer: ")
	q2=input("Enter your Question: ")
	a2=input("Required answer: ")
	quizzard(q1,q2,a1,a2)
check=input("Are you the master(M) or the participant(P)")
if check=='M':
	password=input('Enter password')
	if password=='12345':
		master()
else:
	participant()


