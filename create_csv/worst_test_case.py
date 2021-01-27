import csv


class WorstTestCase:
    def __init__(self, num_param):
        self.num_param = num_param
        self.boundary_values = []
        self.extreme_values = []
        self.table = []
        self.t1 = []

    def f(self, i, table1):
        tem = []
        if i == 0:
            for j in range(5):
                a = self.extreme_values[i][j]
                tem.append([a])
        else:
            for j in range(len(table1)):
                a = table1[j]
                # print(a)
                for k in range(5):
                    b = a[:]
                    b.append(self.extreme_values[i][k])
                    # print(b)
                    tem.append(b)
        # print(tem)
        return tem

    def generateTable(self):
        for i in range(self.num_param):
            self.t1 = self.f(i, self.t1)

    def input_data(self):
        for i in range(self.num_param):
            a = int(input(f'parameter {i+1} lower bound : '))
            b = int(input(f'parameter {i+1} upper bound : '))
            self.boundary_values.append([a, b])
        # print(self.boundary_values)

    def calculate_extreme_values(self):
        for i in range(self.num_param):
            min = self.boundary_values[i][0]
            max = self.boundary_values[i][1]
            nom = int((min+max)/2)
            self.extreme_values.append([min, min+1, max, max-1, nom])

    def formating_data(self):
        header = ["test case"]
        for i in range(self.num_param):
            header.append(f'param{i+1}')
        header.append("expected output")
        self.table.append(header)
        self.generateTable()
        for i in range(len(self.t1)):
            tab = [i+1]
            for j in range(len(self.t1[i])):
                tab.append(self.t1[i][j])
            self.table.append(tab)

    def get_csv(self):
        self.input_data()
        self.calculate_extreme_values()
        self.formating_data()
        with open('../bvc_add2.csv', 'w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            for x in self.table:
                wr.writerow(x)


if __name__ == '__main__':
    n = int(input("Enter number of parameter: "))
    wrc = WorstTestCase(n)
    wrc.get_csv()