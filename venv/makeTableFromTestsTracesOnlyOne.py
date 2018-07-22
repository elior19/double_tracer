import os

class makeTableFromTestsTracesOnlyOne:

    def readContent(self, fileName, path):
        new_path = path + '/' + fileName
        f = open(new_path, 'r')
        content = f.readlines()
        f.close()
        return content

    def readFromFileAndCalculate(self):
        # path = '../../../Documents/accumulo-master/DebuggerTests'
        # path = '../../../Documents/reef-master/reef-master/lang/DebuggerTests'
        # path = '../../../Documents/tika-master/DebuggerTests'
        path = '../../../Documents/ant-master/DebuggerTests'
        
        componane_names = []
        test_table = []

        for fileName in os.listdir(path):

            content = self.readContent(fileName, path)
            new_test = []

            for row in range(len(content)):

                componane_name_1 = content[row].split('@',len(content[row]))[1]
                

                if row < len(content) - 2:
                    componane_name_2 = content[row].split('@', len(content[row]))[1].strip() + '_' + content[row+2].split('@', len(content[row+2]))[1]
                if componane_name_1 not in componane_names:
                    componane_names.append(componane_name_1)

                
                new_test.append(componane_names.index(componane_name_1))
                


            test_table.append({'file_name' : fileName, 'table' : new_test})

        return (componane_names, test_table)
