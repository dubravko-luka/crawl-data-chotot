import requests
import csv
import datetime
import time
from constants import API_AD_LISTING, API_PRODUCT_GRAPH, CSV_HEADERS

def fetch_car_info(id):
    api_url = API_AD_LISTING.format(id)
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def fetch_product_info(id):
    api_url = API_PRODUCT_GRAPH.format(id)
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def save_to_csv(data):
    current_datetime = datetime.datetime.now()
    current_datetime = datetime.datetime.now()

    filename = current_datetime.strftime('%d') + 'D-' + \
            current_datetime.strftime('%-m') + 'M-' + \
            current_datetime.strftime('%Y') + 'Y-' + \
            current_datetime.strftime('%-H') + 'h-' + \
            current_datetime.strftime('%M') + 'm.csv'

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(CSV_HEADERS)

        for item in data:
            if 'product_id' not in item['ad']:
                continue

            ad = item['ad']
            parameters = item['parameters']
            link = item['link']
            product_info = fetch_product_info(ad['product_id'])
            if not product_info:
                continue

            link = link
            name = ad.get('subject', '')
            price = ad.get('price_string', '')
            city = ad.get('region_name', '')
            mileage = next((param['value'] for param in parameters if param['id'] == 'mileage_v2'), '')
            number_of_owners = next((param['value'] for param in parameters if param['id'] == 'number_of_owners'), '')
            car_brand = next((param['value'] for param in parameters if param['id'] == 'carbrand'), '')
            car_model = next((param['value'] for param in parameters if param['id'] == 'carmodel'), '')
            manufacture_date = next((param['value'] for param in parameters if param['id'] == 'mfdate'), '')
            car_origin = next((param['value'] for param in parameters if param['id'] == 'carorigin'), '')
            condition = next((param['value'] for param in parameters if param['id'] == 'condition_ad'), '')
            option = next((param['value'] for param in parameters if param['id'] == 'option'), '')
            gearbox = next((param['value'] for param in parameters if param['id'] == 'gearbox'), '')
            fuel = next((param['value'] for param in parameters if param['id'] == 'fuel'), '')
            car_type = next((param['value'] for param in parameters if param['id'] == 'cartype'), '')
            car_seats = next((param['value'] for param in parameters if param['id'] == 'carseats'), '')

            # API_PRODUCT_GRAPH
            drivetrain = product_info.get('drivetrain', '')
            engine_type = product_info.get('engine_type', '')
            horse_power = product_info.get('horse_power', '')
            torque = product_info.get('torque', '')
            engine_capacity = product_info.get('engine_capacity', '')
            kml_combined = product_info.get('kml_combined', '')
            air_bag = product_info.get('air_bag', '')
            minimum_ground_clearance = product_info.get('minimum_ground_clearance', '')
            doors = product_info.get('doors', '')

            veh_unladen_weight = next((param['value'] for param in parameters if param['id'] == 'veh_unladen_weight'), '')
            veh_gross_weight = next((param['value'] for param in parameters if param['id'] == 'veh_gross_weight'), '')
            veh_warranty_policy = next((param['value'] for param in parameters if param['id'] == 'veh_warranty_policy'), '')
            tbu = next((param['value'] for param in parameters if param['id'] == 'tbu'), '')
            valid_registration = next((param['value'] for param in parameters if param['id'] == 'valid_registration'), '')
            include_accessories = next((param['value'] for param in parameters if param['id'] == 'include_accessories'), '')

            writer.writerow([link, name, price, city, mileage, number_of_owners, car_brand, car_model,
                             manufacture_date, car_origin, condition, option, gearbox, fuel, car_type,
                             car_seats, drivetrain, engine_type, horse_power, torque, engine_capacity,
                             kml_combined, air_bag, minimum_ground_clearance, doors, veh_unladen_weight,
                             veh_gross_weight, veh_warranty_policy, tbu, valid_registration,
                             include_accessories])
