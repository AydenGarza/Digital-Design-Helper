literalsCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class booleanFunction ():
    booleanExpression = None
    literalsPresent = None
    numLiterals = None
    truthTable = None
    canonicalMinterm = None
    canonicalMaxterm = None
    minimumSumOfProducts = None
    minimumProductOfSums = None
    #constructor
    def __init__ (self, booleanExpression):
        self.booleanExpression = booleanExpression.replace(" ", "")
        self.literalsPresent = booleanFunction.getLiterals(self.booleanExpression)
        self.numLiterals = len(self.literalsPresent)
    #creates and returns an array with all literals present in a given boolean expression string
    def getLiterals(expressionString):
        listOfLiteralsPresent = []
        for x in expressionString:
            if x in literalsCharacters and x not in listOfLiteralsPresent:
                listOfLiteralsPresent.append(x)
        return sorted(listOfLiteralsPresent)
    #generates a truth table for a given boolean expression object, zero parameter function
    def generateTruthTable(self):
        def generateInputCombinations():
            inputCombinations = []
            for index in range(0, 2**self.numLiterals):
                binaryInputCombination = bin(index)
                #print("This is supposed to have prefix and all: " + binaryInputCombination)
                binaryInputCombination = binaryInputCombination[2:]
                #print("This is post trim: " + binaryInputCombination)
                if len(binaryInputCombination) < self.numLiterals:
                    padlength = self.numLiterals - len(binaryInputCombination)
                    pad = ''
                    for x in range(0, padlength):
                        pad+='0'
                    binaryInputCombination = pad+binaryInputCombination
                inputCombinations.append(binaryInputCombination)
            return inputCombinations
        def generateFunctionOutputs():
            #using input combination and given boolean expression to get a boolean expression
            stringExpression = self.booleanExpression
            inputCombinations = generateInputCombinations()
            functionOutputs = []
            for inputCombination in inputCombinations: #for each XYZ in the list of 000 through 111
                functionOutput = None
                binaryFormattedString = str(stringExpression)
                #print("NEXT COMBO")
                #print("inputCombination: " + inputCombination)
                #print("binaryFormattedString before the translation: " + binaryFormattedString)
                for i in range(0, len(inputCombination)): # for each character in the XYZ, check if its a 1 or 0, and replace the corresponding character in the boolean expression with that 1 or 0 value
                    if inputCombination[i] == '0':
                        binaryFormattedString = binaryFormattedString.replace(self.literalsPresent[i],'0') #the length of literals present and the length of inputCombination should be equal
                    else:
                        binaryFormattedString = binaryFormattedString.replace(self.literalsPresent[i],'1')
                #print("binaryFormattedString after the translation:" + binaryFormattedString)
                index = 0
                while index < len(binaryFormattedString):
                    if index != 0 and binaryFormattedString[index] != '+' and binaryFormattedString[index-1] != '+' and binaryFormattedString[index] != "'" and binaryFormattedString[index] != ")" and binaryFormattedString[index-1] != "(":
                        binaryFormattedString = binaryFormattedString[:index] + ' ' + binaryFormattedString[index:]
                        index+=2
                    else:
                        index+=1
                #print("binaryFormattedString after the space adding thing: X" + binaryFormattedString + "X")

                binaryFormattedString = binaryFormattedString.replace(' ', ' and ')
                #print("binaryFormattedString after I replaced spaces with and: X" + binaryFormattedString + "X")

                binaryFormattedString = binaryFormattedString.replace('+', ' or ')
                #print("binaryFormattedString after replacing + with or: X" + binaryFormattedString + "X")

                #compliment string to not statement translation
                index = 0
                while "'" in binaryFormattedString:
                    if binaryFormattedString[index] == "'":
                        binaryFormattedString = binaryFormattedString[:index] + ")" + binaryFormattedString[index+1:]
                        #print("yo:" + binaryFormattedString)
                        binaryFormattedString = binaryFormattedString[:index-1] + "not(" + binaryFormattedString[index-1] + binaryFormattedString[index:]
                        #print("yall:" + binaryFormattedString)
                        
                    index = index + 1

                binaryFormattedString = binaryFormattedString.replace('1', 'True')
                #print("Replaced 1 with True: X" + binaryFormattedString + "X")

                binaryFormattedString = binaryFormattedString.replace('0', "False")
                #print("Replaced 0 with False: X" + binaryFormattedString + "X")

                functionOutput = eval(binaryFormattedString)
                functionOutputs.append(functionOutput)
                #print("Moment of truth:" + str(functionOutput))
                #print()
            #print("functionOutputs list: " ,end='')
            #print(functionOutputs)
            return functionOutputs
        #creating the truth table
        headerRow = self.literalsPresent[:]
        headerRow.append("F")
        truthtable = []
        truthtable.append(headerRow)
        tt_inputCombinations = generateInputCombinations()
        tt_functionOutputs = generateFunctionOutputs()
        for rowIndex in range(0, 2**self.numLiterals):
            inputCombinationArray = list(tt_inputCombinations[rowIndex])
            truthTableRow = inputCombinationArray + [tt_functionOutputs[rowIndex]]
            truthtable.append(truthTableRow)
        
        #for x in truthtable:
            #print(x)
        return truthtable

inputExpression = input("type your boolean expression")
testFunction = booleanFunction(inputExpression)
truthtable = testFunction.generateTruthTable()
print("Your expression: " + f'{testFunction.booleanExpression}')
print("The literals present in your expression: " + f'{testFunction.literalsPresent}')
print("The number of literals present in your expression: "+f'{testFunction.numLiterals}')
print("The unformatted truth table: " + f'{testFunction.generateTruthTable()}')
print("The formatted truth table: ")
for row in truthtable:
    print(row)