import curses
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import fetch_car_info, save_to_csv
from constants import CHOTOT_URL

def get_id_from_url(url):
    return url.split('/')[-1].split('.')[0]

def print_center(win, text, y_offset=0):
    lines = text.split('\n')
    height, width = win.getmaxyx()
    for i, line in enumerate(lines):
        x = (width - len(line)) // 2
        y = (height - len(lines)) // 2 + i + y_offset
        win.addstr(y, x, line, curses.A_BOLD)

def welcome_screen(win):
    win.clear()
    ascii_art = (
        "██████  ██    ██ ██████  ██████   █████  ██    ██ ██   ██  ██████  \n"
        "██   ██ ██    ██ ██   ██ ██   ██ ██   ██ ██    ██ ██  ██  ██    ██ \n"
        "██   ██ ██    ██ ██████  ██████  ███████ ██    ██ █████   ██    ██ \n"
        "██   ██ ██    ██ ██   ██ ██   ██ ██   ██  ██  ██  ██  ██  ██    ██ \n"
        "██████   ██████  ██████  ██   ██ ██   ██   ████   ██   ██  ██████  \n"
        "                                                                   \n"
        "                                                                   "
    )
    print_center(win, ascii_art)
    win.refresh()
    time.sleep(3)
    win.clear()


def display_menu(win, current_choice):
    win.clear()
    menu = ["Crawl", "Quit"]
    for idx, item in enumerate(menu):
        y = 5 + idx
        if idx == current_choice:
            win.addstr(y, 0, f"[*]  {item}", curses.A_BOLD)
        else:
            win.addstr(y, 0, f"[ ]  {item}")
    win.refresh()

def get_input(win, y, prompt_string):
    curses.echo()
    win.clear()
    win.addstr(y, 0, prompt_string)
    win.refresh()
    input_str = win.getstr().decode('utf-8')
    curses.noecho()
    return input_str

def crawl_data(win, start_page, end_page):
    driver = webdriver.Chrome()
    links = []
    for page in range(start_page, end_page + 1):
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
                'link': link,
                'parameters': car_info['parameters']
            }
            data.append(car_data)

    save_to_csv(data)
    win.addstr(2, 0, f"Đã lưu thông tin vào file CSV.")
    win.refresh()
    time.sleep(2)