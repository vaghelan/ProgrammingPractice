import heapq


h = []

items = [

{ "key" : 5, "name" : "Nilesh"},

{"key" : 1, "name" : "Neelam"}

]

def get_key(s):
    print (s)
    return s["key"]


#print (heapq.nsmallest(2, items, key=lambda s: s['key']))
print (heapq.nsmallest(10, items, key=get_key))