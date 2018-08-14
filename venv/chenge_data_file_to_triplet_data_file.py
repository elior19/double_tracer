description = ''
component = []
priors = []
bugs = []
name_of_test = []
function_in_test = []
result_of_test = []
initialtests = ""
start_test = 0

countSingle = 0
countDouble = 0
countTriplet = 0
countOldBugs = 0

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
fileName = 'CVE-2017-9207'


pathLittle = '../../../Desktop/matrices/dominators/'
pathBig = '../../../Desktop/matrices/xrefs/'

# with open(pathLittle + fileName + '.txt') as f:
with open(pathBig + fileName + '.txt') as f:
    lines = f.read().splitlines()
    i=0
    while i < len(lines):
        if(lines[i] == '[Description]'):
            description = lines[i+1]
        elif(lines[i] == '[Components names]'):
            pre_component = lines[i+1].split('), (')
            for p in pre_component:
                new_p = p.split(', ')
                component.append(str(new_p[1].split("'")[1]))
            countSingle = len(component)
        elif(lines[i] == '[Priors]'):
            pre_priors = lines[i+1].split(', ')
            for p in range(len(pre_priors)):
                if(p==0):
                    priors.append(float(pre_priors[p].split('[')[1]))
                elif(p==len(pre_priors)-1):
                    priors.append(float(pre_priors[p].split(']')[0]))
                else:
                    priors.append(float(pre_priors[p]))
        elif(lines[i]=='[Bugs]'):
            pre_bugs = lines[i+1].split(', ')
            for p in range(len(pre_bugs)):
                if(p==0):
                    bugs.append(int(pre_bugs[p].split('[')[1]))
                elif(p==len(pre_bugs)-1):
                    bugs.append(int(pre_bugs[p].split(']')[0]))
                else:
                    bugs.append(int(pre_bugs[p]))
                countOldBugs = countOldBugs + 1
        elif(lines[i]=='[InitialTests]'):
            initialtests = lines[i+1]
        elif(lines[i]=='[TestDetails]'):
            i=i+1
            break

        i = i+1
        
    while i < len(lines):
         pre_line = lines[i].split(';[')
         line = pre_line[1].split('];')
         name_of_test.append(pre_line[0])
         pre_functions = line[0].split(', ')
         functions = []
         for p in pre_functions:
             if p != '':
                functions.append(int(p))
         function_in_test.append(functions)
         result_of_test.append(int(line[1]))
         i=i+1
    while(start_test<len(function_in_test)):
        len_list = len(function_in_test[start_test])
        for i2 in range(len_list-1):
            str1 = component[function_in_test[start_test][i2]]+"_"+component[function_in_test[start_test][i2+1]]
            if (str1 in component):
                function_in_test[start_test].append(component.index(str1))
            else:
                component.append(str1)
                countDouble = countDouble + 1
                priors.append(0.1)
                function_in_test[start_test].append(component.index(str1))
            if(((function_in_test[start_test][i2] in bugs) or (function_in_test[start_test][i2+1] in bugs)) and (component.index(str1) not in bugs)):
                    bugs.append(component.index(str1))
        for i3 in range(len_list-2):
            str1 = component[function_in_test[start_test][i3]]+"_"+component[function_in_test[start_test][i3+1]]+"_"+component[function_in_test[start_test][i3+2]]
            if (str1 in component):
                function_in_test[start_test].append(component.index(str1))
                
            else:
                component.append(str1)
                countTriplet = countTriplet + 1
                function_in_test[start_test].append(component.index(str1))
            if(((function_in_test[start_test][i3] in bugs) or (function_in_test[start_test][i3+1] in bugs) or (function_in_test[start_test][i3+2] in bugs)) and (component.index(str1) not in bugs)):
                    bugs.append(component.index(str1))
        start_test = start_test+1

    new_component = []
    for i in range(len(component)):
        tmp = (i, component[i])
        new_component.append(tmp)

    


directoryPathLittle = 'files-after-transform/dominators/'
directoryPathBig = 'files-after-transform/xrefs/'

# write_file = open(directoryPathLittle + fileName + '-transformed.txt','w')
write_file = open(directoryPathBig + fileName + '-transformed.txt','w')

write_file.write('[Description]\n')
write_file.write(description+'\n')
write_file.write('[Components names]\n')
write_file.write(str(new_component)+'\n')
print("single component: " + str(countSingle))
print("double component: " + str(countDouble))
print("triplet component: " + str(countTriplet))
sum = countSingle + countDouble + countTriplet
print("all component: " + str(len(component)) + " = " + str(sum))
write_file.write('[Priors]\n')
write_file.write(str(priors)+'\n')
write_file.write('[Bugs]\n')
print("old bugs: " + str(countOldBugs))
print("bugs: " + str(len(bugs)))
write_file.write(str(bugs)+'\n')
write_file.write('[InitialTests]\n')
write_file.write(str(initialtests)+'\n')
write_file.write('[TestDetails]\n')
for i in range(len(function_in_test)):
 
    write_file.write(name_of_test[i]+";"+str(function_in_test[i])+';'+str(result_of_test[i])+'\n')
write_file.close()

