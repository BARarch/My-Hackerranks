def removeTasks(k, toDo):
    del toDo[k-1::k]
    return toDo

if __name__ == "__main__":
    ll = [1237, 2847, 27485, 2947, 1, 247, 374827, 22]
    print(removeTasks(3, ll))
