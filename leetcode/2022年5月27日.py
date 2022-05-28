words = ["I","am","a","student","from","a","university","in","a","city"]
word1 = "a"
word2 = "student"
hashmap = {}
dis = len(words)
for place, word in enumerate(words):
    if word1==word:
        hashmap[word1]=place
    if word2==word:
        hashmap[word2]=place

    if word2 in hashmap and word1 in hashmap:
        dis = min(abs(hashmap[word2] - hashmap[word1]),dis)

print(dis)


