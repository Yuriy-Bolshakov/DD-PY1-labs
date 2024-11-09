from typing import List

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

missing_index = numbers.index(None)

numbers_without_missing: List[int] = [num for num in numbers if num is not None]

average = round(sum(numbers_without_missing) / (len(numbers_without_missing) + 1), 2)

numbers[missing_index] = average

print("Измененный список:", numbers)
