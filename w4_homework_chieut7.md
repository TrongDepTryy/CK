1. Cho hai vector có độ dài n được biểu diễn bằng mảng một chiều (list), hãy viết một đoạn mã tính khoảng cách Euclid giữa chúng (là căn bậc hai của tổng các bình phương của hiệu giữa các phần tử tương ứng).
2. Tìm phần tử trùng lặp. Cho một mảng có n phần tử với mỗi phần tử nằm trong khoảng từ 1 đến n, hãy viết một đoạn mã để xác định xem có phần tử nào bị trùng lặp hay không.

---

### Bài tập 1: **Phân tích đơn hàng**
Cho một danh sách các đơn hàng từ một cửa hàng thương mại điện tử, mỗi đơn hàng là một `tuple` gồm (Mã đơn hàng, Tên khách hàng, Tổng giá trị đơn hàng). Hãy viết một chương trình sử dụng `list` và `dict` để:
1. Tạo một `dict` để lưu tổng số đơn hàng và tổng giá trị đơn hàng của từng khách hàng.
2. Xuất ra khách hàng nào có tổng giá trị đơn hàng cao nhất và thấp nhất.

**Dữ liệu mẫu:**
```python
orders = [
    ("ORD001", "Alice", 250),
    ("ORD002", "Bob", 150),
    ("ORD003", "Alice", 300),
    ("ORD004", "Charlie", 500),
    ("ORD005", "Bob", 200)
]
```

---

### Bài tập 2: **Hệ thống quản lý sản phẩm**
Bạn quản lý một kho hàng trực tuyến. Mỗi sản phẩm có một mã sản phẩm (ID), tên sản phẩm, và giá tiền. Sử dụng `dict` để quản lý danh sách các sản phẩm và `tuple` để lưu thông tin sản phẩm (tên, giá tiền). Viết chương trình để:
1. Thêm sản phẩm mới vào kho.
2. Cập nhật giá sản phẩm.
3. Xóa sản phẩm khỏi kho.
4. In ra danh sách sản phẩm hiện có trong kho.

---

### Bài tập 3: **Phân tích danh mục khách hàng**
Trong hệ thống thương mại điện tử, mỗi khách hàng có thể thuộc vào một hay nhiều danh mục khách hàng (Ví dụ: "VIP", "Mới", "Thường xuyên"). Dùng `set` để lưu các danh mục này. Viết chương trình để:
1. Tạo danh sách khách hàng và các danh mục của họ.
2. Kiểm tra xem khách hàng có nằm trong một danh mục cụ thể hay không.
3. Tìm ra những khách hàng nào thuộc nhiều nhất 3 danh mục.

---

### Bài tập 4: **Phân tích số liệu bán hàng**
Một công ty kinh doanh trực tuyến theo dõi lượng sản phẩm bán được hàng tháng. Sử dụng `dict` với `list` để lưu trữ số liệu bán hàng theo tháng cho mỗi sản phẩm. Hãy viết chương trình để:
1. Tính tổng doanh số của mỗi sản phẩm.
2. Xác định sản phẩm nào có mức tăng trưởng doanh số lớn nhất trong các tháng liên tiếp.
3. Tìm sản phẩm có doanh số cao nhất trong tháng bất kỳ.

**Dữ liệu mẫu:**
```python
sales_data = {
    "Product A": [100, 150, 200, 250],
    "Product B": [300, 320, 330, 290],
    "Product C": [50, 60, 70, 80]
}
```

---

### Bài tập 5: **Phân tích khách hàng trùng lặp**
Cửa hàng thương mại điện tử có hai danh sách khách hàng từ hai chiến dịch quảng cáo khác nhau, mỗi danh sách là một `set` chứa tên khách hàng. Viết chương trình để:
1. Tìm danh sách khách hàng chung từ cả hai chiến dịch.
2. Tìm danh sách khách hàng chỉ tham gia vào chiến dịch đầu tiên nhưng không tham gia chiến dịch thứ hai.
3. Kiểm tra xem danh sách khách hàng của hai chiến dịch có hoàn toàn giống nhau không.

**Dữ liệu mẫu:**
```python
campaign1_customers = {"Alice", "Bob", "Charlie", "David"}
campaign2_customers = {"Charlie", "Eve", "Alice", "Frank"}
```

---

### Bài tập 6: **Hệ thống chấm điểm khách hàng**
Công ty có chương trình khách hàng thân thiết, với các khách hàng được tính điểm dựa trên giá trị mua hàng. Mỗi khách hàng có thể có nhiều giao dịch, và số điểm tích lũy dựa trên tổng giá trị giao dịch của họ. Sử dụng `dict` để quản lý thông tin khách hàng và `tuple` để lưu từng giao dịch (ngày, giá trị giao dịch). Viết chương trình để:
1. Cập nhật điểm khách hàng dựa trên giá trị giao dịch.
2. Tìm khách hàng có số điểm cao nhất.
3. Xóa giao dịch cũ nhất của một khách hàng nếu cần.

---

### Bài tập 7: **Quản lý giỏ hàng**
Một hệ thống quản lý giỏ hàng của người dùng thương mại điện tử. Mỗi người dùng có thể có nhiều sản phẩm trong giỏ hàng, mỗi sản phẩm có số lượng khác nhau. Sử dụng `dict` để lưu giỏ hàng của mỗi người dùng và `tuple` để lưu thông tin sản phẩm (mã sản phẩm, số lượng). Viết chương trình để:
1. Thêm sản phẩm vào giỏ hàng.
2. Xóa sản phẩm khỏi giỏ hàng.
3. Kiểm tra tổng số sản phẩm có trong giỏ hàng của một người dùng.
4. Kiểm tra xem một người dùng có một sản phẩm cụ thể trong giỏ hàng hay không.

---

### Bài tập 8: **Phân tích dữ liệu giá sản phẩm**
Bạn có một danh sách sản phẩm với giá trong nhiều đợt khuyến mãi khác nhau, lưu trữ trong một `dict`, với mỗi sản phẩm có một danh sách các mức giá trong `list`. Viết chương trình để:
1. Tìm mức giá trung bình của mỗi sản phẩm.
2. Xác định sản phẩm có giá giảm nhiều nhất qua các đợt khuyến mãi.
3. Sắp xếp sản phẩm theo mức giá cao nhất của chúng.

**Dữ liệu mẫu:**
```python
product_prices = {
    "Laptop": [1000, 900, 850, 800],
    "Smartphone": [700, 650, 600, 550],
    "Tablet": [400, 380, 370, 360]
}
```

---