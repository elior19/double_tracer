# import makeTableFromTestsTracesDouble
import makeTableFromTestsTraces
import PrintToMatrixFile
import readTestsResults

# componaneNames, testTable = makeTableFromTestsTracesDouble.makeTableFromTestsTracesDouble().readFromFileAndCalculate()
testsResults = readTestsResults.readTestsResults().readFromFile()
componaneNames, testTable = makeTableFromTestsTraces.makeTableFromTestsTraces().readFromFileAndCalculate()
PrintToMatrixFile.PrintToMatrixFile().printToFile(componaneNames, testTable, testsResults)

