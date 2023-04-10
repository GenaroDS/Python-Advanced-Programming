layers = int(input("Layers: "))

# Determine the dimensions of the square
size = 2 * layers - 1

# Initialize the square with spaces
square = [[' ' for _ in range(size)] for _ in range(size)]

# Fill in the layers of the square
for layer in range(layers):
    letter = chr(ord('A') + layer)
    for i in range(layer, size - layer):
        square[layer][i] = letter
        square[size - layer - 1][i] = letter
        square[i][layer] = letter
        square[i][size - layer - 1] = letter

# If there are less than 3 layers, add a border of the outermost letter
if layers < 3:
    letter = chr(ord('A') + layers - 1)
    for i in range(size):
        square[0][i] = letter
        square[-1][i] = letter
        square[i][0] = letter
        square[i][-1] = letter

# Print the square
for row in square:
    print(''.join(row))



