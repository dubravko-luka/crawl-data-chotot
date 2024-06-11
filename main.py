from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import datetime
from utils import get_attribute_or_empty, scrape_data

driver = webdriver.Chrome()

# Tạo tên file theo định dạng yêu cầu
current_date = datetime.datetime.now().strftime('%Y-%m-%d')
filename = f'{current_date}-page-1-100.csv'

# Mở file CSV và viết tiêu đề các cột
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Link', 'Tên', 'Giá', 'Số Km đã đi', 'Số chủ sở hữu', 'Hãng xe', 'Dòng xe',
                     'Năm sản xuất', 'Xuất xứ', 'Tình trạng', 'Tùy chọn', 'Hộp số', 'Nhiên liệu', 'Loại xe',
                     'Số chỗ ngồi', 'Hệ dẫn động', 'Loại động cơ', 'Công suất', 'Momen xoắn', 'Dung tích động cơ',
                     'Tiêu thụ nhiên liệu', 'Túi khí', 'Khoảng sáng gầm xe', 'Số cửa', 'Trọng lượng không tải',
                     'Trọng lượng toàn tải', 'Chính sách bảo hành', 'TBÚ', 'Đăng kiểm', 'Phụ kiện đi kèm'])

    pages = list(range(1, 3))
    index = 0

    for page in pages:
        url = f'https://xe.chotot.com/mua-ban-oto?page={page}'
        driver.get(url)
        time.sleep(10)
        links = driver.find_elements(By.CSS_SELECTOR, 'a[itemprop="item"]')
        href_links = [link.get_attribute('href') for link in links]

        for href_link in href_links:
            data = scrape_data(driver, href_link)
            writer.writerow(data)
            index += 1
            if index >= 5:
                break

        index = 0

driver.quit()
print(f"Đã lưu các thông tin vào file '{filename}'")
