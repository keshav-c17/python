from collections import  namedtuple
n = int(input())
column_heading = input().split()
student = namedtuple('student', column_heading)
marks_ls = []
for i in range(n):
    data_input = input().split()
    s = student(*data_input)
    marks_ls.append(int(s.MARKS))

print("{:.2f}".format(sum(marks_ls)/len(marks_ls)))



