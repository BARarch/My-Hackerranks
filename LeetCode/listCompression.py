'''
This code is for LeetCode 443. String Compression
February 23, 2022
'''

import string

if __name__ == "__main__":

    def insertAndCompress(chars, count, groupPos, group):
        if count == 1:
            print(f'compressed {group} group {chars} index at {groupPos}')
            return groupPos
        else:
            for digit in str(count):
                chars.insert(groupPos, digit)
                groupPos += 1
            ## Remove all extras all count - 1 of them
            del chars[groupPos: groupPos + count - 1]
            print(f'compressed {group} group {chars} index at {groupPos}')
            return groupPos 
             

    def compress(chars)  -> int:
        print(f'Initial string {chars}')
        group, count = chars[0], 1
        groupPos = 1
        index = 1
        while index < len(chars):
            if chars[index] == group:
                count += 1
                index += 1
            else:
                ## Compress Previous Group
                index = insertAndCompress(chars, count, groupPos, group)
                ## Start New Group
                group, count, groupPos = chars[index], 0, index + 1
        
        ## Append the remaining Group
        index = insertAndCompress(chars, count, groupPos, group)

        
        return len(chars)


    print(compress(["a", "a","b", "b", "b", "f", "f", "c", "c"]))
    print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

    '''
    char.insert(groupPos, )
    '''

   

