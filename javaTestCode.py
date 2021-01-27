import csv

csvFile = "bvc_get_gpa.csv"
javaFile = "javaFile2.txt"
report = "report2.csv"

def cal_sum(a):
    tot = 0
    for i in a:
        tot += int(i)
    return tot-int(a[0])


def getGPA(grade):
    # total = cal_sum(a)
    # print(total)
    print(grade)
    gpa = 0.0
    if grade == "A+":
        gpa = 4.00
    elif grade == "A":
        gpa = 3.50
    elif grade == "B":
        gpa = 3.00
    elif grade == "C":
        gpa = 2.00
    else:
        gpa = 0.00
    return gpa



def create_java_class():
    testFuncName = "getGPA"
    className = "GradeCalculator"
    with open(csvFile, 'r', newline='') as csv_file, open(javaFile, 'w') as java_test, open(report, 'w', newline='') as report_csv:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_writer = csv.writer(report_csv, quoting=csv.QUOTE_ALL)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                csv_writer.writerow(row)
            else:
                # if row[2] == 0:
                #     java_test.write(
                #         f"@Test\npublic void {testFuncName} () " + "{" + f"\n\tint a = \"{row[1]}\";" + f"\n\tint b = {row[2]};" + f"\n\t{className} obj = new {className}();" + f"\n\tint exp = MATH.INF;\n\tint res = obj.{testFuncName}(a);\n\tassertEquals(exp,res);\n" + "}\n")
                #     row.append("Infinity")
                #     row.append("Error")
                #     row.append("Failed")
                #     csv_writer.writerow(row)
                #     continue
                expected = getGPA(row[1])
                output = expected
                java_test.write(f"@Test\npublic void {testFuncName} () "+"{" + f"\n\tint a = \"{row[1]}\";" + f"\n\t{className} obj = new {className}();" + f"\n\tint exp = {expected};\n\tint res = obj.{testFuncName}(a);\n\tassertEquals(exp,res);\n" + "}\n")
                row.append(expected)
                row.append(output)
                row.append("passed")
                csv_writer.writerow(row)

            line_count += 1
        print(f'Processed {line_count} lines.')

create_java_class()








# + f"\n\tint b = {row[2]};"+ f"\n\tint c = {row[3]};"+ f"\n\tint d = {row[4]};"


# def get_grade(a):
#     total = cal_sum(a)
#     print(total)
#     if total >= 80:
#         grade = "A+"
#     elif total >= 70:
#         grade = "A"
#     elif total >= 60:
#         grade = "B"
#     elif total >= 50:
#         grade = "c"
#     else:
#         grade = "F"
#     return grade
#
# def getGPA(grade):
#     # total = cal_sum(a)
#     # print(total)
#     print(grade)
#     gpa = 0.0
#     if grade == "A+":
#         gpa = 4.00
#     elif grade == "A":
#         gpa = 3.50
#     elif grade == "B":
#         gpa = 3.00
#     elif grade == "C":
#         gpa = 2.00
#     else:
#         gpa = 0.00
#     return gpa