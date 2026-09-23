def search_employee(ids, target, index):
    if index == len(ids):
        return -1
    if ids[index] == target:
        return index
    return search_employee(ids, target, index + 1)


ids = [101, 102, 103, 104, 105]
target = int(input("Enter employee ID to search: "))

result = search_employee(ids, target, 0)

if result != -1:
    print("Employee ID found at index", result)
else:
    print("Employee ID not found")
