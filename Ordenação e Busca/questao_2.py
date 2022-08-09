n = int(int(input()))
grades = []
for i in range(n):
    grades.append(float(input()))

grades.sort()
# for grade in grades: print(grade)
for i in range(len(grades)-1, -1, -1): print(f'{grades[i]:.2f}')