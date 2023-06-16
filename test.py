def sum_even_numbers(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total_sum += num
    return total_sum

# Пример использования функции
start_num = 1
end_num = 10
result = sum_even_numbers(start_num, end_num)
print("Сумма всех четных чисел от", start_num, "до", end_num, ":", result)
