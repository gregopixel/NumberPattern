import collections

numList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = float(input("Please enter the Value of %d Element : " % i))
    numList.append(value)

numList.sort()
# mean
print("Element After Sorting List in Ascending Order is : ", numList)
print("Mean is", sum(numList)/Number)

# median
if Number % 2 == 0:
    median1 = numList[Number // 2]
    median2 = numList[Number // 2 - 1]
    median = (median1 + median2) / 2
    print("Median is", median)
else:
    median = (numList[int((Number-1)/2)])
    print("Median is", median)

# mode
data = collections.Counter(numList)
dataList = dict(data)
print("Frequency of each unique item", dataList)
maxValue = max(list(data.values()))
print(maxValue)



