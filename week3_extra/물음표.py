input_arr =["러러파덕", "러파덕"]
in_set = set()
temp = sorted(input_arr)
input_arr.sort()
print(input_arr)
for p in temp:
    for h in in_set:
        if h in p or p in h:
            print("True")
        
    in_set.add(p)

print(sorted(in_set))