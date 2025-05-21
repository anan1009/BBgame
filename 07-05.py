# Dữ liệu mẫu
customers_2024 = {'Alice', 'Bob', 'Charlie', 'David', 'Emma'}
customers_2025 = {'Alice', 'Emma', 'Frank', 'Grace', 'Henry'}

kh2_nam = customers_2024 & customers_2025

kh2024 = customers_2024 - customers_2025

kh_tung_mua = customers_2024 | customers_2025

print("Khách hàng mua cả 2 năm:", kh2_nam)
print("Khách hàng chỉ mua năm 2024:", kh2024 )
print("Khách hàng mua ít nhất 1 lần trong 2 năm:", kh_tung_mua)
