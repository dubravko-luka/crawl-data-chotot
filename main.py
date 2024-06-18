import curses
import time
from constants import CHOTOT_URL
from ui_helpers import welcome_screen, display_menu, get_input, crawl_data, print_center

def get_id_from_url(url):
    return url.split('/')[-1].split('.')[0]

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    welcome_screen(stdscr)

    current_choice = 0
    while True:
        display_menu(stdscr, current_choice)
        key = stdscr.getch()

        if key == curses.KEY_DOWN:
            current_choice = (current_choice + 1) % 2
        elif key == curses.KEY_UP:
            current_choice = (current_choice - 1) % 2
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_choice == 0:
                start_page = int(get_input(stdscr, 5, "Nhập vào page đầu: "))
                end_page = int(get_input(stdscr, 5, "Nhập vào page cuối: "))
                crawl_data(stdscr, start_page, end_page)
                welcome_screen(stdscr)
            elif current_choice == 1:
                stdscr.clear()
                print_center(stdscr, "Đã thoát chương trình")
                stdscr.refresh()
                time.sleep(3)
                break

if __name__ == "__main__":
    curses.wrapper(main)
