f = open('nameslist.txt', 'r')
answer = {}
for line in f:
    k, v = line.strip().split('=')
    answer[k.strip()] = v.strip()

f.close()