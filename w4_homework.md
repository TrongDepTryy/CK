1. Lịch. Viết một chương trình nhận vào hai đối số dòng lệnh m và y và in ra lịch tháng cho tháng thứ m của năm y, như trong ví dụ này:

   Tháng 2 năm 2009
   CN T2 T3 T4 T5 T6 T7
    1  2  3  4  5  6  7
    8  9 10 11 12 13 14
   15 16 17 18 19 20 21
   22 23 24 25 26 27 28

2. Công thức kiểm tra sau đây được sử dụng rộng rãi bởi các ngân hàng và công ty thẻ tín dụng để xác thực số tài khoản hợp lệ:

   d0 + f(d1) + d2 + f(d3) + d4 + f(d5) + d6 + ... = 0 (mod 10)
   Các di là các chữ số thập phân của số tài khoản và f(d) là tổng các chữ số thập phân của 2d (ví dụ: f(7) = 5 vì 2 × 7 = 14 và 1 + 4 = 5). Ví dụ: 17327 là hợp lệ vì 1 + 5 + 3 + 4 + 7 = 20, là bội số của 10. Triển khai hàm f và soạn một chương trình để nhận một số nguyên 10 chữ số làm đối số dòng lệnh và in ra một số 11 chữ số hợp lệ với số nguyên đã cho là 10 chữ số đầu tiên và chữ số kiểm tra là chữ số cuối cùng.

3. Soạn một hàm max3() nhận ba đối số int hoặc float và trả về số lớn nhất.

----
<!-- ### somethings fun to do. -->

### Bài tập: Xây dựng hệ thống quản lý đơn hàng đơn giản +0.5

#### **Tiêu đề:** Xây dựng Hệ thống Quản lý Đơn hàng Đơn giản

#### **Mô tả:**

Trong bài tập này, bạn sẽ xây dựng một hệ thống quản lý đơn hàng đơn giản cho một cửa hàng trực tuyến nhỏ. Hệ thống sẽ sử dụng các hàm để thực hiện các chức năng khác nhau, áp dụng nguyên tắc phân rã và trừu tượng hóa. Bạn **không được phép sử dụng lớp (class)** mà chỉ sử dụng các hàm và cấu trúc dữ liệu đơn giản (danh sách, tuple, hoặc từ điển).

#### **Yêu cầu:**

- **Hàm `create_item(name, price, quantity)`**: Tạo một hàm nhận vào tên sản phẩm, giá sản phẩm và số lượng sản phẩm. Hàm trả về một tuple đại diện cho một mặt hàng.

- **Danh sách `Order`**: Tạo một danh sách đại diện cho đơn hàng, chứa các mặt hàng là các tuple được tạo ra từ hàm `create_item`.

- **Hàm `add_item(order, item)`**: Tạo một hàm nhận vào danh sách đơn hàng và một mặt hàng, thêm mặt hàng đó vào danh sách đơn hàng.

- **Hàm `remove_item(order, item_name)`**: Tạo một hàm nhận vào danh sách đơn hàng và tên của mặt hàng, loại bỏ mặt hàng đó khỏi đơn hàng dựa trên tên.

- **Hàm `calculate_total(order)`**: Tạo một hàm nhận vào danh sách đơn hàng và tính tổng giá trị của tất cả các mặt hàng trong đơn hàng (tổng số lượng * giá).

- **Hàm `apply_discount(order, discount_percent)`**: Tạo một hàm nhận vào danh sách đơn hàng và phần trăm giảm giá, áp dụng giảm giá cho tổng giá trị đơn hàng.

- **Hàm `is_eligible_for_free_shipping(order)`**: Tạo một hàm kiểm tra xem đơn hàng có đủ điều kiện để được miễn phí vận chuyển hay không (ví dụ: tổng giá trị đơn hàng trên $100).

- **Hàm `generate_order_summary(order)`**: Tạo một hàm trả về một chuỗi tóm tắt đơn hàng, bao gồm danh sách mặt hàng, tổng giá trị, phần trăm giảm giá và điều kiện miễn phí vận chuyển.

#### **Ví dụ hàm và Input/Output:**

1. **Hàm `create_item(name, price, quantity)`**

   ```python
   def create_item(name, price, quantity):
       return (name, price, quantity)
   ```

   Ví dụ:

   ```python
   item1 = create_item("Laptop", 1000, 1)
   item2 = create_item("Chuột", 25, 2)
   ```

2. **Hàm `add_item(order, item)`**
   - Thêm mặt hàng vào danh sách đơn hàng.

   Ví dụ:

   ```python
   order = []
   add_item(order, item1)
   add_item(order, item2)
   ```

3. **Hàm `remove_item(order, item_name)`**
   - Xóa mặt hàng khỏi đơn hàng dựa trên tên.

   Ví dụ:

   ```python
   remove_item(order, "Chuột")
   ```

4. **Hàm `calculate_total(order)`**
   - Tính tổng giá trị của các mặt hàng trong đơn hàng.

   Ví dụ:

   ```python
   total = calculate_total(order)
   print(total)
   ```

   **Input**:
   - `item1`: Laptop, $1000, số lượng: 1
   - `item2`: Chuột, $25, số lượng: 2

   **Output**: `1050`

5. **Hàm `apply_discount(order, discount_percent)`**
   - Áp dụng giảm giá cho đơn hàng.

   Ví dụ:

   ```python
   apply_discount(order, 10)
   ```

   **Input**: Giảm giá 10%  
   **Output**: Tổng sau giảm giá: `945`

6. **Hàm `is_eligible_for_free_shipping(order)`**
   - Kiểm tra xem đơn hàng có được miễn phí vận chuyển không (ví dụ: nếu tổng > $100).

   Ví dụ:

   ```python
   eligible = is_eligible_for_free_shipping(order)
   print(eligible)
   ```

   **Output**: `True` (nếu tổng > $100)

7. **Hàm `generate_order_summary(order)`**
   - Trả về chuỗi tóm tắt đơn hàng bao gồm danh sách mặt hàng, tổng giá trị, giảm giá và điều kiện miễn phí vận chuyển.

   Ví dụ:

   ```python
   summary = generate_order_summary(order)
   print(summary)
   ```

   **Output**:

   ```
   Tóm tắt đơn hàng:
   1x Laptop - $1000
   2x Chuột - $25 mỗi cái
   Tổng trước giảm giá: $1050
   Giảm giá áp dụng: 10%
   Tổng sau giảm giá: $945
   Miễn phí vận chuyển: Có
   ```

#### **Phát triển thêm độ phức tạp**

Để làm cho bài tập trở nên phức tạp hơn, có thể thêm các tính năng sau:

Sau khi tóm tắt đơn hàng sẽ hỏi thêm các tùy chọn sau đâyđây:

1. **Thêm thuế**: Tạo một hàm để tính thuế (ví dụ: 8% trên tổng giá trị).
   - Hàm: `calculate_tax(order, tax_rate)`
   - Ví dụ: `calculate_tax(order, 8)` -> Thêm thuế vào tổng giá trị đơn hàng.

2. **Phương thức vận chuyển**: Tạo thêm các phương thức vận chuyển khác nhau (ví dụ: giao hàng tiêu chuẩn, giao hàng nhanh) và tính toán chi phí vận chuyển dựa trên phương thức. Giả sử giao hàng tiêu chuẩn tốn $10 + 0.1% giá trị đơn hàng. Giao hàng nhanh tốn $18 + 0.5% giá trị đơn hàng.
   - Hàm: `calculate_shipping_cost(order, method)`
   - Ví dụ: `calculate_shipping_cost(order, 'standard')`

3. **Xử lý lỗi**: Đảm bảo rằng việc thêm/xóa mặt hàng có xử lý lỗi khi mặt hàng không tồn tại trong đơn hàng.

4. **Bán thêm bảo hiểm**: Bảo hiểm hàng 1% giá trị hàng hóa.
    - Hàm `calculate_insurance(order, insur_rate)`

5. In lại tóm tắt đơn hàng sau cùng.

<!-- +0.5 for an extraodinary idea in this homework/ 2 group per class. ****-->