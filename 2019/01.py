### DAY 1 - Part 1

from math import floor

input = open('01.input', 'r')
sum_fuel = 0

for module in input:
    sum_fuel += floor(int(module) / 3.0) - 2

print('The fuel requirement of the spacecraft is:', sum_fuel)
input.close()

### DAY 1 - Part 2

def fuel_per_module(module, sum_fuel):
    if floor(module / 3.0) - 2 <= 0: return sum_fuel
    
    module = floor(module / 3.0) - 2
    sum_fuel += module
    
    return fuel_per_module(module, sum_fuel)

input = open('01.input', 'r')
sum_fuel = 0

for module in input:
    sum_fuel += fuel_per_module(int(module), 0)

print('The overall fuel requirement of the spacecraft is:', sum_fuel)
input.close()