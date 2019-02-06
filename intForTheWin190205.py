

def age_key(person):
    return int(person[2])

def person_lister(f):
    def inner(people):
        peopleDict = {}
        for person in people:
            if age_key(person) in peopleDict:
                peopleDict[age_key(person)].append(person)
            else:
                peopleDict[age_key(person)] = [person]        
        res = []
        #print (sorted(peopleDict))
        for age in sorted(peopleDict):
            res.extend(peopleDict[age])
        return list(map(f, res))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
