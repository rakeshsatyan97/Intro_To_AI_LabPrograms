## change s and t accordingly
s=False
t=False
a = not(s or t)
print(a)
b = s and t
print(b)
c = t or(not t)
print(c)
d = not((not s or s) and (not s or s))
print(d)
e = not(not s) and (not t)
print(e)

if a==b:
    print("a entails b")
if a==c:
    print("a entails c")
if a==d:
    print("a entails d")
if a==e:
    print("a entails e")
else:
    print("no entailment")
