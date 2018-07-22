import sqlite3
import glob
import os

SURFIRE_DIR_NAME = 'surefire-reports'

class readTestsResults:

    def readTestData(self, fileName, path):
        new_path = path + '/' + fileName
        f = open(new_path, 'r')
        content = f.readlines()
        f.close()
        return content
    
    def calculateNumberOfErrorsAndFailures(self, testData):
        numberOfErrors = (testData[1].split('errors="', len(testData[1]))[1].strip())[0]
        numberOfFailures = (testData[1].split('failures="', len(testData[1]))[1].strip())[0]
        return int(numberOfErrors), int(numberOfFailures)
    
    def checkTestStatus(self, numberOfErrors, numberOfFailures):
        # check if were failures or errors somewere
        if numberOfErrors > 0 or numberOfFailures > 0:
            ans = 1 #1
        else:
            ans = 0
        return ans

    def calculateTestName(self, fileName):
        testName = fileName.split('TEST-', len(fileName))[1].strip()
        testName = testName.split('.xml', len(fileName))[0].strip()
        return testName

    def readFromFile(self):
        # path = '../../../Documents/accumulo-master/surfire-reports'
        # path = '../../../Documents/reef-master/reef-master/lang/java/reef-utils/target/surefire-reports'
        # path = '../../../Documents/tika-master/tika-master/tika-server/target/surefire-reports'
        path = '../../../Documents/ant-master/ant-master/target/ant/surefire-reports'
    

        tests = []
        for fileName in os.listdir(path):
            if fileName.endswith('.xml'):
                testData = self.readTestData(fileName, path)
                numberOfErrors, numberOfFailures = self.calculateNumberOfErrorsAndFailures(testData)
                testStatus = self.checkTestStatus(numberOfErrors, numberOfFailures)

                testName = self.calculateTestName(fileName)
                tests.append({'testName': testName, 'testStatus': testStatus})
        # print(tests)
        # print("\n")
                # print(testName)
                # print(testStatus)
        return tests