def triangle():
    first_side = float(input("Введіть довжину першої сторони: "))  # Запрошую данні першої сторони
    second_side = float(input("Введіть довжину другої сторони: "))  # Запрошую данні другої сторони
    third_side = float(input("Введіть довжину третьої сторони: "))  # Запрошую данні третьої сторони
    if first_side + second_side > third_side and second_side + third_side > first_side and first_side + third_side > second_side:  # Якщо данні відповідають пропорціям , обичслюєм :
        half_perimeter = (first_side + second_side + third_side) / 2  # пів периметр
        s = pow(half_perimeter * (half_perimeter - first_side) * (half_perimeter - second_side) * (half_perimeter - third_side), 1 / 2)  # і площу
        answer = (f"Площа трикутника зі сторонами {first_side}, {second_side}, {third_side} складає: {s}")
    else:  # В інакшому випадку вибиваєм текст що данні не коректін
        answer = (f'Трикутник зі сторонами {first_side}, {second_side}, {third_side} існувати не може. И площі у нього також немає :)')
    return answer
answer = triangle()
print(answer)