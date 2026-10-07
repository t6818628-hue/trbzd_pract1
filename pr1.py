import numpy as np

data_coffee = np.array([
    [245, 310, 180, 260, 290, 3500, 220, 275, 240, 310],
    [190, 265, 285, 210, 245, 300, 180, 4000, 290, 150],
    [330, 220, 275, 240, 310, 190, 265, 285, 210, 245]
])

flat_data = data_coffee.flatten()
print(f"Все данные: {flat_data}")

mean_val = np.mean(flat_data)
print(f"Среднее значение: {mean_val}")

median_val = np.median(flat_data)
print(f"Медиана: {median_val}")

std_val = np.std(flat_data)
print(f"Стандартное отклонение: {std_val}")

var_val = np.var(flat_data)
print(f"Дисперсия: {var_val}")

max_val = np.max(flat_data)
print(f"Максимум: {max_val}")

min_val = np.min(flat_data)
print(f"Минимум: {min_val}")

range_val = max_val - min_val
print(f"Размах: {range_val}")

percentiles = np.percentile(flat_data, [25, 50, 75, 90, 99])
print(f"Перцентили (25, 50, 75, 90, 99): {percentiles}")

q1 = np.percentile(flat_data, 25)
q3 = np.percentile(flat_data, 75)
print(f"Первый квартиль: {q1}")
print(f"Третий квартиль: {q3}")

iqr = q3 - q1
print(f"Межквартильный размах: {iqr}")

low_border = q1 - 1.5 * iqr
high_border = q3 + 1.5 * iqr

outliers = flat_data[(flat_data < low_border) | (flat_data > high_border)]
print(f"Выбросы: {outliers}")

total_revenue = np.sum(flat_data)
print(f"Общая выручка за 60 дней: {total_revenue} рублей")

low_days = flat_data[flat_data < 200]
print(f"Дни с выручкой ниже 200 рублей: {low_days}")

A = np.array([210, 245, 300, 180, 260, 290, 150, 330, 220, 275, 240, 310, 190, 265, 285])

matrix = A.reshape(3, 5)
print(f"Матрица 3x5:\n{matrix}")

print(f"Размерность матрицы: {matrix.shape}")

print(f"Общее количество элементов: {matrix.size}")

sum_rows = matrix.sum(axis=1)
print(f"Сумма по строкам: {sum_rows}")

sum_cols = matrix.sum(axis=0)
print(f"Сумма по столбцам: {sum_cols}")

matrix_transposed = matrix.T
print(f"Транспонированная матрица:\n{matrix_transposed}")

flat_matrix = matrix.flatten()
print(f"Все элементы матрицы: {flat_matrix}")

mean_val = np.mean(flat_matrix)
print(f"Среднее значение: {mean_val}")

std_val = np.std(flat_matrix)
print(f"Стандартное отклонение: {std_val}")

var_val = np.var(flat_matrix)
print(f"Дисперсия: {var_val}")

q1 = np.percentile(flat_matrix, 25)
q2 = np.percentile(flat_matrix, 50)
q3 = np.percentile(flat_matrix, 75)
print(f"Первый квартиль: {q1}")
print(f"Второй квартиль: {q2}")
print(f"Третий квартиль: {q3}")
