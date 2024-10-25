# https://www.codewars.com/kata/5875b200d520904a04000003

def enough(cap, on, wait):
    if (on + wait) <= cap:
        return 0
    if (on + wait) > cap:
        return ( on + wait - cap)