def sortStudents(students):
    students.sort(key=lambda x:x.split(" ")[-1])
    return students

if __name__ == "__main__":

    exec(f'st = {input()}')
    print(st)
    print(type(st))

    print(sortStudents(students=st))