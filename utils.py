from selenium.webdriver.common.by import By
import time

def get_attribute_or_empty(driver, selector):
    try:
        element = driver.find_element(By.CSS_SELECTOR, selector)
        return element.text.strip()
    except:
        return ''

def click_view_more_buttons(driver):
    try:
        buttons = driver.find_elements(By.CSS_SELECTOR, 'button')
        for button in buttons:
            if button.text.strip() == 'Xem thêm':
                button.click()
                time.sleep(1)  # đợi một chút để nội dung tải xong
    except:
        pass

def scrape_data(driver, href_link):
    driver.get(href_link)
    
    # Nhấn nút "Xem thêm" hai lần
    click_view_more_buttons(driver)
    click_view_more_buttons(driver)
    
    name_element = driver.find_element(By.CSS_SELECTOR, 'h1')
    name = name_element.text.strip()
    price_element = driver.find_element(By.CSS_SELECTOR, 'b')
    price = price_element.text.strip()
    
    # Thêm các thông tin cần lấy vào đây, sau khi kiểm tra xem chúng có tồn tại không
    mileage = get_attribute_or_empty(driver, 'span[itemprop="mileage_v2"]')
    number_of_owners = get_attribute_or_empty(driver, 'span[itemprop="number_of_owners"]')
    car_brand = get_attribute_or_empty(driver, 'span[itemprop="carbrand"]')
    car_model = get_attribute_or_empty(driver, 'span[itemprop="carmodel"]')
    manufacture_date = get_attribute_or_empty(driver, 'span[itemprop="mfdate"]')
    car_origin = get_attribute_or_empty(driver, 'span[itemprop="carorigin"]')
    condition = get_attribute_or_empty(driver, 'span[itemprop="condition_ad"]')
    option = get_attribute_or_empty(driver, 'span[itemprop="option"]')
    gearbox = get_attribute_or_empty(driver, 'span[itemprop="gearbox"]')
    fuel = get_attribute_or_empty(driver, 'span[itemprop="fuel"]')
    car_type = get_attribute_or_empty(driver, 'span[itemprop="cartype"]')
    car_seats = get_attribute_or_empty(driver, 'span[itemprop="carseats"]')
    drivetrain = get_attribute_or_empty(driver, 'span[itemprop="drivetrain"]')
    engine_type = get_attribute_or_empty(driver, 'span[itemprop="engine_type"]')
    horse_power = get_attribute_or_empty(driver, 'span[itemprop="horse_power"]')
    torque = get_attribute_or_empty(driver, 'span[itemprop="torque"]')
    engine_capacity = get_attribute_or_empty(driver, 'span[itemprop="engine_capacity"]')
    kml_combined = get_attribute_or_empty(driver, 'span[itemprop="kml_combined"]')
    air_bag = get_attribute_or_empty(driver, 'span[itemprop="air_bag"]')
    minimum_ground_clearance = get_attribute_or_empty(driver, 'span[itemprop="minimum_ground_clearance"]')
    doors = get_attribute_or_empty(driver, 'span[itemprop="doors"]')
    veh_unladen_weight = get_attribute_or_empty(driver, 'span[itemprop="veh_unladen_weight"]')
    veh_gross_weight = get_attribute_or_empty(driver, 'span[itemprop="veh_gross_weight"]')
    veh_warranty_policy = get_attribute_or_empty(driver, 'span[itemprop="veh_warranty_policy"]')
    tbu = get_attribute_or_empty(driver, 'span[itemprop="tbu"]')
    valid_registration = get_attribute_or_empty(driver, 'span[itemprop="valid_registration"]')
    include_accessories = get_attribute_or_empty(driver, 'span[itemprop="include_accessories"]')
    
    return [href_link, name, price, mileage, number_of_owners, car_brand, car_model, manufacture_date,
            car_origin, condition, option, gearbox, fuel, car_type, car_seats, drivetrain, engine_type,
            horse_power, torque, engine_capacity, kml_combined, air_bag, minimum_ground_clearance, doors,
            veh_unladen_weight, veh_gross_weight, veh_warranty_policy, tbu, valid_registration,
            include_accessories]
