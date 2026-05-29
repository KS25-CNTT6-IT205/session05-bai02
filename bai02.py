# Lỗi hệ thống xảy ra do vị trí khởi tạo biến total_students. Trong đoạn legacy code, biến này được đặt bằng 0 ở bên ngoài vòng 
# lặp duyệt chi nhánh (outer loop). Vì không được đặt lại (reset) sau khi kết thúc một vòng lặp chi nhánh, nó tiếp tục mang giá 
# trị cũ để cộng dồn với dữ liệu của các chi nhánh tiếp theo.

# Vì sao Chi nhánh 1 hiển thị đúng là 83 học viên:
# Khi chương trình bắt đầu, total_students được khởi tạo đúng bằng 0.
# Nhập số liệu lớp học chi nhánh 1: total_students = 0 + 30 + 25 + 28 = 83.
# Kết quả in ra là 83 (Chính xác).

# Vì sao Chi nhánh 2 đúng là 60 nhưng hệ thống hiển thị 143 học viên:
# Khi vòng lặp chuyển sang chi nhánh 2, hệ thống không reset biến tổng. Giá trị của nó vẫn đang là 83 (lưu từ chi nhánh 1).
# Nhập số liệu lớp học chi nhánh 2: total_students = 83 + 20 + 22 + 18 = 143.
# Kết quả in ra bị cộng dồn thành 143.

# Vì sao Chi nhánh 3 đúng là 97 nhưng hệ thống hiển thị 240 học viên:
# Tương tự, biến tổng tiếp tục mang giá trị 143 từ bước trước đó sang chi nhánh 3.
# Nhập số liệu lớp học chi nhánh 3: total_students = 143 + 35 + 32 + 30 = 240.
# Kết quả in ra bị cộng dồn sai thành 240.

branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))
for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}")
    total_students = 0 
    for classroom in range(1, class_count + 1):
        student_count = int(input(f"Nhập số học viên lớp {classroom}: "))
        total_students += student_count
    print(f"Chi nhánh {branch}: {total_students} học viên")