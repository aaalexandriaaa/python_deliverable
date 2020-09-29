# #  https://git.generalassemb.ly/SEI-CC/SEI-CC-8/blob/master/work/w07/d5/04-python-functions-lab.md

def sum_to(n):
    i = 0
    total = n
    while i != n:
        total += i
        i += 1
    print(f'sum_to ', total)
    return total

sum_to(10)

def largest(inp):
    print(f'largest ', max(inp))
    return max(inp)

largest([1, 2, 3, 4, 0])  # returns 4
largest([10, 4, 2, 231, 91, 54])  # returns 231

def occurances(str1, str2):
    print(f'occurances ', str1.count(str2))
    return str1.count(str2)

occurances('fleep floop', 'e')   # returns 2
occurances('fleep floop', 'p')   # returns 2
occurances('fleep floop', 'ee')  # returns 1
occurances('fleep floop', 'fe')  # returns 0

def product(*args):
    total = 1
    for arg in args:
        total = total * arg
    print("product", total)

product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0

