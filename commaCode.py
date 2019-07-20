def commaCode(list):
	list.insert(len(list) - 1, 'and')
	return ', '.join(list) + '.'
		
print(commaCode(['apples', 'bananas', 'tofu', 'cats']))
# Output: 'apples, bananas, tofu, and, cats.
# Output in book: 'apples, bananas, tofu, and cats.

print(commaCode(['apples', 'bananas', 'pears', 'oranges', 'peaches', 'plums']))
# Output: 'apples, bananas, pears, oranges, peaches, and, plums.
