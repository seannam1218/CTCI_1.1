#Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?

#brute force approach. Running time = O(n^2)
def UniqueCheck(str):
    for i in range(0, len(str)):
        for j in range(i+1, len(str)):
            if (str[i] == str[j]):
                return False;
    return True;

#Quicksort approach. Running time = O(nlog(n))
def FastCheck(str):
    sorted_str = quickSort(str)
    for i in range(0, len(sorted_str)-1):
        if (sorted_str[i] == sorted_str[i+1]):
            return False;
    return True;


def quickSort(str):
    str_list = list(str)
    pivot = str_list[0]
    left = []
    right = []
    for i in range(1,len(str_list)):
        s = str_list[i]
        if s <= pivot:
            left.append(s)
        elif s > pivot:
            right.append(s)
    if len(left) > 1:
        left = quickSort(left)
    if len(right) > 1:
        right = quickSort(right)
    ret = left + list(pivot) + right
    return ret


#test
print(str(UniqueCheck("damn")) + ", " + str(FastCheck("damn")))
print(str(UniqueCheck("wow")) + ", " + str(FastCheck("wow")))
print(str(UniqueCheck("this has to come out false")) + ", " + str(FastCheck("this has to come out false")))
print(str(UniqueCheck("nice tru")) + ", " + str(FastCheck("nice tru")))

print(quickSort("nfdsahr"))