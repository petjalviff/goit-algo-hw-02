from collections import deque

def is_palindrome(input_string):
    # приведення рядка у нижній регістр та видалення пробілів
    string = input_string.lower().replace(" ", "")
    
    # Ініціалізація черги для зберігання символів рядка
    d_queue = deque()
    
    # Додавання кожного символу рядка до черги
    for char in string:
        d_queue.append(char)
    
    # Порівняння символів з обох кінців черги
    while len(d_queue) > 1:
        if d_queue.popleft() != d_queue.pop():
            return print("Ні, введений рядок не є паліндромом")
    
    # Якщо всі символи збігаються, рядок є паліндромом
    return print("Так, введений рядок є паліндромом")

# Приклад використання
is_palindrome(input("Введіть речення або слово для перевірки (наприклад: кит на морі романтик):"))


