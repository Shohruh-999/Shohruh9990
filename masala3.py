def func(ls):
    dic = {}
    
    for i in ls:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    print(dic)

ls = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
func(ls)
