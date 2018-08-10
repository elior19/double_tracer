from sfl_diagnoser.Diagnoser import diagnoserUtils
from sfl_diagnoser.Diagnoser import Diagnosis_Results
import sfl_diagnoser.Diagnoser.ExperimentInstance

# fileName = 'CVE-2017-9207'
fileName = 'CVE-2016-9207-transformed'

# file123 = open('sfl_diagnoser/output-single/xrefs/' + fileName + '-out.txt' ,'w')
file123 = open('sfl_diagnoser/output/xrefs/' + fileName + '-out.txt' ,'w')
# file123 = open('sfl_diagnoser/output-single/dominators/' + fileName + '-out.txt' ,'w')
# file123 = open('sfl_diagnoser/output/dominators/' + fileName + '-out.txt' ,'w')

# inst = diagnoserUtils.readPlanningFile('sfl_diagnoser/input-single/xrefs/' + fileName + '.txt')
inst = diagnoserUtils.readPlanningFile('sfl_diagnoser/input/xrefs/' + fileName + '.txt')
# inst = diagnoserUtils.readPlanningFile('sfl_diagnoser/input-single/dominators/' + fileName + '.txt')
# inst = diagnoserUtils.readPlanningFile('sfl_diagnoser/input/dominators/' + fileName + '.txt')

inst.diagnose()
results = Diagnosis_Results.Diagnosis_Results(inst.diagnoses,inst.initial_tests,inst.error)

file123.write(str(results.get_metrics_names()))
file123.write(str(results.get_metrics_values()))
file123.write('\n')
file123.write('\n')
file123.write(str(inst.diagnoses))
file123.write('\n')
file123.write('\n')
file123.write(str(inst.initial_tests))
file123.write('\n')
file123.write('\n')
file123.write(str(inst.error))
file123.write('\n')
file123.close()
# ei = sfl_diagnoser.Diagnoser.ExperimentInstance.addTests(inst,inst.hp_next())