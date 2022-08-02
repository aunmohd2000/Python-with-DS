import linecache


data=""
while True:
    line=input("line >>>")
    if not line:
        break
    data += line+" "

print('you have entered following data')
print(data)