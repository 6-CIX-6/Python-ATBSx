import copy

def commaCode(someList):
    if someList == [] or len(someList) == 1:
        print("List is empty.")
    else:
        tempList = copy.copy(someList)
        del someList[-1]
        del tempList[:-1]
        someString = ''
        print('someList: ' + str(someList))
        print('templist: ' + str(tempList))
        for i in someList:
            someString = someString + i + ", "
        print(someString + 'and ' + tempList[0])


spam = ['apples', 'bananas', 'tofu', 'cats']
turd = []
commaCode(spam)
commaCode(turd)
