[Bài tập tuần 1](../w1/w1_homework.md)
## 💻 Bài tập - Tuần 2

<!-- https://s.cafef.vn//Ajax/PageNew/News.ashx?Symbol=pnj&NewsType=0&PageIndex=1&PageSize=2020 -->

Luyện tay:

### 1. Viết một script yêu cầu người dùng nhập vào đáy và chiều cao của tam giác và tính diện tích của tam giác đó (diện tích = 0.5 x b x h).

Ví dụ:
```python
    Nhập vào đáy: 20
    Nhập vào chiều cao: 10
    Diện tích của tam giác là 100
```

### 2. Viết một script yêu cầu người dùng nhập vào cạnh a, cạnh b, và cạnh c của tam giác. Tính chu vi của tam giác (chu vi = a + b + c).

Ví dụ:
```python
    Nhập cạnh a: 5
    Nhập cạnh b: 4
    Nhập cạnh c: 3
    Chu vi của tam giác là 12
```

### 3. Viết một script yêu cầu người dùng nhập vào số giờ và tiền công mỗi giờ. Tính tiền lương của người đó.

Ví dụ:
```python
    Nhập số giờ: 40
    Nhập tiền công mỗi giờ: 28
    Thu nhập hàng tuần của bạn là 1120
```

### 4. Viết một script yêu cầu người dùng nhập vào số năm đã sống. Tính số giây mà người đó có thể sống. Giả sử một người có thể sống 100 năm.

Ví dụ:
```python
    Nhập số năm bạn đã sống: 100
    Bạn đã sống 3153600000 giây.
```

### 5. Viết một script Python hiển thị bảng sau

```python
    1 1 1 1 1
    2 1 2 4 8
    3 1 3 9 27
    4 1 4 16 64
    5 1 5 25 125
```

------------------------------

Đặt tên file bài tập tập theo định dạng như tuần 1, với mỗi câu làm riêng 1 file thêm .[số câu]

ví dụ:

[tên bài].1
[tên bài].2

1. Một sinh viên vật lý nhận được kết quả không mong muốn khi sử dụng mã sau để tính toán:

```python
force = G * mass1 * mass2 / radius * radius
```
theo công thức 
$
F = \frac{G \cdot m1 \cdot m2}{r^2}
$

Hãy sửa lỗi trên và viết lại vào file bài tập.

### Ngày trong tuần

2. Hãy viết một chương trình nhận vào một ngày và in ra ngày trong tuần mà ngày đó rơi vào. Chương trình của bạn nên nhận ba tham số dòng lệnh: `m` (tháng), `d` (ngày), và `y` (năm). Đối với `m`, sử dụng 1 cho tháng Giêng, 2 cho tháng Hai, và tương tự. Đối với kết quả, in ra 0 cho Chủ nhật, 1 cho Thứ Hai, 2 cho Thứ Ba, và tiếp tục như vậy. Sử dụng các [công thức sau cho lịch Gregorian](https://www.tondering.dk/claus/cal/julperiod.php):


$$
\begin{align}
 y_0 &= y - \frac{14 - m}{12} \\
x &= y_0 + \frac{y_0}{4} - \frac{y_0}{100} + \frac{y_0}{400} \\
m_0 &= m + 12 \times \left(\frac{14 - m}{12}\right) - 2 \\
d &= \left(d + x + \frac{31 \times m_0}{12}\right) \mod 7 \\
\end{align}
$$

Ví dụ, ngày 2 tháng 8 năm 1953 là ngày nào trong tuần?

$$
\begin{align}
y = 1953 - 0 = 1953 \\
x = 1953 + \frac{1953}{4} - \frac{1953}{100} + \frac{1953}{400} = 2426 \\
m = 8 + 12 \times 0 - 2 = 6 \\
d = \left(2 + 2426 + \frac{31 \times 6}{12}\right) \mod 7 = 2443 \mod 7 = 0 \text{ (Chủ nhật)} \\
\end{align}
$$


### Chuyển đổi màu sắc

3. Có nhiều định dạng khác nhau được sử dụng để biểu diễn màu sắc. Ví dụ, định dạng chính cho màn hình LCD, máy ảnh kỹ thuật số và trang web, được gọi là định dạng RGB, xác định mức độ của đỏ (R), xanh lá cây (G), và xanh dương (B) trên thang điểm từ 0 đến 255. Định dạng chính cho xuất bản sách và tạp chí, được gọi là định dạng CMYK, xác định mức độ của xanh lơ (C), đỏ tươi (M), vàng (Y), và đen (K) trên thang điểm từ 0.0 đến 1.0. Hãy viết một chương trình chuyển đổi từ RGB sang CMYK. Chương trình nhận vào ba số nguyên `r`, `g`, và `b` từ dòng lệnh và in ra các giá trị CMYK tương đương. Nếu các giá trị RGB đều bằng 0, thì các giá trị CMY đều bằng 0 và giá trị K bằng 1; ngược lại, sử dụng các công thức sau:

$$
\begin{align}
w = \max\left(\frac{r}{255}, \frac{g}{255}, \frac{b}{255}\right) \\
c = \frac{w - \frac{r}{255}}{w} \\
m = \frac{w - \frac{g}{255}}{w} \\
y = \frac{w - \frac{b}{255}}{w} \\
k = 1 - w \\
\end{align}
$$


### Lãi suất kép liên tục

4. Hãy viết một chương trình tính toán và in ra số tiền bạn sẽ có nếu bạn đầu tư với một lãi suất nhất định được tính theo lãi suất kép liên tục. Chương trình sẽ nhận vào số năm `t`, số tiền gốc `P`, và lãi suất hàng năm `r` dưới dạng tham số dòng lệnh. Giá trị mong muốn được tính theo công thức:

$
A = P \cdot e^{r \cdot t}
$

Trong đó:
- `A` là số tiền sau thời gian `t` năm.
- `P` là số tiền gốc ban đầu.
- `r` là lãi suất hàng năm (dưới dạng số thập phân, ví dụ: 0.05 cho 5%).
- `t` là số năm.
- `e` là cơ số của logarit tự nhiên (khoảng 2.71828).