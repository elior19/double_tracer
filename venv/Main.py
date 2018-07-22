import makeTableFromTestsTracesOnlyOne
import makeTableFromTestsTraces
import PrintToMatrixFile
import readTestsResults

testsResults = readTestsResults.readTestsResults().readFromFile()
# componaneNames, testTable = makeTableFromTestsTracesOnlyOne.makeTableFromTestsTracesOnlyOne().readFromFileAndCalculate()
componaneNames, testTable = makeTableFromTestsTraces.makeTableFromTestsTraces().readFromFileAndCalculate()
PrintToMatrixFile.PrintToMatrixFile().printToFile(componaneNames, testTable, testsResults)

