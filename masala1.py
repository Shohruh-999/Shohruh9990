def func(ls, n):
    res = []
    for i in range(0, len(ls), n):
        res.append(ls[i:i+n])
    print(res)

ls = ["A", "B", "C", "D", "E", "F", "G", "L", "Q", "U"]
n = int(input("Son kiriting: "))
func(ls, n)
