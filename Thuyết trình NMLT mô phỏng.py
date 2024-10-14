#Def đăng ký thông tin khách hàng, tạo mã qr riêng cho khách hàng
import qrcode
import uuid
def register_customer(name, phone, address,diem,tong,hangmuc):
    customer_id = str(uuid.uuid4())
    customer_info = {
        'id': customer_id,
        'ten': name,
        'dienthoai': phone,
        'diachi': address,
        'Diem':diem,
        'tongchitieu':tong,
        'hangmuc':hangmuc
    }
    print(f"Đăng ký thành công! ID khách hàng: {customer_id}")
    qr = qrcode.make(customer_info)
    qr.save(f"{customer_id}.png")
    print(f"Mã QR đã được tạo cho {name} và lưu dưới dạng {customer_id}.png")   
    return customer_info


#Chạy hàm tạo QR
ho_ten1=str(input('Nhập tên khách hàng: '))
so_dien_thoai1=str(input('Số điện thoại: '))
dia_chi1=str(input('Địa chỉ: '))
diem = 0
tong_chi_tieu = 0
hang_muc = "Member"
customer = register_customer(ho_ten1,so_dien_thoai1,dia_chi1,diem,tong_chi_tieu,hang_muc)

def record_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


#Máy quét QR
import cv2
from pyzbar.pyzbar import decode
# conda install -c conda-forge pyzbar
from datetime import datetime
def scan_qr_code():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        for barcode in decode(frame):
            qr_data = barcode.data.decode('utf-8')
            print(f"QR Code data: {qr_data}")
            cap.release()
            cv2.destroyAllWindows()
            return qr_data
        cv2.imshow('QR Code Scanner', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
print(f"Thời gian đăng kí: {record_timestamp()}")


# Giả lập quét mã QR và tích điểm
qr_data = scan_qr_code()
if qr_data:
    customer_data = eval(qr_data) 

    from datetime import datetime, timedelta
    diem = 0
    tong_chi_tieu = 0
    hang_muc = "Member"

# Hàm tính điểm theo hạng mục hiện tại
    def tinh_diem(don_hang, ngay_thang):
        global diem, tong_chi_tieu, hang_muc

        diem_cu = diem  # Lưu điểm trước đó để so sánh
        if hang_muc == "Diamond":
            diem += (don_hang // 1000) * 5
        elif hang_muc == "Platinum":
            diem += (don_hang // 1000) * 4
        elif hang_muc == "Gold":
            diem += (don_hang // 1000) * 3
        elif hang_muc == "Silver":
            diem += (don_hang // 1000) * 2
        else:
            diem += don_hang // 1000
        tong_chi_tieu += don_hang

    # Hiển thị thông tin đơn hàng
        print(f"Ngày: {ngay_thang.strftime('%Y-%m-%d')}")
        print(f"Tổng tiền thanh toán đơn hàng: {don_hang}")
        print(f"Điểm đã tích lũy: {diem_cu} → {diem}")
        print(f"Tổng chi tiêu trong tháng: {tong_chi_tieu}")
        print(f"Hạng mục hiện tại: {hang_muc}")
        print("-" * 30)

# Hàm cập nhật hạng mục dựa trên tổng chi tiêu hiện tại
    def cap_nhat_hang_muc():
        global tong_chi_tieu, hang_muc

        if tong_chi_tieu >= 4000000:
            hang_muc = "Diamond"
        elif hang_muc == "Platinum" and tong_chi_tieu >= 4000000:
            hang_muc = "Diamond"
        elif hang_muc == "Gold":
            if tong_chi_tieu >=4000000:
                hang_muc = "Diamond"
            if tong_chi_tieu >=3000000:
                hang_muc = "Platinum"
        elif hang_muc == "Silver":
            if tong_chi_tieu >=4000000:
                hang_muc = "Diamond"
            if tong_chi_tieu >=3000000:
                hang_muc = "Platinum"
            if tong_chi_tieu >=2000000:
                hang_muc="Gold"            
        else:
            if tong_chi_tieu >=4000000:
                hang_muc = "Diamond"
            if tong_chi_tieu >=3000000:
                hang_muc = "Platinum"
            if tong_chi_tieu >=2000000:
                hang_muc="Gold"
            if tong_chi_tieu >=1000000:
                hang_muc="Silver"
        print(f"Hạng mục sau khi cập nhật: {hang_muc}")
        print("-" * 30)

# Hàm tự động reset chi tiêu và cập nhật hạng mục sau mỗi tháng
    def cap_nhat_theo_thang(ngay_hien_tai, ngay_bat_dau):
        global tong_chi_tieu, hang_muc
        so_thang_da_qua = (ngay_hien_tai.year - ngay_bat_dau.year) * 12 + (ngay_hien_tai.month - ngay_bat_dau.month)
        if so_thang_da_qua >= 1:
            print(f"Đã qua {so_thang_da_qua} tháng, reset tổng chi tiêu và cập nhật hạng mục.")

        # Kiểm tra tổng chi tiêu của tháng trước đó và giữ nguyên hạng mục hiện tại
            tong_chi_tieu_thang_truoc = tong_chi_tieu  # Lưu tổng chi tiêu tháng trước khi reset
            tong_chi_tieu = 0  # Reset tổng chi tiêu cho tháng mới

        # Hạng mục chỉ thay đổi nếu tổng chi tiêu của tháng trước không đủ duy trì hạng mục hiện tại
            if tong_chi_tieu_thang_truoc < 1000000:
                hang_muc = "Member"
            elif tong_chi_tieu_thang_truoc < 2000000:
                hang_muc = "Silver"
            elif tong_chi_tieu_thang_truoc < 3000000:
                hang_muc = "Gold"
            elif tong_chi_tieu_thang_truoc < 4000000:
                hang_muc = "Platinum"
            else:
                hang_muc = "Diamond"
            print(f"Hạng mục sau khi cập nhật: {hang_muc}")
            print("-" * 30)

# Ngày bắt đầu tích điểm
    ngay_bat_dau = datetime(2024,10, 6)

# Tích điểm và cập nhật hạng mục theo từng đơn hàng
    don_hang_1 = 1500000
    ngay_1 = datetime(2024, 10, 19)
    tinh_diem(don_hang_1, ngay_1)
    cap_nhat_hang_muc()

    don_hang_2 = 500000
    ngay_2 = datetime(2024, 10, 21)
    tinh_diem(don_hang_2, ngay_2)
    cap_nhat_hang_muc()

# Kiểm tra và reset theo từng tháng
    ngay_cap_nhat = datetime(2024, 11, 6)
    cap_nhat_theo_thang(ngay_cap_nhat, ngay_bat_dau)

# Đơn hàng mua sau khi cập nhật (sau ngày 6/10/2024)
    don_hang_3 = 400000
    ngay_3 = datetime(2024, 11, 10)
    tinh_diem(don_hang_3, ngay_3)
    cap_nhat_hang_muc()

# Kiểm tra và reset sau tháng thứ hai (27/11/2024)
    ngay_cap_nhat_2 = datetime(2024, 12, 6)
    cap_nhat_theo_thang(ngay_cap_nhat_2, ngay_bat_dau)

# Đơn hàng vào tháng tiếp theo
    don_hang_4 = 500000
    ngay_4 = datetime(2024, 12, 12)
    tinh_diem(don_hang_4, ngay_4)
    cap_nhat_hang_muc()
#Điểm của khách hàng lúc này là diem=4200


    from datetime import datetime, timedelta
#Các voucher mặc định trên app
    voucher1 = 10000
    voucher2 = 20000
    voucher3 = 50000
    voucher4 = 100000
    voucher5 = 200000
    voucher6 = 500000


# Tạo biến lưu thông tin về các voucher đã đổi và thời gian hết hạn
    voucher_da_doi = {}


# Hàm để quy đổi điểm lấy voucher
    def doivoucher(voucher, ngay_doi):
        global diem
    # Kiểm tra xem đủ điều kiện đổi voucher hay không
        if voucher == voucher1 and diem >= 2000:
            diem -= 2000
            voucher_da_doi["voucher1"] = ngay_doi + timedelta(days=7)
            print(f"Đã đổi được voucher1, bạn còn {diem} điểm")
        elif voucher == voucher2 and diem >= 4000:
            diem -= 4000
            voucher_da_doi["voucher2"] = ngay_doi + timedelta(days=7)
            print(f"Đã đổi được voucher2, bạn còn {diem} điểm")
        elif voucher == voucher3 and diem >= 10000:
            diem -= 10000
            voucher_da_doi["voucher3"] = ngay_doi + timedelta(days=7)
            print(f"Đã đổi được voucher3, bạn còn {diem} điểm")
        elif voucher == voucher4 and diem >= 20000:
            diem -= 20000
            voucher_da_doi["voucher4"] = ngay_doi + timedelta(days=7)
            print(f"Đã đổi được voucher4, bạn còn {diem} điểm")
        elif voucher == voucher5 and diem >= 40000:
            diem -= 40000
            voucher_da_doi["voucher5"] = ngay_doi + timedelta(days=7)
            print(f"Đã đổi được voucher5, bạn còn {diem} điểm")
        elif voucher == voucher6 and diem >= 100000:
            diem -= 100000
            voucher_da_doi["voucher6"] = ngay_doi + timedelta(days=7)
            print(f"Đã đổi được voucher6, bạn còn {diem} điểm")
        else:
            print("Không đủ điểm để đổi voucher này.")

# Hàm để sử dụng voucher trong đơn hàng
    def dungvoucher(voucher, don_hang, ngay_dung):
    # Kiểm tra xem voucher còn hạn 
        #Trường hợp 1
        if voucher == voucher1 and "voucher1" in voucher_da_doi and ngay_dung <= voucher_da_doi["voucher1"]:
            tong_thanh_toan = don_hang - voucher1
            print(f"Tổng thanh toán sau khi dùng voucher1: {tong_thanh_toan}")


        elif voucher == voucher2 and "voucher2" in voucher_da_doi and ngay_dung <= voucher_da_doi["voucher2"]:
            tong_thanh_toan = don_hang - voucher2
            print(f"Tổng thanh toán sau khi dùng voucher2: {tong_thanh_toan}")
        elif voucher == voucher3 and "voucher3" in voucher_da_doi and ngay_dung <= voucher_da_doi["voucher3"]:
            tong_thanh_toan = don_hang - voucher3
            print(f"Tổng thanh toán sau khi dùng voucher3: {tong_thanh_toan}")
        elif voucher == voucher4 and "voucher4" in voucher_da_doi and ngay_dung <= voucher_da_doi["voucher4"]:
            tong_thanh_toan = don_hang - voucher4
            print(f"Tổng thanh toán sau khi dùng voucher4: {tong_thanh_toan}")
        elif voucher == voucher5 and "voucher5" in voucher_da_doi and ngay_dung <= voucher_da_doi["voucher5"]:
            tong_thanh_toan = don_hang - voucher5
            print(f"Tổng thanh toán sau khi dùng voucher5: {tong_thanh_toan}")
        elif voucher == voucher6 and "voucher6" in voucher_da_doi and ngay_dung <= voucher_da_doi["voucher6"]:
            tong_thanh_toan = don_hang - voucher6
            print(f"Tổng thanh toán sau khi dùng voucher6: {tong_thanh_toan}") 

        #Trường hợp 2
        elif voucher == voucher1 and ngay_dung > voucher_da_doi.get("voucher1", ngay_dung):
            print("Voucher1 đã hết hạn dùng")
            tong_thanh_toan = don_hang
            print(f"Tổng thanh toán : {tong_thanh_toan}")


        elif voucher == voucher2 and ngay_dung > voucher_da_doi.get("voucher2", ngay_dung):
            print("Voucher2 đã hết hạn dùng")
            tong_thanh_toan = don_hang
            print(f"Tổng thanh toán : {tong_thanh_toan}")
        elif voucher == voucher3 and ngay_dung > voucher_da_doi.get("voucher3", ngay_dung):
            print("Voucher3 đã hết hạn dùng")
            tong_thanh_toan = don_hang
            print(f"Tổng thanh toán : {tong_thanh_toan}")
        elif voucher == voucher4 and ngay_dung > voucher_da_doi.get("voucher4", ngay_dung):
            print("Voucher4 đã hết hạn dùng")
            tong_thanh_toan = don_hang
            print(f"Tổng thanh toán : {tong_thanh_toan}")
        elif voucher == voucher5 and ngay_dung > voucher_da_doi.get("voucher5", ngay_dung):
            print("Voucher5 đã hết hạn dùng")
            tong_thanh_toan = don_hang
            print(f"Tổng thanh toán : {tong_thanh_toan}")
        elif voucher == voucher6 and ngay_dung > voucher_da_doi.get("voucher6", ngay_dung):
            print("Voucher6 đã hết hạn dùng")
            tong_thanh_toan = don_hang
            print(f"Tổng thanh toán : {tong_thanh_toan}")
        else:
            print("Voucher không hợp lệ hoặc đã hết hạn.")

#Ví dụ 1:
    ngay_doi = datetime(2024, 11, 12)
    doivoucher(voucher1, ngay_doi)  # Đổi voucher1
    print("-" * 30)
# Ví dụ sử dụng: Khách hàng dùng voucher1 vào ngày 7/11/2024 để mua đơn hàng trị giá 500000
    ngay_dung = datetime(2024, 11, 16)
    don_hang = 500000
    dungvoucher(voucher1, don_hang, ngay_dung)  # Dùng voucher1
    print("-" * 30)
# Ví dụ 2: Khách hàng đổi và dùng voucher1 sau khi voucher đã hết hạn vào ngày 21/11/2024
    ngay_doi = datetime(2024, 11, 13)
    doivoucher(voucher1, ngay_doi)

    ngay_dung = datetime(2024, 11, 21)
    donhang =100000
    dungvoucher(voucher1, donhang, ngay_dung)  # Dùng voucher1 đã hết hạn
    print("-" * 30)

    
#Khi bạn đặt hàng online, đây sẽ là cách để tính khoảng cách coi bạn có nằm trong bán kính 5km hay không để free ship   
    from geopy.distance import geodesic
# Tọa độ từ các liên kết Google Maps
    coords_1 = (10.8221589, 106.6868454)  # Trường Đại học Công nghiệp TP.HCM
    coords_2 = (10.8231406, 106.6934509)  # Emart Phan Văn Trị

# Hàm tính khoảng cách giữa hai tọa độ
    def tinh_khoang_cach(coords_a, coords_b):
        return geodesic(coords_a, coords_b).kilometers

# Tính khoảng cách giữa hai địa chỉ
    khoang_cach = tinh_khoang_cach(coords_1, coords_2)
    print(f"Khoảng cách từ Trường Đại học Công nghiệp TP.HCM đến Emart Phan Văn Trị là {khoang_cach:.2f} km.")
    print("-" * 30)


# Hàm tính tổng thanh toán bao gồm phí ship
    def tinh_tong_thanh_toan(donhang, phiship, khoangcach, hangmuc):
        if hangmuc == "Member" or hangmuc == "Silver":
            if khoangcach <= 5 and donhang >= 500000:
                phiship -= 35000
        elif hangmuc == "Gold" or hangmuc == "Platinum" or hangmuc == "Diamond":
            if khoangcach <= 5:
                phiship = 0
    # Đảm bảo phí ship không âm
        phiship = max(phiship, 0)

    # Tính tổng thanh toán
        tongthanhtoan = donhang + phiship
        return tongthanhtoan



# Hạng mục của khách hàng lúc nãy là hang_muc = Member
    donhang = 600000
    phiship_ = 40000
    tongthanhtoan = tinh_tong_thanh_toan(donhang, phiship_, khoang_cach, hang_muc)
    print(f"Tổng thanh toán: {tongthanhtoan} đồng")
    print("-" * 30)


    from datetime import datetime
#Onelife tạo mã giảm giá khuyến mãi khách hàng
    ma_hop_le = "XHNGH"
    giam_gia = 50000
    ngay_phat_hanh = datetime(2024, 10, 27)
    ngay_ket_thuc = datetime(2024, 11, 6)

# Hàm kiểm tra và áp dụng mã khuyến mãi
    def ap_dung_ma_khuyen_mai(tongthanhtoan, ma_khuyen_mai, ngay_su_dung):
    # Kiểm tra nếu mã hợp lệ và trong thời hạn sử dụng
        if ma_khuyen_mai == ma_hop_le and ngay_phat_hanh <= ngay_su_dung <= ngay_ket_thuc:
            tongthanhtoan -= giam_gia
            print(f"Mã {ma_khuyen_mai} đã được áp dụng, giảm {giam_gia} đồng.")
        else:
            print(f"Mã {ma_khuyen_mai} không hợp lệ hoặc đã hết hạn.")
        return max(tongthanhtoan, 0)

# Ví dụ sử dụng
    tongthanhtoan_homnay = 500000
    ngay_su_dung = datetime(2024, 11, 1)
# Tính lại tổng thanh toán sau khi áp dụng mã khuyến mãi
    tongthanhtoan = ap_dung_ma_khuyen_mai(tongthanhtoan_homnay, "XHNGH", ngay_su_dung)
    print(f"Tổng thanh toán sau khi áp dụng khuyến mãi: {tongthanhtoan} đồng")
    print("-" * 30)


#Kỷ niệm thành viên
    from datetime import timedelta
# Hàm kỷ niệm thành viên
    def ky_niem_thanh_vien(ngay_dang_ky, ngay_hien_tai, diem):
    # Cộng 10.000 điểm nếu đến ngày kỷ niệm 1 năm
        if ngay_hien_tai == ngay_dang_ky + timedelta(days=365):
            diem += 10000
            print("Chúc mừng bạn đã kỷ niệm 1 năm thành viên, bạn đã được cộng 10.000 điểm!")
    
        return diem

# Ví dụ sử dụng
# Điểm lúc nãy sau khi đổi voucher của khách hàng Tân còn diem=200 và ngày bắt đầu là ngày 6/10/2024
    ngay_hien_tai = datetime(2025, 10, 6)

# Cộng điểm vào ngày kỷ niệm thành viên
    diem = ky_niem_thanh_vien(ngay_bat_dau, ngay_hien_tai, diem)
    print(f"Số điểm hiện tại của bạn là: {diem} điểm")
