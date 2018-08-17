from sfl_diagnoser.Diagnoser import diagnoserUtils
from sfl_diagnoser.Diagnoser import Diagnosis_Results
import sfl_diagnoser.Diagnoser.ExperimentInstance

################################## file name ###################################

########### single ###############
# dominators
fileName = 'CVE-2017-7623'
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
# fileName = 'CVE-2017-9207-transformed'

################################## file path ###################################

# file123 = open('sfl_diagnoser/output-single/xrefs/' + fileName + '-out.txt' ,'w')
# file123 = open('sfl_diagnoser/output/xrefs/' + fileName + '-out.txt' ,'w')
file123 = open('sfl_diagnoser/output-single/dominators/' + fileName + '-out.txt' ,'w')
# file123 = open('sfl_diagnoser/output/dominators/' + fileName + '-out.txt' ,'w')

# inst = diagnoserUtils.readPlanningFile('sfl_diagnoser/input-single/xrefs/' + fileName + '.txt')
# inst = diagnoserUtils.readPlanningFile('sfl_diagnoser/input/xrefs/' + fileName + '.txt')
inst = diagnoserUtils.readPlanningFile('sfl_diagnoser/input-single/dominators/' + fileName + '.txt')
# inst = diagnoserUtils.readPlanningFile('sfl_diagnoser/input/dominators/' + fileName + '.txt')


################################## calculate diagnoses ###################################

inst.diagnose()
results = Diagnosis_Results.Diagnosis_Results(inst.diagnoses,inst.initial_tests,inst.error)

################################## check diagnoses size from file ###################################

#get components numbers and prob
probabilities = ([x.probability for x in inst.diagnoses])
probability = probabilities[0]
print("\n")
print("prob: " + str(probability))

diagnosis_numbers = ([x.diagnosis for x in inst.diagnoses])
print("\n")
print("diag: " + str(diagnosis_numbers))

sum = 0

# read which component is double and which triplet
pathLittle = 'sfl_diagnoser/matrix-sizes/dominators/'
pathBig = 'sfl_diagnoser/matrix-sizes/xrefs/'

with open(pathLittle + fileName + '-components.txt') as f:
# with open(pathBig + fileName + '-components.txt') as f:
    lines = f.read().splitlines()
    i=0
    while i < len(lines):
        if(lines[i] == 'double_components:'):
            double_components = lines[i+1]
        elif(lines[i] == 'triplet_components:'):
            triplet_components = lines[i+1]
        i = i + 1
    print("\n")
    print("double_components: " + str(double_components))
    print("\n")
    print("triplet_components: " + str(triplet_components))

    # check the components
    for num in range(len(diagnosis_numbers)):
        # if you want to check the insides part of the diagnoses uncoment this and delete the zero.
        # then you can use any inside logic you want.
        # we decided to check by the first member.
        # for j in range(len(diagnosis_numbers[num])):
            j=0
            if str(diagnosis_numbers[num][j]) in double_components:
                sum = 2 * probability + sum
            if str(diagnosis_numbers[num][j]) in triplet_components:
                sum = 3 * probability + sum
            else:
                sum = 1 * probability + sum
    print("\n")
    print("sum: " + str(sum))

    #check the len
    len = len(inst.diagnoses)
    print("\n")
    print("diagnosis len: " + str(len))

    #calculate finale answer:
    ans = sum / len
    print("\n")
    print("final answer: " + str(ans))



################################## write answer to file ###################################

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