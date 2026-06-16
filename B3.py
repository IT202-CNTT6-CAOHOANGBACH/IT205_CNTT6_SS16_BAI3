'''
Phân tích và thiết kế giải pháp
    Input/Output cho từng hàm:
        display_patients(patient_list)
            Input: danh sách bệnh nhân (List of Lists).
            Output: in ra màn hình danh sách bệnh nhân hoặc thông báo rỗng.
        validate_gender(gender_input)
            Input: chuỗi giới tính nhập vào.
            Output: True nếu hợp lệ ("nam"/"nu"), False nếu sai.
        add_patient(patient_list)
            Input: danh sách bệnh nhân.
            Output: cập nhật danh sách (append thêm list con mới) và in thông báo.
        find_patient_index(patient_list, patient_id)
            Input: danh sách bệnh nhân, mã BN.
         Output: trả về index nếu tìm thấy, -1 nếu không.
        update_diagnosis(patient_list)
            Input: danh sách bệnh nhân.
            Output: cập nhật chẩn đoán bệnh cho bệnh nhân theo mã BN.
        search_by_disease(patient_list)
            Input: danh sách bệnh nhân.
            Output: in danh sách bệnh nhân có bệnh chứa từ khóa và tổng số lượng.
    Giải pháp kỹ thuật:
        - Trong Python, khi truyền patient_list vào hàm, thực chất là truyền tham chiếu (reference). Nghĩa là hàm có thể thay đổi trực tiếp nội dung list gốc.
        - Do đó, cần cẩn thận khi cập nhật để không làm sai lệch dữ liệu.
        - Chuỗi (String) bất biến, nên mọi thao tác chuẩn hóa phải gán lại kết quả.
        - List (Mảng) có thể thay đổi trực tiếp bằng .append(), .remove(), .update phần tử theo index.
'''

# Triển khai code
def menu():
    print("===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
    print("1. Hiển thị danh sách bệnh nhân")
    print("2. Tiếp nhận bệnh nhân mới")
    print("3. Cập nhật chẩn đoán bệnh theo mã BN")
    print("4. Tìm kiếm và thống kê theo tên bệnh")
    print("5. Thoát chương trình")
    print("===========================================")

def display_patients(patient_list):
    if not patient_list:
        print("Hiện không có bệnh nhân nào đang điều trị.")
    else:
        print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")
        for index, value in enumerate(patient_list, start=1):
            print(f"{index}. Mã: {value[0]:<7} | Tên: {value[1]:<12} | Giới tính: {value[2]:<5} | Bệnh: {value[3]:<20}")

def validate_gender(gender_input):
    """Kiểm tra giới tính hợp lệ"""
    gender = gender_input.strip().lower()
    return gender in ["nam", "nu"]

def find_patient_index(patient_list, patient_id):
    """Tìm index bệnh nhân theo mã BN"""
    pid = patient_id.strip().upper()
    for index, value in enumerate(patient_list):
        if value[0] == pid:
            return i
    return -1

def add_patient(patient_list):
    """Tiếp nhận bệnh nhân mới"""
    print("----- TIẾP NHẬN BỆNH NHÂN MỚI -----")
    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()
    if not patient_id:
        print("Mã bệnh nhân không được để trống!")
        return
    if find_patient_index(patient_list, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip().title()
    if not name:
        print("Tên bệnh nhân không được để trống!")
        return

    gender = input("Nhập giới tính Nam/Nu: ").strip()
    while not validate_gender(gender):
        print("Giới tính không hợp lệ, vui lòng nhập lại!")
        gender = input("Nhập giới tính Nam/Nu: ").strip()
    gender = gender.strip().title()

    diagnosis = input("Nhập chẩn đoán bệnh: ").strip().capitalize()
    if not diagnosis:
        print("Chẩn đoán bệnh không được để trống!")
        return

    patient_list.append([patient_id, name, gender, diagnosis])
    print("Tiếp nhận bệnh nhân thành công!")

def update_diagnosis(patient_list):
    """Cập nhật chẩn đoán bệnh theo mã BN"""
    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")
    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()
    if not patient_id:
        print("Mã bệnh nhân không được để trống!")
        return
    index = find_patient_index(patient_list, patient_id)
    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {patient_id}!")
        return
    print(f"Tìm thấy bệnh nhân: {patient_list[index][1]}")
    print(f"Chẩn đoán hiện tại: {patient_list[index][3]}")
    new_diag = input("Nhập chẩn đoán mới: ").strip().capitalize()
    if not new_diag:
        print("Chẩn đoán bệnh không được để trống!")
        return
    patient_list[index][3] = new_diag
    print("Cập nhật chẩn đoán bệnh thành công!")

def search_by_disease(patient_list):
    """Tìm kiếm bệnh nhân theo tên bệnh"""
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")
    keyword = input("Nhập từ khóa tên bệnh: ").strip().lower()
    if not keyword:
        print("Từ khóa tìm kiếm không được để trống!")
        return
    results = [p for p in patient_list if keyword in p[3].lower()]
    if results:
        print("Kết quả tìm kiếm:")
        for index, patient in enumerate(results, start=1):
            print(f"{index}. Mã: {patient[0]} | Tên: {patient[1]} | Giới tính: {patient[2]} | Bệnh: {patient[3]}")
    else:
        print("Không tìm thấy bệnh nhân nào phù hợp.")
    print(f"Có tổng cộng {len(results)} bệnh nhân mắc bệnh liên quan đến '{keyword}'.")


def main():
    patients = [
        ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
        ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
    ]
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ").strip()

        match choice:
            case "1":
                display_patients(patients)
            case "2":
                add_patient(patients)
            case "3":
                update_diagnosis(patients)
            case "4":
                search_by_disease(patients)
            case "5":
                print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")
main()