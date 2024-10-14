Bài 1: Chèn khoảng thời gian mới

Đề bài:
Cho một mảng các khoảng thời gian không chồng chéo `intervals`, trong đó mỗi khoảng thời gian được biểu diễn bởi điểm bắt đầu và kết thúc. Mảng này đã được sắp xếp theo thứ tự tăng dần của điểm bắt đầu. Bạn cần chèn một khoảng thời gian mới `newInterval` vào mảng sao cho mảng vẫn được sắp xếp và không có khoảng thời gian nào chồng chéo.

Yêu cầu:
1. Chèn `newInterval` vào `intervals`.
2. Hợp nhất các khoảng thời gian chồng chéo nếu cần.
3. Trả về mảng kết quả sau khi chèn.

Ví dụ:
```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

Bài tập cho sinh viên:
1. Chèn một khoảng thời gian mới vào mảng các khoảng thời gian đã sắp xếp.
2. Xử lý các trường hợp chồng chéo và hợp nhất khoảng thời gian nếu cần.
3. Đảm bảo mảng kết quả vẫn được sắp xếp theo thứ tự tăng dần của điểm bắt đầu.

Bài 2: Tìm phần tử xuất hiện nhiều nhất

Đề bài:
Cho một mảng số nguyên `nums`. Tìm phần tử xuất hiện nhiều hơn một nửa số lần trong mảng.

Yêu cầu:
1. Tìm phần tử xuất hiện nhiều hơn `n/2` lần trong mảng, với n là độ dài của mảng.
2. Giả định rằng phần tử này luôn tồn tại trong mảng.

Ví dụ:
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

1. Tìm phần tử xuất hiện nhiều nhất trong mảng.
2. Sử dụng thuật toán Boyer-Moore Voting).
3. Kiểm tra kết quả với các ví dụ khác nhau.

## Số lượng đảo

**Mô tả bài toán:**

Bạn được cho một lưới 2 chiều (mảng 2D) chứa các ô, mỗi ô có thể là '1' (đại diện cho đất) hoặc '0' (đại diện cho nước). Nhiệm vụ của bạn là đếm số lượng đảo trong lưới. Một đảo được định nghĩa là một nhóm các ô '1' kết nối với nhau theo chiều ngang hoặc chiều dọc.

**Quy tắc kết nối:**

- Hai ô '1' được coi là thuộc cùng một đảo nếu chúng nằm cạnh nhau theo chiều ngang hoặc chiều dọc.

**Ví dụ:**

Giả sử bạn có lưới sau:

```
11110
11010
11000
00000
```

Trong trường hợp này, có 1 đảo.

Còn với lưới này:

```
11000
11000
00100
00011
```

Có 3 đảo.

**Yêu cầu:**

Viết một hàm có tên `numIslands` nhận vào một lưới và trả về số lượng đảo trong lưới đó.

**Hướng dẫn thực hiện:**

1. **Khởi tạo biến đếm:** Tạo một biến để đếm số lượng đảo.
  
2. **Duyệt qua từng ô:** Sử dụng vòng lặp để duyệt qua từng ô trong lưới.

3. **Kiểm tra ô '1':** Khi gặp ô '1', tăng biến đếm lên 1 và thực hiện tìm kiếm theo chiều sâu (DFS) hoặc tìm kiếm theo chiều rộng (BFS) để đánh dấu tất cả các ô '1' liên quan đến đảo đó là đã được xử lý.

4. **Tiếp tục duyệt:** Tiếp tục duyệt qua các ô còn lại cho đến khi hoàn thành việc kiểm tra toàn bộ lưới.

5. **Trả về kết quả:** Cuối cùng, trả về số lượng đảo đã đếm được.

**Lưu ý:** Hãy chắc chắn rằng bạn không tính lại các ô đã được đánh dấu là đã xử lý trong quá trình duyệt.

---

Bài tập này giúp bạn rèn luyện kỹ năng lập trình và tư duy giải quyết vấn đề. Hãy cố gắng hoàn thành và kiểm tra xem bạn có thể tối ưu hóa thuật toán của mình hay không!

Citations:
[1] https://leetcode.com/problems/number-of-islands/description/