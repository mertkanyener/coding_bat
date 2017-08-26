#Coding bat warmup 2 exercises


def string_splosion(str):
    res = ''
    for i in range(len(str)):
        res = res + str[:i+1]
    return res

s = string_splosion('Code')
print(s)


def array_front9(arr):
    res = False
    rng = 4
    if len(arr) < 4:
        rng = len(arr)
    for i in range(rng):
        if arr[i] == 9:
            res = True
    return res

def array123(arr):
    res = False
    for i in range(len(arr)):
        if i + 2 < len(arr):
            if arr[i] == 1 and arr[i+1] == 2 and arr[i+2] == 3:
               res = True
    return res


#Coding bat Logic 2 exercises

def fix_teen(n):
    if n == 15 or n == 16:
        return n
    else:
        return 0


def no_teen_sum(a, b, c):
    l = [a ,b ,c]
    sum = 0
    for i in range(len(l)):
        if l[i] in range(13, 20):
            l[i] = fix_teen(l[i])
        sum
