ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
#calculating min and max ages
min_num = min(ages)
max_num = max(ages)
#printing the ages
print("minimum:", min_num)
print("maximum:", max_num)
#inserting min and max ages
ages.insert(0,19)
ages.append(26)
print(ages)
# Import statistics Library
import statistics
# Calculate middle value
print(statistics.median(ages))
# Python program to get average of a list
average=sum(ages)/len(ages)
print(average)
#calculating range
range=max_num-min_num
print(range)