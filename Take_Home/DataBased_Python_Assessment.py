# Hello World! Thanks for exploring the opportunity to join us at DataBased.
# We wish you the best with the assessment.
# Please complete and come prepared to present your solutions to the team.

# Instructions: Solve the problems listed below.
# There are more details about the problems in the provided README, we highly
# recommend reading through the README before solving the problems.

# In order to run the program install Python if not already installed.
# Then change your current directory to the same as the file
# Run the command `python DataBased_Python_Assessment.py` or `python3 DataBased_Python_Assessment.py`
# If you see 'PASSED' that means you passed the all test cases in the test function,
# it does not mean your solution is 100% correct. There may be edge cases you
# should add tests for on your own!

# PROBLEM 1 - Least Factorial
# Given an integer n, find the minimal k such that
# k = m! (where m! = 1 * 2 * ... * m) for some integer m; k ≥n. In other
# words, find the smallest factorial which is not less than n.

from math import ceil
from math import floor
from tkinter.ttk import LabeledScale
from tracemalloc import start
from webbrowser import get

from numpy import number


def leastFactorial(n):

	# running factorial value
	value = 1

	# factor of current iteration of factorial loop
	factor = 1

	# find factorial value until that value is above n
	while(value < n):
		# next factorial value
		value *= factor
		
		# increase factor for next factorial value
		factor += 1
	
	return value

def testLeastFactorial():
	print('-' * 20)
	print('Part 1: Least Factorial')

	assert leastFactorial(17) == 24
	assert leastFactorial(5) == 6
	assert leastFactorial(1) == 1
	assert leastFactorial(0) == 1
	assert leastFactorial(3628799) == 3628800

	print('PASSED PROBLEM 1!')

# PROBLEM 2 - Reclying Lipstick
# You own a lipstick business. When a lipstick container is empty, there is actu-
# ally some leftover lipstick at the bottom that cannot be used because it is not
# accessible. Being an environmentally friendly business owner, you would like to
# recycle the leftover lipstick to make more. As a business, you know you need
# ‘numberOfLeftoversNeeded‘ to make a new lipstick. You have ‘numberOfLip-
# sticks‘ in your possession. What’s the total number of lipsticks you can sell
# assuming that each of your customers return their leftovers

def getTotalNumberOfLipsticks(numberOfLipsticks, numberOfLeftoversNeeded):

	#current number of leftover lipstick
	leftOver = numberOfLipsticks
	#running sum of lipsticks sold
	sold = numberOfLipsticks

	#while there are at least the amount of needed lipstick
	while(leftOver >= numberOfLeftoversNeeded):
		temp = leftOver

		# add to sold the number of new lipsticks you can make and sell
		sold += floor(leftOver / numberOfLeftoversNeeded)
		
		# subtract from leftOver, the number of leftOver lipsticks used to make new lipsticks
		leftOver -= (numberOfLeftoversNeeded * floor(leftOver / numberOfLeftoversNeeded))

		# add to leftOver, the number of new lipsticks sold this time
		leftOver += floor(temp / numberOfLeftoversNeeded)
	
	return sold

def testLipsticks():
	print('\n'+ '-' * 20)
	print('Part 2: Lipsticks')
	assert getTotalNumberOfLipsticks(5, 2) == 9
	assert getTotalNumberOfLipsticks(15, 5) == 18
	assert getTotalNumberOfLipsticks(2, 3) == 2
	assert getTotalNumberOfLipsticks(0, 10) == 0
	assert getTotalNumberOfLipsticks(1, 2) == 1
	assert getTotalNumberOfLipsticks(20, 40) == 20

	print('PASSED PROBLEM 2!')

# PROBLEM 3 - Students and Treats
# A school teacher wants to hand out treats to his students. The teacher de-
# cides the best way to divide the treats is to have the students sit in a circle of
# sequentially numbered chairs. A chair number will be drawn from a hat. Begin-
# ning with the student in drawn chair, one treat will be handed to each student
# sequentially going around the circle until all treats have been distributed.
# The teacher wants to have the students involved in sharing treats. He decides
# that whoever gets the very last treat, will be the student who makes the treats
# for the next game. Determine the chair number occupied by the student who
# will receive the last treat.

# For example, there are 4 students and 6 treats. The students arrange them-
# selves in seats numbered 1 to 4. Let’s suppose 2 is drawn from the hat. Students
# receive treats at positions 2,3,4,1,2,3. The student who gets the last treat is in
# chair number 3

def getLastStudent(numberOfStudents, treats, startingChair):

	# if the number of treats is exactly one more than number of students
	if(numberOfStudents == treats - 1):
		return startingChair
	# if the number of treats is less than number of students
	if(treats < numberOfStudents):
		# do numberOfstudents mod treats to find number of chairs after starting chair,
		# add starting chair after for offset 
		return (numberOfStudents % treats + startingChair)
	else:
		# do all complete rotations of students to get leftover treats
		# add starting chair for offset
		return treats % numberOfStudents + startingChair - 1

def testLastStudent():
		print('\n'+ '-' * 20)
		print('Part 3: Students and Treats')
		assert getLastStudent(5,2,1) == 2
		assert getLastStudent(5,2,2) == 3
		assert getLastStudent(7,19,2) == 6
		assert getLastStudent(3,7,3) == 3
		assert getLastStudent(1, 2, 1) == 1
		assert getLastStudent(2, 3, 2) == 2 
		assert getLastStudent(2, 3, 1) == 1

		print('PASSED PROBLEM 3!')

def getPairsOfShoes(listOfShoes):
	# init empty list of every type of shoe and their count
	counts = {}

	for shoe in listOfShoes:
		
		# if type of shoe already know, add to running sum
		if shoe in counts:
			counts[shoe] += 1
		# else add a new type of show with count of 1
		else:
			counts[shoe] = 1
	
	# init count of pairs
	count = 0

	# for each type of show, find the number of pairs you can do
	# and add to running sum
	for shoe in counts:
		count += (counts[shoe] - (counts[shoe] % 2)) / 2
	return count

# PROBLEM 4 - Pairs of Shoes
# Given an array of strings that represent a type of shoe, return how many matching
# pairs of shoes can be made?

def testPairsOfShoes():
	print('\n'+ '-' * 20)
	print('Part 4: Pairs of Shoes')
	assert getPairsOfShoes(["red", "blue", "red", "green", "green", "red"]) == 2
	assert getPairsOfShoes(["green", "blue", "blue", "blue", "blue", "blue", "green"]) == 3
	assert getPairsOfShoes(["red","red", "red", "red", "red", "blue", "green", "blue"]) == 3

	print('PASSED PROBLEM 4!')
	print('\n\nCongratulations!!')

# Call test functions
testLeastFactorial()
testLipsticks()
testLastStudent()
testPairsOfShoes()
