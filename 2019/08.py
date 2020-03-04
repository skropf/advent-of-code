### Day 8 - Part 1

from math import inf
puzzle_orig = open('08.input', 'r')
puzzle = puzzle_orig.read()
puzzle_orig.close()

image_width = 25
image_height = 6
pixels = image_width * image_height

# splitting the input into the image layers
image_layers = [puzzle[i:i+pixels] for i in range(0, len(puzzle), pixels)]

control_layer, min_zeros = "", inf
for layer in image_layers:
    if layer.count('0') < min_zeros:
        min_zeros = layer.count('0')
        control_layer = layer

print("Checksum:", control_layer.count('1') * control_layer.count('2'))


### Day 8 - Part 2

resulting_image = [pixel for pixel in image_layers[0]]

for layer in image_layers:
    for i in range(pixels):
        if resulting_image[i] == '2':
            resulting_image[i] = layer[i]

print("Resulting image/message:", )
[print(x) for x in [''.join(resulting_image)[i:i+image_width] for i in range(0, len(''.join(resulting_image)), image_width)]]