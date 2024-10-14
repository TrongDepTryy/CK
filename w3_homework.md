## Bài tập lập trình Python

### Bài tập cơ bản

1. **So sánh ba số nguyên:** Viết chương trình nhận ba số nguyên từ tham số dòng lệnh và in ra "bằng nhau" nếu cả ba số bằng nhau, ngược lại in ra "không bằng nhau".

2. **Giải phương trình bậc hai:** Viết chương trình giải phương trình bậc hai dạng ax<sup>2</sup> + bx + c = 0 với a, b, c là các số thực nhập từ bàn phím. Chương trình cần xử lý các trường hợp đặc biệt như:

    - a = 0: phương trình trở thành phương trình bậc nhất.
    - Δ < 0: phương trình vô nghiệm.
    - Δ = 0: phương trình có nghiệm kép.

3. **Kiểm tra số thực trong khoảng (0, 1):** Viết một đoạn mã nhận hai số thực từ tham số dòng lệnh và in ra True nếu cả hai số đều nằm trong khoảng (0, 1) và False trong trường hợp ngược lại.

4. **Cải thiện bài toán "wind chill":** Cải thiện chương trình tính "wind chill" trong thư mục w3 bằng cách thêm mã để kiểm tra xem các giá trị của tham số dòng lệnh có nằm trong khoảng giá trị hợp lệ của công thức hay không và thêm mã để in thông báo lỗi nếu không phải như vậy.

### Bài tập vòng lặp

5. **Tính giá trị của j:** Cho biết giá trị của biến j sau khi mỗi đoạn mã sau được thực thi:

    a. 
    ```python
    j = 0
    for i in range(0, 10):
        j += i
    ```

    b. 
    ```python
    j = 1
    for i in range(0, 10):
        j += j
    ```

    c. 
    ```python
    for j in range(0, 10):
        j += j
    ```

6. **In dòng chữ "Hello":** Viết chương trình in dòng chữ "Hello" từ tham số nhập vào. Giả sử tham số nhỏ hơn 1000.

7. **In số nguyên theo dòng:** Viết chương trình sử dụng một vòng lặp `for` và một câu lệnh `if` để in các số nguyên từ 1000 (bao gồm) đến 2000 (không bao gồm) với năm số nguyên trên mỗi dòng.

8. **Số ngẫu nhiên:** Viết chương trình nhận một số nguyên n làm tham số dòng lệnh, sử dụng `random.random()` để tạo ra n số ngẫu nhiên đều trong khoảng từ 0 đến 1, sau đó in ra giá trị trung bình, giá trị nhỏ nhất và giá trị lớn nhất của chúng.

10. **Bảng giá trị hàm:** Viết chương trình in ra bảng giá trị của log n, n, n log n, n<sup>2</sup> và n<sup>3</sup> với n = 2, 4, 8, 16, 32, 64, 128. Sử dụng tab (`\t`) để căn chỉnh các cột.

11. **Đảo ngược chữ số:** Cho biết giá trị của m và n sau khi đoạn mã sau được thực thi:

```python
n = 123456789
m = 0
while n != 0:
    m = (10 * m) + (n % 10)
    n //= 10
```

12. **Dãy Fibonacci:** Viết chương trình in 100 số đầu tiên của dãy số fibonacci ra màn hình.

13. **Lũy thừa của 2:** Viết chương trình nhận một tham số dòng lệnh n và in ra tất cả các lũy thừa của 2 nhỏ hơn hoặc bằng n. Đảm bảo rằng chương trình của bạn hoạt động chính xác cho tất cả các giá trị của n. (Chương trình của bạn sẽ không in ra gì nếu n là số âm hoặc bằng 0).

14. **Tính tổng nghịch đảo bình phương:** Không giống như dãy số điều hòa, tổng 1/1<sup>2</sup> + 1/2<sup>2</sup> + ... + 1/n<sup>2</sup> hội tụ về một hằng số khi n tiến đến vô cùng. (Thực tế, hằng số đó là π<sup>2</sup>/6, vì vậy công thức này có thể được sử dụng để ước tính giá trị của π.) Vòng lặp `for` nào sau đây tính toán tổng này? Giả sử n là số nguyên 1000000 và total là một số float được khởi tạo bằng 0.0.

    a. 
    ```python
    for i in range(1, n+1):
        total += 1 / (i*i)
    ```

    b. 
    ```python
    for i in range(1, n+1):
        total += 1.0 / i*i
    ```

    c. 
    ```python
    for i in range(1, n+1):
        total += 1.0 / (i*i)
    ```

    d. 
    ```python
    for i in range(1, n+1):
        total += 1 / (1.0*i*i)
    ```

15. **Chuyển đổi cơ số:** Tạo chương trình nhận i và k làm tham số dòng lệnh và chuyển đổi i sang cơ số k. Giả sử k là một số nguyên từ 2 đến 16. Đối với cơ số lớn hơn 10, sử dụng các chữ cái từ A đến F để biểu thị các chữ số từ 11 đến 16. Với số nhập vào từ người dùng.

16. **Biểu diễn nhị phân:** Viết chương trình nhận một tham số dòng lệnh là số nguyên dương n, đặt biểu diễn nhị phân của n vào một chuỗi và sau đó in chuỗi đó.

17. **Bàn cờ:** Viết chương trình nhận một tham số dòng lệnh là số nguyên n và in ra mô hình bàn cờ hai chiều n-by-n với các dấu cách và dấu sao xen kẽ, giống như mô hình 4-by-4 sau.

```
* * * *
 * * * *
* * * *
 * * * *
```

28. **Ước chung lớn nhất:** Viết chương trình nhận hai số nguyên x và y từ dòng lệnh và tìm và in ra ước chung lớn nhất (gcd) của x và y bằng cách sử dụng thuật toán Euclid.

29. **Số nguyên tố cùng nhau:** Viết chương trình nhận một tham số dòng lệnh n và in ra bảng n-by-n sao cho có dấu * ở hàng i và cột j nếu gcd của i và j là 1 (i và j là số nguyên tố cùng nhau), và một khoảng trắng ở vị trí đó.

1. **Taxi của Ramanujan:** Nhà toán học Ấn Độ S. Ramanujan nổi tiếng với trực giác tuyệt vời về các con số. Một ngày nọ, khi nhà toán học người Anh G. H. Hardy đến thăm ông trong bệnh viện, Hardy nhận xét rằng số xe taxi của ông là 1729, một con số khá nhàm chán. Ramanujan đáp lại: "Không, Hardy! Không, Hardy! Đó là một con số rất thú vị. Đó là số nhỏ nhất có thể biểu diễn thành tổng của hai số lập phương theo hai cách khác nhau." Xác minh khẳng định này bằng cách viết chương trình nhận một tham số dòng lệnh n và in ra tất cả các số nguyên nhỏ hơn hoặc bằng n có thể được biểu diễn thành tổng của hai số lập phương theo hai cách khác nhau. Nói cách khác, tìm các số nguyên dương phân biệt a, b, c và d sao cho a<sup>3</sup> + b<sup>3</sup> = c<sup>3</sup> + d<sup>3</sup>. Sử dụng bốn vòng lặp `for` lồng nhau.

2. **Biển số xe:** Biển số xe 87539319 có vẻ như là một con số khá nhàm chán. Hãy xác định lý do tại sao nó không phải như vậy.

3. **Mã kiểm tra ISBN:** Mã số sách tiêu chuẩn quốc tế (ISBN) là mã gồm 10 chữ số, xác định duy nhất một cuốn sách. Chữ số ngoài cùng bên phải là chữ số kiểm tra, có thể được xác định duy nhất từ ​​9 chữ số còn lại theo điều kiện 10d<sub>10</sub> + 9d<sub>9</sub> + ... + 2d<sub>2</sub> + d<sub>1</sub> phải là bội số của 11 (ở đây d<sub>i</sub> biểu thị chữ số thứ i tính từ phải sang). Chữ số kiểm tra d<sub>1</sub> có thể là bất kỳ giá trị nào từ 0 đến 10: quy ước ISBN là sử dụng giá trị 'X' để biểu thị 10. Ví dụ: chữ số kiểm tra tương ứng với 020131452 là 5 vì là giá trị duy nhất của d<sub>1</sub> từ 0 đến 10 mà 10 * 0 + 9 * 2 + 8 * 0 + 7 * 1 + 6 * 3 + 5 * 1 + 4 * 4 + 3 * 5 + 2 * 2 + d<sub>1</sub> là bội số của 11. Viết chương trình nhận một số nguyên 9 chữ số làm tham số dòng lệnh, tính toán chữ số kiểm tra và in ra số ISBN gồm 10 chữ số. Không sao nếu chương trình không in bất kỳ số 0 nào ở đầu.

4. **Đếm số nguyên tố:** Viết chương trình nhận một tham số dòng lệnh n và in ra số lượng số nguyên tố nhỏ hơn n. Sử dụng nó để in ra số lượng số nguyên tố nhỏ hơn 10 triệu. Lưu ý: nếu bạn không cẩn thận để làm cho chương trình của mình hiệu quả, nó có thể sẽ không kết thúc trong một khoảng thời gian hợp lý.

6. **Trung vị của 5:** Viết chương trình nhận năm số nguyên phân biệt từ dòng lệnh và in ra giá trị trung vị (giá trị mà hai trong số các số nguyên khác nhỏ hơn và hai số nguyên lớn hơn). Điểm cộng: Giải quyết bài toán bằng một chương trình so sánh các giá trị ít hơn bảy lần cho bất kỳ đầu vào nào.

10. **Bài toán của Pepys:** Năm 1693, Samuel Pepys hỏi Isaac Newton điều gì có khả năng xảy ra hơn: nhận được ít nhất một lần số 1 khi gieo một con xúc xắc sáu mặt sáu lần hoặc nhận được ít nhất hai lần số 1 khi gieo nó 12 lần. Viết chương trình có thể cung cấp cho Newton câu trả lời nhanh chóng.

11. **Mô phỏng trò chơi:** Trong chương trình trò chơi những năm 1970 "Hãy chọn cửa", người chơi được trình bày ba cánh cửa. Đằng sau một trong số chúng là một giải thưởng giá trị. Sau khi người chơi chọn một cánh cửa, người dẫn chương trình sẽ mở một trong hai cánh cửa còn lại (tất nhiên là không bao giờ tiết lộ giải thưởng). Sau đó, người chơi được trao cơ hội chuyển sang cánh cửa chưa mở khác. Người chơi có nên làm như vậy? Theo trực giác, có vẻ như cánh cửa lựa chọn ban đầu của người chơi và cánh cửa chưa mở khác có khả năng chứa giải thưởng như nhau, vì vậy sẽ không có động lực để chuyển đổi. Viết chương trình để kiểm tra trực giác này bằng mô phỏng. Chương trình của bạn sẽ nhận một tham số dòng lệnh n, chơi trò chơi n lần bằng cách sử dụng mỗi chiến lược (chuyển đổi hoặc không chuyển đổi) và in ra cơ hội thành công cho mỗi chiến lược.

13. **Giả thuyết về tổng lũy thừa của Euler:** Năm 1769, Leonhard Euler đã hình thành một phiên bản tổng quát của Định lý cuối cùng của Fermat, phỏng đoán rằng cần có ít nhất n lũy thừa bậc n của các số nguyên dương để có được một tổng là lũy thừa bậc n, với n> 2. Viết chương trình để bác bỏ giả thuyết của Euler (đứng vững cho đến năm 1967) , sử dụng một vòng lặp lồng nhau năm lần để tìm bốn số nguyên dương có tổng lũy thừa thứ 5 bằng với lũy thừa thứ 5 của một số nguyên dương khác. Đó là, tìm năm số nguyên a, b, c, d và e sao cho a<sup>5</sup> + b<sup>5</sup> + c<sup>5</sup> + d<sup>5</sup> = e<sup>5</sup>.

# Chọn 10 bài không trùng nhau, bất kì để làm.