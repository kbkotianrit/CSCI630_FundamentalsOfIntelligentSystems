import random
import statistics

def payBack(testTuple):
    if testTuple == ["BAR"]*3:
        return 20
    elif testTuple == ["BELL"]*3:
        return 15
    elif testTuple == ["LEMON"]*3:
        return 5
    elif testTuple == ["CHERRY"]*3:
        return 3
    elif testTuple[0] == testTuple[1] =="CHERRY":
        return 2
    elif testTuple[0] == "CHERRY":
        return 1
    else:
        return 0

def generateRandomSlotMachineCombinations():
    availableFruits = ["BELL", "BAR", "LEMON", "CHERRY"]
    randomFruitCombination = []
    for combinationValues in range(3):
        randomFruitCombination.append(random.choice(availableFruits))
    return randomFruitCombination

def playTillBroke(coinsAvailableToInvest):
    balanceMoney = coinsAvailableToInvest
    numberOfPlays = 0
    while balanceMoney > 0:
        # 1 coin to play a turn
        balanceMoney -= 1
        balanceMoney += payBack(generateRandomSlotMachineCombinations())
        numberOfPlays += 1
    return numberOfPlays

def simulation(coinsAvailableToInvest, numberOfSimulations):
    numberOfPlaysSimulationList = []
    for x in range(numberOfSimulations):
        numberOfPlaysSimulationList.append(playTillBroke(coinsAvailableToInvest))
    mean = statistics.mean(numberOfPlaysSimulationList)
    median = statistics.median(numberOfPlaysSimulationList)
    return mean, median

def main():
    mean,median = simulation(10, 100)
    print("Mean = ",mean,"\nMedian = ",median )

if __name__ == '__main__':
    main()



