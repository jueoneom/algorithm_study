def solution(answers):
    answer = []
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    students = [[0, 1],[0, 2],[0, 3]]
    
    for i, ans in enumerate(answers):
        if student1[ i % len(student1) ] == ans:
            students[0][0] += 1
        if student2[ i % len(student2) ] == ans:
            students[1][0] += 1
        if student3[ i % len(student3) ] == ans:
            students[2][0] += 1
            
    students.sort(key = lambda x: -x[0])
    max = students[0][0]
    for count, student in students:
        if max <= count:
            answer.append(student)
            
    return answer