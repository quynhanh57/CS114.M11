nam = ["lios", "etr", "initis"]
nu = ["liala", "etra", "inites"]

def Gioitinhn(n):
    for i in nam:
        if (i == n[-len(i):]):
            return 1
    for i in nu:
        if i == nu[-len(i):]:
            return 0
    return -1

def Loaitun(n):
    for i in range(len(nam)):
        if (n[-len(nam[i]):] == nam[i]):
            return i
    for i in range(len(nu)):       
        if (n[-len(nu[i]):] == nu[i]):
            return i
    return -1

def Checkdanhtu(loaitu):
    if loaitu.count(1) != 1 and len(loaitu) > 1:
        return False
    return True

def Checkvitri(loaitu):
    for i in range(len(loaitu) - 1):
        if (loaitu[i] > loaitu[i+1]):
            return False
    return True

def Checkgioitinh(gioitinh):
    for i in gioitinh:
        if (i != gioitinh[0]):
            return False
    return True

w = list(input().split())
gioitinh = [Gioitinhn(n) for n in w]
loaitu = [Loaitun(n) for n in w]

result = True

if (gioitinh.count(-1) != 0 or loaitu.count(-1) != 0):
    result = False
if (Checkdanhtu(loaitu) == False):
    result = False
if (Checkvitri(loaitu) == False):
    result = False
if (Checkgioitinh(gioitinh) == False):
    result = False

if result:
    print("YES")
else:
    print("NO")