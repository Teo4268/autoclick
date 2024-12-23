import pyautogui
import time
import logging
import sys

# Cấu hình logging để ghi log ra terminal
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Lấy độ phân giải màn hình (x, y)
screen_width, screen_height = pyautogui.size()

# Tính tọa độ giữa màn hình
center_x, center_y = screen_width // 2, screen_height // 2

# Biến đếm giây
start_time = time.time()

try:
    print("Auto click đã bắt đầu. Nhấn Ctrl+C để dừng.")
    while True:
        # Click vào chính giữa màn hình
        pyautogui.click(center_x, center_y)
        
        # Tính số giây đã trôi qua
        elapsed_time = int(time.time() - start_time)
        
        # Ghi log vào terminal, bao gồm cả giây đã trôi qua
        logging.info("Click tại tọa độ: (%d, %d) (%d giây)", center_x, center_y, elapsed_time)
        
        # Chờ 1 giây trước khi click tiếp
        time.sleep(1)
except KeyboardInterrupt:
    print("Đã dừng Auto Click.")
    sys.exit()
  
