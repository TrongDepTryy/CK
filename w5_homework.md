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

<!-- Ví dụ:
``` -->
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

1. Tìm phần tử xuất hiện nhiều nhất trong mảng.
2. Sử dụng thuật toán Boyer-Moore Voting).
3. Kiểm tra kết quả với các ví dụ khác nhau.