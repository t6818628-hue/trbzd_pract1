import numpy as np

data_coffee = np.array([
    [245, 310, 180, 260, 290, 3500, 220, 275, 240, 310],
    [190, 265, 285, 210, 245, 300, 180, 4000, 290, 150],
    [330, 220, 275, 240, 310, 190, 265, 285, 210, 245]
])

flat_data = data_coffee.flatten()
print("Все данные:", flat_data)

mean_val = np.mean(flat_data)
print("Среднее значение:", mean_val)

median_val = np.median(flat_data)
print("Медиана:", median_val)

std_val = np.std(flat_data)
print("Стандартное отклонение:", std_val)

var_val = np.var(flat_data)
print("Дисперсия:", var_val)

max_val = np.max(flat_data)
print("Максимум:", max_val)

min_val = np.min(flat_data)
print("Минимум:", min_val)

range_val = max_val - min_val
print("Размах:", range_val)

percentiles = np.percentile(flat_data, [25, 50, 75, 90, 99])
print("Перцентили (25, 50, 75, 90, 99):", percentiles)

q1 = np.percentile(flat_data, 25)
q3 = np.percentile(flat_data, 75)
print("Первый квартиль:", q1)
print("Третий квартиль:", q3)

iqr = q3 - q1
print("Межквартильный размах:", iqr)

low_border = q1 - 1.5 * iqr
high_border = q3 + 1.5 * iqr

outliers = flat_data[(flat_data < low_border) | (flat_data > high_border)]
print("Выбросы:", outliers)

total_revenue = np.sum(flat_data)
print("Общая выручка за 60 дней:", total_revenue, "рублей")

low_days = flat_data[flat_data < 200]
print("Дни с выручкой ниже 200 рублей:", low_days)
