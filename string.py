S="aabcdbbcda"
op=""
for i  in S:
    if i not in op:
        op = op + 1
print(op)
for i in op:
    print("occurance of ", i, S.count(i))