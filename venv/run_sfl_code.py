from sfl_diagnoser.Diagnoser import diagnoserUtils
from sfl_diagnoser.Diagnoser import Diagnosis_Results
import sfl_diagnoser.Diagnoser.ExperimentInstance


########### single ###############
# dominators
# fileName = 'CVE-2017-7623'
# fileName = 'CVE-2017-7939'
# fileName = 'CVE-2017-9204'
# fileName = 'CVE-2017-9205'
# fileName = 'CVE-2017-9206'
# fileName = 'CVE-2017-9207'

# xrefs
# fileName = 'CVE-2015-8784'
# fileName = 'CVE-2016-8691'
# fileName = 'CVE-2016-8692'
# fileName = 'CVE-2016-8887'
# fileName = 'CVE-2016-10250'
# fileName = 'CVE-2016-10251'
# fileName = 'CVE-2016-10271'
# fileName = 'CVE-2016-10272'
# fileName = 'CVE-2017-7452'
# fileName = 'CVE-2017-7453'
# fileName = 'CVE-2017-7454'
# fileName = 'CVE-2017-7623'
# fileName = 'CVE-2017-7939'
# fileName = 'CVE-2017-7962'
# fileName = 'CVE-2017-9204'
# fileName = 'CVE-2017-9205'
# fileName = 'CVE-2017-9206'
# fileName = 'CVE-2017-9207'


########### transformed ###############
# dominators
# fileName = 'CVE-2017-7623-transformed'
# fileName = 'CVE-2017-7939-transformed'
# fileName = 'CVE-2017-9204-transformed'
# fileName = 'CVE-2017-9205-transformed'
# fileName = 'CVE-2017-9206-transformed'
# fileName = 'CVE-2017-9207-transformed'

# xrefs
# fileName = 'CVE-2015-8784-transformed'
# fileName = 'CVE-2016-8691-transformed'
# fileName = 'CVE-2016-8692-transformed'
# fileName = 'CVE-2016-8887-transformed'
# fileName = 'CVE-2016-10250-transformed'
# fileName = 'CVE-2016-10251-transformed'
# fileName = 'CVE-2016-10271-transformed'
# fileName = 'CVE-2016-10272-transformed'
# fileName = 'CVE-2017-7452-transformed'
# fileName = 'CVE-2017-7453-transformed'
# fileName = 'CVE-2017-7454-transformed'
# fileName = 'CVE-2017-7623-transformed'
# fileName = 'CVE-2017-7939-transformed'
# fileName = 'CVE-2017-7962-transformed'
# fileName = 'CVE-2017-9204-transformed'
# fileName = 'CVE-2017-9205-transformed'
# fileName = 'CVE-2017-9206-transformed'
fileName = 'CVE-2017-9207-transformed'

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
diagnosis = inst.diagnoses
file123.write(str(diagnosis))
print("diagnosis len: " + str(len(diagnosis)))
file123.write('\n')
file123.write('\n')
file123.write(str(inst.initial_tests))
file123.write('\n')
file123.write('\n')
file123.write(str(inst.error))
file123.write('\n')
file123.close()
# ei = sfl_diagnoser.Diagnoser.ExperimentInstance.addTests(inst,inst.hp_next())