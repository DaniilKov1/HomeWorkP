Login = input()
error = '=?*^$№@_'
list = []


for i in range(len(Login)):
    if Login[i] in error :
        list.append(Login[i])

print(list)