## This is code for LeedCodes 38. Count and Say

import string

if __name__ == "__main__":

    def countAndSay(n: int) -> str:
        if n == 1:
            return "1"
        else:
            ##digits = say(countAndSay)
            return say(countAndSay(n - 1))

    def say(digits: str) -> str:
        prev, count = digits[0], 1
        res = ""
        for d in digits[1:]:
            if d == prev:
                count += 1
                addLast = True
            else:
                res += str(count) + prev
                prev, count = d, 1
                addLast = False
        ##if addLast:
        res += str(count) + prev
        return res

    print(countAndSay(4))
   ## print(say("4"))

'''countAndSay(4)
= say(countAndSay(3))
= say(say(countAndSay(2)))
= say(say(say(countAndSay(1)))
= say(say(say('1'))))
= say(say('11'))
= say('21')
= '1211' '''
   

