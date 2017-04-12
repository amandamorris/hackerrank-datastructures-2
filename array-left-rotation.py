# Enter your code here. Read input from STDIN. Print output to STDOUT
length, numrotes = raw_input().split()
length = int(length)
numrotes = int(numrotes)
lst = raw_input().split()

lst = [lst[((i + numrotes) % length)] for i in range(length)]

for elem in lst:
    print elem,
