def get_score(elm):
    return elm[1]

def get_name(elm):
    return elm[0]

def less_than(elm, name, score):
    if score == get_score(elm):
        return (name < get_name(elm))
    else:
        return (score < get_score(elm))
    
def greater_than(elm, name, score):
    if score == get_score(elm):
        return (name > get_name(elm))
    else:
        return (score > get_score(elm))
    
def second_lowest_score(studends):
    lowest = get_score(students[0])
    student = 1
    while get_score(students[student]) == lowest and student < len(students):
        student += 1
        
    if student < len(students):
        return get_score(studends[student])
    else:
        return None
    
        

if __name__ == '__main__':
    students = []
    place = 0
    for _ in range(int(input())):
        done = False
        name = input()
        score = float(input())
        place = 0

        if students:
            while place < len(students):
                if greater_than(students[place], name, score):
                    place += 1
                else:
                    students.insert(place, [name, score,])
                    done = True
                    break
                      
            if not done:
                students.append([name, score,])
            
        else:
            students.append([name, score,])
            

    SLS = second_lowest_score(students)
    for student in list(filter(lambda x: get_score(x) == SLS, students)):
        print(get_name(student))