def printTable(tableData):
	# First find the longest string from all of the inner lists.
	sub_list_longest = []
	for sub_list in tableData:
		longest = max([len(word) for word in sub_list])
		sub_list_longest.append(longest)
	print(sub_list_longest)
	
	leftWidth = sub_list_longest[0] + 1
	midWidth = sub_list_longest[1] + 1
	rightWidth = sub_list_longest[2] + 1
	
	for i in range(len(tableData) + 1):
		print(tableData[0][i].rjust(leftWidth, ' ') + tableData[1][i].rjust(midWidth, ' ') + tableData[2][i].rjust(rightWidth, ' '))


if __name__ == "__main__":
	tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
	print(printTable(tableData))

			 
