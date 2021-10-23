import operator
def most_freq():
    s=str(input("Enter a string:"))
    s1=s.lower()
    d={}.fromkeys([x for x in s1],0)
    for char in s1:
        d[char]+= 1
    d1=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
    print(d1)
most_freq()
