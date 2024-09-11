
def calculate_structure_sum(structure):
    total = 0
    if isinstance(structure, (int, float)):
        return structure
    elif isinstance(structure, dict):
        for key, value in structure.items():
            total += calculate_structure_sum(len(key))
            total += calculate_structure_sum(value)
    elif isinstance(structure, (list, tuple, set)):
        for item in structure:
            total += calculate_structure_sum(item)
    elif isinstance(structure, (str)):
        for words in structure:
            total += calculate_structure_sum(len(words))
    return total


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
