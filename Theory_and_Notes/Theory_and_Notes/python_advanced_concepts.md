# CÁC KHÁI NIỆM PYTHON NÂNG CAO

## 1. Generators & Lazy Evaluation

- **Sample Code:**

```
def read_large_file(file_path):
    """Generator for the function reading the file line by line."""
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

# How to use:
log_gen = read_large_file("very_large_data.txt")

# Extract a single line when needed
for log_entry in log_gen:
    print(log_entry)
    # After finish processing this line, RAM will be released for the next line.
```

- Câu hỏi: Sự khác biệt về bộ nhớ giữa `return [x*2 for x in range(1000000)]` và `yield`?
- Trả lời: Generator tiết kiệm RAM hơn List bình thường vì: Khi tạo ra một List, Python sẽ đọc và lưu trữ toàn bộ các phần tử vào RAM cùng 1 lúc. Đối với Generator, nó sẽ chỉ lưu trữ “trạng thái” của hàm và “công thức” để tạo ra giá trị tiếp theo. Từ đó, tại bất kỳ thời điểm nào cũng sẽ chỉ cần tiêu tốn 1 lượng RAM nhỏ để lưu trữ dòng hiện tại đang xử lý, bất kể file được đọc nặng bao nhiêu GB. Tóm lại, List sẽ lưu trữ toàn bộ dữ liệu đang xử lý vào RAM cùng 1 lúc, còn Generator sẽ chỉ lưu vào RAM đúng nội dung hiện tại, cần đến đâu dùng đến đấy, nên ít tốn RAM hơn nhiều, đặc biệt là đối với dữ liệu lớn.
- **Ngắn gọn:** Thay vì dùng `return` tạo ra một list tốn RAM, dùng `yield` sẽ trả về từng giá trị một (generator object).
- **Ứng dụng:** Đọc file text/CSV siêu lớn hoặc load data batch cho AI model mà không làm tràn RAM.

## 2. Decorators

- **Sample Code:**

```
import time
import functools

def timer(func):
    @functools.wraps(func) # Dán nhãn cho hàm trước khi đưa vào wrapper để giữ nguyên thông tin của hàm gốc
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()	# Bắt đầu đo thời gian

        result = func(*args, **kwargs)		# Thực thi hàm gốc

        end_time = time.perf_counter()	# Kết thúc đo thời gian
        run_time = end_time - start_time	# Tính tổng thời gian thực thi hàm gốc

        print(f"--- [Timer] Hàm {func.__name__!r} chạy hết: {run_time:.4f} giây ---")
        return result
    return wrapper

	    # Sử dụng:
@timer
def model_inference(data):
    # Giả lập thời gian model xử lý
    time.sleep(1.5)
    return "Kết quả dự đoán"

# Chạy thử
output = model_inference("image_data_01")
print(f"Output: {output}")

```

- **Giải thích:** Decorator giúp thay đổi hành vi của một hàm mà không cần sửa code bên trong hàm đó.
- **Thực hành:** Custom `@timer` decorator dùng `functools.wraps` và `time.perf_counter`.
