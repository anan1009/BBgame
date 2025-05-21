# Yêu cầu:
# Viết hàm tự tính tổng, giá trị trung bình, tìm giá trị lớn nhất và vị trí lớn nhất.
# Không dùng sum, max, index
# Input:
# views = [145, 200, 180, 210, 90, 175, 160]


def tinh_tong_va_max(views):
    total = 0
    max_value = views[0]

    for i in range(len(views)):
        value = views[i]
        total += value
        if value > max_value:
            max_value = value
    return total, max_value

views = [145, 200, 180, 210, 90, 175, 160]
total, max_value = tinh_tong_va_max(views)
print("Tổng:", total)
print("Giá trị lớn nhất:", max_value)
