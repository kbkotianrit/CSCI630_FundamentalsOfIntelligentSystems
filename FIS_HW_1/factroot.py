import math
import sys

basicConstant = 4

def factroot(expectedOutput):
    outputString = []
    obtainedOutput = basicConstant
    innermostFactCount = 0
    flag = True
    outputString = factrootRecursion(expectedOutput, innermostFactCount, obtainedOutput, outputString, flag)
    return outputString

def factrootRecursion(expectedOutput, innermostFactCount, obtainedOutput, outputString, flag) :
    if math.floor(math.sqrt(obtainedOutput)) == expectedOutput:
        return outputString.append('f')

    elif math.sqrt(obtainedOutput) > expectedOutput or not flag:
        if math.sqrt(obtainedOutput) > expectedOutput * expectedOutput and flag :
            return factrootRecursion(expectedOutput, innermostFactCount, math.sqrt(obtainedOutput), outputString.append('s'), flag)
        elif innermostFactCount > 0 or flag :
            for x in range(0, innermostFactCount):
                obtainedOutput = math.factorial(obtainedOutput)
                outputString.append('!')
            flag = True
            return factrootRecursion(expectedOutput, innermostFactCount, obtainedOutput, outputString, flag)
        else:
            return factrootRecursion(expectedOutput, innermostFactCount, math.factorial(obtainedOutput), outputString.append('!'), flag)

    else:
        del outputString[:]
        obtainedOutput = basicConstant
        innermostFactCount += 1
        flag = False
        return factrootRecursion(expectedOutput, innermostFactCount, obtainedOutput, outputString, flag)

def main():
    print(factroot(int(sys.argv[1])))

if __name__ == '__main__':
    main()
