import re 
import email.utils as eu

emailPattern = re.compile(r'^[^\W\_][\w\-\.]*@[^\d\W\_]+\.[^\d\W\_]{1,3}$')

def email_str(parsed_email):
    return parsed_email[1]

def check_email(emailStr):
    return bool(emailPattern.match(emailStr))

if __name__ == "__main__":
    N = int(input().rstrip())

    for _ in range(N):
        emailTup = eu.parseaddr(input().rstrip())
        if check_email(email_str(emailTup)):
            print(eu.formataddr(emailTup))
