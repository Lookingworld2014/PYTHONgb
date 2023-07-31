# Задача №21. 
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

d = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
     {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

unique_values = set()

for item in d:
    for value in item.values():
        unique_values.add(value.strip())

print(unique_values) # Output: {'S005', 'S002', 'S007', 'S001', 'S009'}