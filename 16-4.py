def d():
    ten = input("Nhập tên của bạn: ").title()
    tuoi = int(input("Nhập tuổi của bạn: "))
    if tuoi < 18:
        print("Xin lỗi, bạn chưa đủ tuổi để đăng ký dịch vụ.")
        return
    elif tuoi > 60:
        print(f"Chào mừng {ten}! Chúng tôi gợi ý bạn sử dụng gói cao cấp .")
        return

    print("Nghề nghiệp: ")
    print("1. Học sinh")
    print("2. Sinh viên")
    print("3. Khác")
    lua_chon = input("Nhập số ")

    if lua_chon == "1":
        nghe_nghiep = "học sinh"
    elif lua_chon == "2":
        nghe_nghiep = "sinh viên"
        print(f"Chào mừng {ten}! Bạn đã nhận ưu đãi 50% vì là {nghe_nghiep}.")
    else:
        nghe = input("Nghề của bạn là:")
        
        print(f"Chào mừng {nghe} - {ten} đã đăng ký thành công gói dịch vụ của chúng tôi.")
        return
d()