if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for student_num in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

if query_name in student_marks :
    marks_for_avg = student_marks[query_name]
avg = sum(marks_for_avg)/len(marks_for_avg)
formatted_avg = "{:.2f}".format(avg)
print(formatted_avg)