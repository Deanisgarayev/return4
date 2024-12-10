
def calculate_structure_sum(data):
    sum = 0
    if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
        for i in data:
            sum += value(i)
    elif isinstance(data, dict):
        for i, j in data.items():
            sum += value(i)
            sum += value(j)
    return sum

def value(a):
    count = 0
    if isinstance(a, int):
        count += a
        return count
    elif isinstance(a, str):
        count += len(a)
        return count
    else:
        return calculate_structure_sum(a)

data_structure = [ [1, 2, 3,], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}]) ]
result = calculate_structure_sum(data_structure)
print(result)