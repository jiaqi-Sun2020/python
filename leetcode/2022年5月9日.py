
s =  "IDID"
s_list = list(s)

n = len(s_list)
o = 0


for i,ele in enumerate(s_list):
    if i==0:
        if ele == 'I':
            ret=[o]
            o += 1
        if ele == 'D':
            ret=[n]
            n -= 1
    if ele == 'I':

        ret.append(n)
        n -= 1
    if ele == 'D':

        ret.append(o)
        o+=1
print(ret)


