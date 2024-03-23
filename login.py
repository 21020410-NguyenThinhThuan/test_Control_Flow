def login():
    username = input("Tên đăng nhập: ")
    password = input("Mật khẩu: ")

    # Kiểm tra tên đăng nhập và mật khẩu
    if username == "admin" and password == "12345":
        return "Đăng nhập thành công!"
    else:
        return "Đăng nhập thất bại. Vui lòng đăng nhập lại."

if __name__ == "__main__":
    login()