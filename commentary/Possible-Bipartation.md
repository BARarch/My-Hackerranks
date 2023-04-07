# Intuition
We have to assign people into two sets.  Everyone in a set can't dislike each other.  Interesting!

# Approach
Start assigning groups to people and memoize the groups (the $$g$$ array) once we know all the people a particular person dislikes (the $$D$$ map).  We attempt to recursively assign people known to be disliked by others to that group opposite from the person which dislikes them `groupHelper(D[person][i], assignGroup(group)`.  

...That is if they have not been assigned a group allready. 

If we can assign everyone with no conflicts, that's great! We have a computed list of actual assginments too!

If a person incounters person that they dislike and we try to assign them to the other group, but they're allready assigned to theirs, we fail the branch.  Thats ok, we'll backtrack all the way back to the root of the recursion and assign THAT person to the OTHER group.  We then try again with the group assignments as they were at the time, because we copied the memoized groups with `gSaved := make([]string, len(g))` and `copy(gSaved, g)`.  If we fail to assign everyone here then it is really impossible.

# Complexity
- Time complexity:
$$O(n^2)$$ Worst case.  The implementation assigns a group to each person and stores it in a slice.  The slice is used for memoization so we don't revisit the same people and re-evaluate the same dislikes.  It's copied for each person that is assigned a group at the root of a recusion.  This could happen for every person if no one dislikes anyone else.

- Space complexity:
$$O(n)$$ Worst case.  Same reseasons as above.

# Code
```
// The Group array
var g []string

// The DISLIKES Hash Map: Slices of Slices
var D [][]int

func possibleBipartition(n int, dislikes [][]int) bool {
	g = make([]string, n+1)
	for i := range g {
		g[i] = ""
	}
    g[0] = "a"
	fmt.Println(g)

	D = make([][]int, n+1)
	for i := range D {
		D[i] = make([]int, 0)
	}
	//fmt.Println(D)

	// Fill Dislikes
	for _, dislike := range dislikes {
		//fmt.Println(dislike)
		D[dislike[0]] = append(D[dislike[0]], dislike[1])
	}
	fmt.Println(D)

    //Loop Through all ungrouped Nodes
    for i := range g {
        if g[i] == "" {
            gSaved := make([]string, len(g))
            copy(gSaved, g) // get a copy of g here at the root of the BFS in case we need to backtrack 
            if !groupHelper(i, "a"){ // if this attempt fails backtrack with alternate group assignment
                g = gSaved
                fmt.Println("Try ", i, "in group b with")
                fmt.Println(gSaved)
                if !groupHelper(i, "b") { // if this one fails there are no other viable solutions
                    return false
                }
            }
        }
    }
    fmt.Println("DONE!")
    fmt.Println(g)
	return true
}

func groupHelper(person int, group string) bool {
    g[person] = group
    // We are checking g and D here
    for i := range D[person] {
        if g[D[person][i]] == ""{
            // recurse into child, alternate group
            if !groupHelper(D[person][i], assignGroup(group)) { // if recursion fails leave group
                return false
            }
        } else if g[D[person][i]] == group { // If group for this node has a conflict with a previous assignment
            fmt.Println("Bottom Out!")
            fmt.Println(g)
            fmt.Println(person, " Dislikes ", D[person][i], " and is in group ", group)
            return false
        }
    }
	return true
}

func assignGroup(group string) string {
    if group == "a" {
        return "b"
    }
    return "a"
}
```