colors = ['black', 'white']
sizes = ['S', 'M', 'L']

t_shirts = [(color, size) for color in colors for size in sizes]
print(t_shirts)

for color in colors:
	for size in sizes:
		print((color, size))