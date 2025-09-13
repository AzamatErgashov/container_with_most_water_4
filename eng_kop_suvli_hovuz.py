mylist = [1,8,6,5,10,11]

i, j = 0, len(mylist) - 1

max_area = 0
while i < j:
    area = (j - i) *  min(mylist[i], mylist[j]) 
    # print(area)
    max_area = max(area, max_area)

    if mylist[i] < mylist[j]:
        i += 1
    else:
        j -= 1
print(max_area)