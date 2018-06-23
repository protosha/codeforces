"""
This code solves task 144A from codeforces.org
link: https://codeforces.com/problemset/problem/144/A
"""
from sys import stdin, stdout

# read number of soldiers (n)
soldier_count = int(stdin.readline().rstrip())
# read all of their heights (a1, a2, ..., an)
heights = list(map(int, stdin.readline().rstrip().split()))

max = 0
imax = 0
min = 101
imin = 0
for i in range(0, len(heights)):
    height = heights[i]
    # search for maximum height with the least index
    if max < height:
        max = height
        imax = i
    # search for minimum height with the highest index
    if min >= height:
        min = height
        imin = i

if max == min:
    # all soldiers have the save height, so we don't need to perform any swaps
    stdout.write("0\n")
elif imin < imax:
    # time spent to bubble up the shortest soldier
    time = len(heights) - imin - 1
    # time spent to bubble up the tallest soldier
    # we save 1 second, because of bubbling up the shortest soldier
    time += imax - 1
    stdout.write(str(time) + "\n")
else:
    # same as previous, but without 1 second advantage
    time = len(heights) - imin - 1
    time += imax
    stdout.write(str(time) + "\n")