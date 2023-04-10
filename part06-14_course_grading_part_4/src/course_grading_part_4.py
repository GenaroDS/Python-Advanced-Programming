def main():
    student_file = input("Student information: ")
    exercises_file = input("Exercises completed: ")
    exam_points_file = input("Exam points: ")
    course_file = input("Course information: ")

    with open(course_file, 'r') as f:
        course_info = dict(line.strip().split(': ') for line in f.readlines())

    students = {}
    with open(student_file, 'r') as f:
        for line in f.readlines():
            student_id, student_name, *_ = line.strip().split(';')
            students[student_id] = {'name': student_name}


    with open(exercises_file, 'r') as f:
        for line in f.readlines():
            student_id, exec_nbr, exec_pts, *_ = line.strip().split(';')
            try:
                students[student_id]['exec_nbr'] = int(exec_nbr)
                students[student_id]['exec_pts'] = int(exec_pts)
            except ValueError:
                print(f"Error: Invalid data in exercises file for student {student_id}: {exec_nbr}, {exec_pts}")



    with open(exam_points_file, 'r') as f:
        for line in f.readlines():
            student_id, exm_pts = line.strip().split(';')
            students[student_id]['exm_pts'] = int(exm_pts)

    for student_id, student_data in students.items():
        student_data['tot_pts'] = student_data['exec_pts'] + student_data['exm_pts']
        student_data['grade'] = min(5, student_data['tot_pts'] // 3)

    with open('results.txt', 'w') as f:
        f.write(f"{course_info['name']}, {course_info['study credits']} credits\n")
        f.write("======================================\n")
        f.write("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")
        for student_data in students.values():
            f.write("{:<30} {:<8} {:<8} {:<8} {:<8} {}\n".format(
                student_data['name'],
                student_data['exec_nbr'],
                student_data['exec_pts'],
                student_data['exm_pts'],
                student_data['tot_pts'],
                student_data['grade']
            ))

    with open('results.csv', 'w') as f:
        for student_id, student_data in students.items():
            f.write(f"{student_id};{student_data['name']};{student_data['grade']}\n")

    print("Results written to files results.txt and results.csv")


main()
