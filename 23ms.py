#Millisecond 23
import os
import queue

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/23input.txt", 'r')

instructions = file.read().strip().split('\n')

registry = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}

def value(elem, registry):
    try: return int(elem)
    except: return registry[elem]

#Millisecond 18: First half
def execute(instructions):
    count_mul = 0
    i = 0

    while i < len(instructions) and i >= 0:
        instruction = instructions[i]

        elems = instruction.split(' ')
        operation = elems[0]

        if operation == "set":
            registry[elems[1]] = value(elems[2], registry)
            i += 1
        if operation == "sub":
            registry[elems[1]] = value(elems[1], registry) - value(elems[2], registry)
            i += 1
        if operation == "mul":
            registry[elems[1]] = value(elems[1], registry) * value(elems[2], registry)
            count_mul += 1
            i += 1
        if operation == "jnz":
            x = value(elems[1], registry)
            if x != 0:
                i += value(elems[2], registry)
            else:
                i += 1

    return count_mul


print(execute(instructions))

#Millisecond 18: Second half
from math import sqrt

class PrimeGen():

    __primes = []
    __old_count = 3

    def __gen_prime__(self, number, count):

        while count <= number:
            isprime = True

            for x in range(2, int(sqrt(count) + 1)):
                if count % x == 0:
                    isprime = False
                    break

            if isprime: self.__primes.append(count)
            count += 1

        return count

    def __contains__(self, value):
        self.__old_count = self.__gen_prime__(value, self.__old_count)
        return value in self.__primes



def execute2(instructions):
    prime_gen = PrimeGen()

    b = 81 * 100 + 100000
    c = b + 17000
    h = 0

    while True:
        if b not in prime_gen: h += 1
        if b == c: return h
        b += 17

print(execute2(instructions))

## Explanation of second half
# def implementation_of_instrucions():
#     b = 81 * 100 + 100000
#     c = b + 17000
#     h = 0
#
#     while True:
#         f = 1
#         d = 2
#         while d - b != 0:
#             e = 2
#             while e - b != 0:
#                 if d * e - b == 0: #it will try all possible combinations of multiplicators (up to value of b)
#                     f = 0          #[the two while conditions] and if a pair is found it is not a prime number. ==> h += 1
#                 e += 1
#             d += 1
#         if f == 0: h += 1
#         if b == c: break
#         b += 17
#     print(h)
