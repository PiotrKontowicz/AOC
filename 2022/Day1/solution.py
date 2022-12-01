def ex1():
    with open('ex1.txt', 'r') as f:
        data = [x for x in ''.join(f.readlines()).split('\n\n')]
        data = [sum([int(y) for y in x.split('\n')]) for x in data]
        return max(data)

def ex2():
    with open('ex1.txt', 'r') as f:
        data = [x for x in ''.join(f.readlines()).split('\n\n')]
        data = [sum([int(y) for y in x.split('\n')]) for x in data]
        data.sort()
        return sum(data[-3::])

print('Part 1: {}'.format(ex1()))
print('Part 2: {}'.format(ex2()))