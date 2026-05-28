# BÀI TẬP VẬN DỤNG CƠ BẢN 2
# Yêu cầu: 1. Phân tích lỗi  2. Sửa lỗi

# 1. Phân tích lỗi
# - Biến total_students đặt sai vị trí, không reset về 0 khi sang chi nhánh mới.
# - Dẫn đến cộng dồn sai tổng học viên giữa các chi nhánh.

# 2. Sửa lỗi

so_chi_nhanh = 3
so_lop = 3

students = [
    [30, 25, 28],  # Chi nhánh 1
    [20, 22, 18],  # Chi nhánh 2
    [35, 32, 30]   # Chi nhánh 3
]

for i in range(so_chi_nhanh):
    total_students = 0  # reset về 0 cho mỗi chi nhánh
    for j in range(so_lop):
        total_students += students[i][j]
    print(f"Chi nhánh {i+1}: {total_students} học viên")
