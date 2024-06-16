import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import fetch_car_info, save_to_csv
from constants import CHOTOT_URL

def get_id_from_url(url):
    return url.split('/')[-1].split('.')[0]

if __name__ == "__main__":
    driver = webdriver.Chrome()

    links = []
    pages = list(range(1, 2))
    for page in pages:
        url = CHOTOT_URL.format(page)
        driver.get(url)
        time.sleep(10)
        
        elements = driver.find_elements(By.CSS_SELECTOR, 'a[itemprop="item"]')
        for element in elements:
            href = element.get_attribute('href')
            links.append(href)

    driver.quit()

    data = []
    for link in links:
        id = get_id_from_url(link)
        car_info = fetch_car_info(id)
        if car_info and 'ad' in car_info and 'product_id' in car_info['ad']:
            car_data = {
                'ad': car_info['ad'],
                'parameters': car_info['parameters']
            }
            data.append(car_data)

    save_to_csv(data)
    print(f"Đã lưu thông tin vào file CSV.")
