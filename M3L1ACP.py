#======================
#My Running Lap Tracker
#======================

#Topics - Pseudocode,Time Complexity and Space Complexity

#Problem - A runner completes laps.They complete laps and earn points like: Lap 1 = 1 point,Lap 2 = 2 points,Lap 3 = 3 points etc.
#Find the total running points after n laps using three different solutions.

n = 5

print("======================")
print("My Running Lap Tracker")
print("======================")
print("Number of Laps: ",n)
print()

#Solution 1 - Formula Method
#Algorithm - Use the formula n * (n + 1) // 2 to calculate points correctly

#Pseudocode:
#START
#    total = n * (n + 1) //2
#    print total
#END

formula_total = n * (n + 1) //2

print("Solution 1 - Formula Method")
print(f"Total Running Points:{formula_total}  Time Complexity : 0(1)   Space Complexity : 0(1)")
print()

#Solution - Loop Method

#Algorithm - Start total from 0
#Add each lap number one by one.

#Pseudocode:
#START
#   total = 0
#   for lap from 1 to n
#   total = total + lap
#   print total
#END

nested_total = 0
steps_nested = 0

for lap in range(1,n + 1):
    for point in range(1,lap + 1):
        nested_total = nested_total + 1
        steps_nested = steps_nested + 1

print("Solution 3:Nested Loop Method")
print("Total Running Points:",nested_total)
print("Steps Taken:",steps_nested)
print("Time Complexity: O(n^2)")
print("Space Complexity: O(1)")
print()

#Algorithm Efficiency Comparing

print("Algorithm Efficiency Comparison")
print("\n")
print("Formula Methof: Fastest because it only uses one calculation.")
print("Loop Method: Slower because it repeats once for every lap.")
print("Nested Loop Method:Slowest because it uses a loop inside another loop.")
print()
print("Best Method:Formula Method")
print("Reason:It has 0(1) time complexity,so it stays fast even when laps increase.")
print("========================================================================================")
