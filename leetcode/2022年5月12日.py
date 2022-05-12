strs = ["zyx","wvu","tsr"]
flag_list = [0 for x in range(len(strs[0]))]
list__ = ["a" for x in range(len(strs[0]))]
for i,ele in enumerate(strs):
    for t, e in enumerate(ele):
        if e>= list__[t]:
            list__[t]=e
        else:
            flag_list[t]=1
print(sum(flag_list))


