
# 0index  #1index  #2index
# last index of list will be (number of items in a list-1)
states = ['State1', "State2", "State3"]
randomList = [1, 2, 3, 2]
id = ["0xff3455", 2, 5, 'black', 3, 4, 555, 66]
# id = list((4,5,6))

# result = states[0]
# result = states[2]
result = id[7]
# print(result)

days = ['sun', 'mon', 'tue', 'wed', 'thu']
numberOfItems = len(days)
# print(numberOfItems)
lastIndex = numberOfItems-1
lastItem = days[lastIndex]
# print(lastItem)
# days[0]="changed"
# print(days[0])
days.append('fri')
print(days)


