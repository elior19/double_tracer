class PrintToMatrixFile:

    def printComponentsNames(self, componane_names):
        componane_names_for_file = []
        for index in range(len(componane_names)):
            componane_names_for_file.append((index, componane_names[index].strip()))
        return componane_names_for_file
          
    def printPriors(self, componane_names):
        Priors_for_file = []
        for index in range(len(componane_names)):
            Priors_for_file.append(0.1)
        return Priors_for_file

    def findTestName(self, testsResults, test_table, index):
        ans = -1
        for i in range(len(testsResults)):
            if testsResults[i]['testName'] in test_table[index]['file_name']:
                ans = i
        return ans

    def printInitialTests(self, test_table, testsResults):
        initional_test_for_file = []
        testsNamesWithNumbers = []
        for index in range(len(test_table)):
            testNumber = 'T' + str(index + 1)
            initional_test_for_file.append(testNumber)
            testNameIndex = int(self.findTestName(testsResults, test_table, index))
            testName = str(testsResults[testNameIndex]['testName'])
            testsNamesWithNumbers.append({'testNumber': testNumber, 'testName': testName})
        return initional_test_for_file, testsNamesWithNumbers

    def findIndexOfTestNameByTestIndex(self, testsNamesWithNumbers, testIndex):
        for idx in range(len(testsNamesWithNumbers)):
            testName = testsNamesWithNumbers[idx]['testNumber']
            testNumber = testName.split('T')[1]
            if int(testNumber) is int(testIndex):
                return idx
        # if index does not exist return 0 (change to -1...)
        return 0

    def findTestResultIndexByTestName(self, testsResults, testName):
        for i in range(len(testsResults)):
            if testsResults[i]['testName'] is testName:
                return i
        # if index does not exist return 0 (change to -1...)
        return 0

    def findTestResult(self, testsResults, testsNamesWithNumbers, testIndex):
        # find in name-number table the test name by its number
        testNameIndex = self.findIndexOfTestNameByTestIndex(testsNamesWithNumbers, testIndex)
        testName = testsNamesWithNumbers[testNameIndex]['testName']
        # find in name-status table the test status by its name
        testStatusIndex = self.findTestResultIndexByTestName(testsResults, testName)
        testStatus = testsResults[testStatusIndex]['testStatus']
        return str(testStatus)

    def printTestDetails(self, file, test_table, initional_test_for_file, testsNamesWithNumbers, testsResults):
        # this function print to the file and not calculate like all the functions because we want to print \n before each line
        for index in range(len(test_table)):
            testResult = self.findTestResult(testsResults, testsNamesWithNumbers, index)
            file.write(initional_test_for_file[index] + ';' + str(test_table[index]['table']) + ';' + testResult)
            file.write('\n')
        
    def printToFile(self, componane_names, test_table, testsResults):
        f = open('out.txt', 'w')
        
        f.write('[Description]\n')
        f.write('default description\n')
        
        f.write('[Components names]\n')
        f.write(str(self.printComponentsNames(componane_names)) + '\n')
        
        f.write('[Priors]\n')
        f.write(str(self.printPriors(componane_names)) + '\n')
        
        f.write('[Bugs]\n')
        f.write(str([0]) + '\n')
        
        f.write('[InitialTests]\n')
        initional_test_for_file, testsNamesWithNumbers = self.printInitialTests(test_table, testsResults)
        f.write(str(initional_test_for_file) + '\n')

        f.write('[TestDetails]\n')
        self.printTestDetails(f, test_table, initional_test_for_file, testsNamesWithNumbers, testsResults)

        f.close()