f = open('result.txt')

res = int(f.readline())
print(res)
if res==0:
  raise Exception()
