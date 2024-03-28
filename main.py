def readFile(text):
    f = open(text, 'r', encoding="UTF-8")
    wood = []
    k = 1
    answ = []
    while True:
        line = f.readline().strip()
        if line=="0":
            wood.append(answ)
            break
        if not line:
            raise Exception("Некоректные данные")
        if k > 3:
            wood.append(answ)
            k = 0
            answ = []
        answ.append(line)
        k += 1
    return wood
def findClosest(elem, seq):
    answ = abs(seq[0]-elem)
    answIndex = 0
    for i in range(1, len(seq)):
        if (abs(seq[i]-elem)<answ):
            answ = abs(seq[i]-elem)
            answIndex = i
    return answIndex

def woodLog(l, seq):
    if len(seq)==1:
        return l

    if len(seq)%2!=0: # odd
        ind = findClosest(l/2, seq)
        return woodLog(
                seq[ind],
                seq[:ind]) \
            + woodLog(
                l - seq[ind],
                [i - seq[ind] for i in seq[ind+1:]]) \
            + l
    else: # even
        if seq[0] != l - seq[-1]:
            if seq[0] > l - seq[-1]:
                return l + woodLog(l - seq[0], [i - seq[0] for i in seq[1:]])
            else:
                return l + woodLog(l - seq[-1], seq[:-1])
        else:
            ind = findClosest(l / 2, seq)
            if ind == 0:
                return l + woodLog(l - seq[0], [i - seq[0] for i in seq[1:]])
            elif ind == len(seq) - 1:
                return l + woodLog(l - seq[-1], seq[:-1])
            else:
                return woodLog(
                    seq[ind],
                    seq[:ind]) \
                    + woodLog(
                        l - seq[ind],
                        [i - seq[ind] for i in seq[ind + 1:]]) \
                    + l

def getAnswer(wood):
    for i in wood:
        l = int(i[0])
        seq = list(map(int, i[2].split(" ")))
        print("The minimum cutting price is", woodLog(l, seq))

from os import listdir, getcwd

print(getcwd())
files = [i for i in listdir(getcwd()) if ".txt" in i]

for i, file in enumerate(files, start=1):
    try:
        print(f"Тест {i}")
        getAnswer(readFile(file))
    except Exception as e:
        print(e)


# A = [
#     (10, [4, 5, 7, 8]),
#     (7, [i for i in range(1, 7)]),
#     (8, [i for i in range(1, 8)]),
#     (100, [25, 50, 75]),
#     (10, [2, 4, 7])
# ]
#
# for l, seq in A:
#     print(l, seq, woodLog(l, seq))
#     print()
# print(woodLog(10, [4, 5, 7, 8]))
# print(woodLog(7, [i for i in range(1, 7)]))
# print(woodLog(8, [i for i in range(1, 8)]))
