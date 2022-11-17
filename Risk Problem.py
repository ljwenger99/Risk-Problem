# Lucas Wenger
# RISK PROBLEM
    # Find the pmf of X where X is the number of armies lost by the attacker in a single round.
    # Attacker always has 3 dice; defender always has 2. Attacker's top 2 dice go against the defender's 2. Defender wins any ties.
# Probability
# 4/23/2021

'''
----------------------------------------------------------------------------------------ASSIGNMENT 1---------------------------------------------------------------------------------------
'''

'''
CALCULATED PMF:
    |P{X = 0} = 2890/7776
    |P{X = 1} = 2611/7776
    |P{X = 2} = 2275/7776
'''

import random

# FUNCTION TO CALCULATE OUTCOME OF A ROUND
def round(attacker, defender):
    '''calculates outcome given rolls of attacker and defender and increases corresponding pmf value'''
    global pmfzero
    global pmfone
    global pmftwo
    global totalrounds
    attacker = sorted(attacker)
    defender = sorted(defender)
    temptotal = 0
    if defender[0] >= attacker[1]:
        temptotal += 1
    if defender[1] >= attacker[2]:
        temptotal += 1
    if temptotal == 0:
        pmfzero += 1
    elif temptotal == 1:
        pmfone += 1
    elif temptotal == 2:
        pmftwo += 1
    totalrounds += 1

#---------------------------------------------------------------------------------METHOD 1---------------------------------------------------------------------------------
# METHOD 1: Iterate through every possibility, take each value of X over total number of rolls
# roll and store all possible attacker rolls
print("---------------ASSIGNMENT 1---------------")
attackerrolls = []
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            attackerrolls.append((i,j,k))


# roll and store all possible defender rolls
defenderrolls = []
for i in range(1,7):
    for j in range(1,7):
        defenderrolls.append((i,j))

# pmf = 0, 1, 2
pmfzero = 0
pmfone = 0
pmftwo = 0
totalrounds = 0

# Do the testing!
for i in attackerrolls:
    for j in defenderrolls:
        round(i,j)

# Print probabilities
print("""The calculated pmf of X is as follows:
|P{X = 0} = """ + str(pmfzero) + '/' + str(totalrounds) + " = " + str(pmfzero/totalrounds) + """
|P{X = 1} = """ + str(pmfone) + '/' + str(totalrounds) + " = " + str(pmfone/totalrounds) + """
|P{X = 2} = """ + str(pmftwo) + '/' + str(totalrounds) + " = " + str(pmftwo/totalrounds) + "\n")
    
#---------------------------------------------------------------------------------METHOD 2---------------------------------------------------------------------------------
# METHOD 2: Battle a lot!
# pmf = 0, 1, 2
pmfzero = 0
pmfone = 0
pmftwo = 0
totalrounds = 0

# input number of rounds to do
while True:
    try:
        numofrounds = 7776 # Use for custom input -- int(input("How many rounds would you like to do to estimate the pmf? (Note: 7776 would make for an easy comparison with the calculated pmf)\n"))
    except:
        print("Please enter an integer.\n")
        continue
    break

print("Processing...\n")
# set dice randomly, roll a lot!
for z in range(numofrounds): # (7776 would make for an easy comparison with Method 1)
    attacker = (random.randint(1,6), random.randint(1,6), random.randint(1,6))
    defender = (random.randint(1,6), random.randint(1,6))
    round(attacker, defender)
print("""The estimated pmf of X is as follows:
|P{X = 0} = """ + str(pmfzero) + '/' + str(totalrounds) + " = " + str(pmfzero/totalrounds) + """
|P{X = 1} = """ + str(pmfone) + '/' + str(totalrounds) + " = " + str(pmfone/totalrounds) + """
|P{X = 2} = """ + str(pmftwo) + '/' + str(totalrounds) + " = " + str(pmftwo/totalrounds) + "\n")


'''
----------------------------------------------------------------------------------------ASSIGNMENT 2---------------------------------------------------------------------------------------
'''
# If both sides (attacker, defender) have many, many armies, what's the chance that the defender would lose 5 armies strictly before the attacker loses 4?
#(i.e., what's the chance that the attacker loses no more than 3 armies in the first 4 rounds?)

'''
ANSWER = 0.46065957344177616
'''
print("---------------ASSIGNMENT 2---------------")
# Constants:
'''
deflose = 5
attlose = 4
oddrounds = int((deflose + attlose)/2) #4, in our specific case
# Not used in this program -- would be used for general deflose and attlose
'''

alosetwo = 2275/7776
bothloseone = 2611/7776
dlosetwo = 2890/7776

# CASES
# 3 indistinguishable items into 4 distinguishable boxes -- 6 choose 3 minus 4 = 20 - 4 = 16 (because of cases where all 3 are in one box)
# 2 indistinguishable items into 4 distinguishable boxes -- 5 choose 3 = 10
# 1 indistinguishable items into 4 distinguishable boxes -- 4
# 0 indistinguishable items into 4 distinguishable boxes -- 1
# TOTAL CASES = 31

# Huh, there's a cool shortcut. To put n OR LESS indistinguishable items into k distinguishable boxes, we can basically just add another box that represents "not in the other boxes."
# So, to put 3 OR LESS indistinguishable items into 4 distinguishable boxes, we can do C(n+k, k) = C(7, 4) = 35.

# Let's make a list of all possible cases:
tempcases = []
cases = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                tempcases.append((i,j,k,l))
for case in tempcases:
    if sum(case) <= 3:
        cases.append(case)
# Now "cases" is a list of all valid cases

#print(len(cases)) #gives 31. Great!

def caseodds(case):
    ''' Gives the odds of a single case occurring'''
    global alosetwo
    global bothloseone
    global dlosetwo
    odds = 1
    for num in case:
        if num == 0:
            odds = odds*dlosetwo
        elif num == 1:
            odds = odds*bothloseone
        elif num == 2:
            odds = odds*alosetwo
    return odds

# Now, we can put the odds of each case occurring in a list and sum it up
oddslist = []
for case in cases:
    oddslist.append(caseodds(case))
    
totalodds = sum(oddslist)

print("The odds of the defender losing 5 armies strictly before the attacker loses 4 is " + str(totalodds) + ".\n")
 
# I thought of a pretty quick way to check!
checkodds = 0
# Cases with only zeros
checkodds += (dlosetwo**4)
# Cases with three zeros and one one
checkodds += (4*bothloseone*(dlosetwo**3))
# Cases with two zeros and two ones
checkodds += (6*(bothloseone**2)*(dlosetwo**2))
# Cases with one zero and three ones
checkodds += (4*(bothloseone**3)*dlosetwo)
# Cases with three zeros and one two
checkodds += (4*alosetwo*(dlosetwo**3))
# Cases with one one, one two, and two zeros
checkodds += (4*3*(alosetwo)*(bothloseone)*(dlosetwo**2))

print("Doublechecking, we get " + str(checkodds) + ".\n")







