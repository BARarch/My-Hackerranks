def get_score(elm):
    return elm[1]

def get_name(elm):
    return elm[0]

def less_than(elm, name, score):
    if score == get_score(elm):
        return (name < get_name(elm))
    else:
        return (score < get_score(elm))
            
        
if __name__ == '__main__':
    students = []
    place = 0
    for _ in range(int(input())):
        done = False
        name = input()
        score = float(input())
        print("{} {}".format(name, str(score)))
        place = 0
        ## find a place
        if students:
            while place < len(students):
                print(place)
                print(less_than(students[place], name, place))
                if less_than(students[place], name, place):
                    print('less than')
                    place += 1
                else:
                    print("inserting {} {}".format(name, str(score)))
                    students.insert(place, [name, score,])
                    done = True
                    break
                      
            if not done:
            ## Add to the end of list
                print("placing at the end {} {}".format(name, str(score)))
                students.append([name, score,])
            
        else:
            # It was emtpy
            print("placing at the end {} {}".format(name, str(score)))
            students.append([name, score,])
            
    print(students)
