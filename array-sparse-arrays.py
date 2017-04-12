# Enter your code here. Read input from STDIN. Print output to STDOUT
num_strs = int(raw_input())
str_cts = {}

# iterate through the strings and populate str_cts dictionary with strings as keys and counts as values
for i in range(num_strs):
    new_str = raw_input()
    str_cts[new_str] = str_cts.setdefault(new_str, 0) + 1

num_queries = int(raw_input())
for i in range(num_queries):
    target = raw_input()
    print str_cts.get(target, 0)
