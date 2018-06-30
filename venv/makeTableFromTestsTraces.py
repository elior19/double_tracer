import os

class makeTableFromTestsTraces:

    def readContent(self, fileName, path):
        new_path = path + '/' + fileName
        f = open(new_path, 'r')
        content = f.readlines()
        f.close()
        return content

    def readFromFileAndCalculate(self):
        path = '../../../Documents/accumulo-master/DebuggerTests'
        componane_names = []
        test_table = []

        for fileName in os.listdir(path):

            content = self.readContent(fileName, path)
            new_test = []

            for row in range(len(content)):

                componane_name_1 = content[row].split('@',len(content[row]))[1]
                componane_name_2 = 0
                componane_name_3 = 0

                if row < len(content) - 2:
                    componane_name_2 = content[row].split('@', len(content[row]))[1].strip() + '_' + content[row+2].split('@', len(content[row+2]))[1]

                if row < len(content) - 3:
                    componane_name_3 = content[row].split('@', len(content[row]))[1].strip() + '_' + content[row+2].split('@', len(content[row+2]))[1].strip() + '_' + content[row+3].split('@', len(content[row+3]))[1]

                if componane_name_1 not in componane_names:
                    componane_names.append(componane_name_1)

                if componane_name_2 is not 0 and componane_name_2 not in componane_names:
                    componane_names.append(componane_name_2)
                new_test.append(componane_names.index(componane_name_1))
                if componane_name_2 is not 0:
                    new_test.append(componane_names.index(componane_name_2))

                if componane_name_3 is not 0 and componane_name_3 not in componane_names:
                    componane_names.append(componane_name_3)
                new_test.append(componane_names.index(componane_name_1))
                if componane_name_3 is not 0:
                    new_test.append(componane_names.index(componane_name_3))

            test_table.append({'file_name' : fileName, 'table' : new_test})

        return (componane_names, test_table)
