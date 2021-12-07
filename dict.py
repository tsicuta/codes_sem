print()
d = {"apple": "яблоко", "pen": "карандаш", "watch": "часы"}
print(d["apple"])
print()

print (d)
print()

d2 = dict()
d2["apple"] = "яблоко"
print(d2)
print()

d["apple"] = "яблоко2"
print(d)
print()

print(d.keys())
print()
d = {"apple": "яблоко", "pen": "карандаш", "watch": "часы"}
print(d["apple"])
word = input()
trans_word =  input()
if not word in d.keys():
    d[word] = trans_word
print(d)