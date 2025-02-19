def printNos(self, n):
    def printRec(current):
        if (current > n):
            return
        print(current, end=' ')
        printRec(current + 1)

    printRec(1)