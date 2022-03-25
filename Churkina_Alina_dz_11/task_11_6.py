from checker_error import CheckVal, MyErrIsInt

class WarehouseOfficeEquipment:
    products = {}
    def __init__(self, name: str, value: int, place: str) -> None:
        self.name = name
        self.value = value
        self.plase = place
        dict_key = name
        WarehouseOfficeEquipment.products = {dict_key : [value, place]}

    def get_info(key):
        p = WarehouseOfficeEquipment.products[key][1]
        v = WarehouseOfficeEquipment.products[key][0]
        print(f'Info "{key}": value - {v}, place - {p}')

    def transfer_to_department(key, place:str):
        WarehouseOfficeEquipment.products[key][1] = place
        n_p = WarehouseOfficeEquipment.products[key][1]
        v = WarehouseOfficeEquipment.products[key][0]
        print(f'Теперь "{key}" находится тут - "{n_p}" в количестве - {v}')

    def change_value_product(key, value):
        o_v = WarehouseOfficeEquipment.products[key][0]
        WarehouseOfficeEquipment.products[key][0] = value
        n_v = WarehouseOfficeEquipment.products[key][0]
        print(f'Изменилось кол-во "{key}": было - {o_v}, стало - {n_v}')


class OfficeEquipment:
    def __init__(self, brand: str, year:int, app_color:str, possible_colors: tuple, two_sided_printing: bool, sheet_format: list, country:str) -> None:
        self.brand = brand
        self.year = year
        self.app_color = app_color
        self.possible_colors = possible_colors  
        self.two_sided_printing = two_sided_printing   
        self.sheet_format = sheet_format
        self.country = country
class Printer(OfficeEquipment):
    def __init__(self, brand: str, year: int, app_color: str, possible_colors: tuple, two_sided_printing: bool, usb_port:int, sheet_format: list, country:str) -> None:
        super().__init__(brand, year, app_color, possible_colors, two_sided_printing, sheet_format, country)
        self.usb_port = usb_port

class Scanner(OfficeEquipment):
        def __init__(self, brand: str, year: int, app_color: str, possible_colors: tuple, scanner_glass_area: float, country:str) -> None:
            super().__init__(brand, year, app_color, possible_colors, country)
            self.scanner_glass_area = scanner_glass_area

class Copier(OfficeEquipment):
    def __init__(self, brand: str, year: int, app_color: str, possible_colors: tuple, two_sided_printing: bool, sheet_format: list, country:str) -> None:
        super().__init__(brand, year, app_color, possible_colors,two_sided_printing, sheet_format, country)

p1 = OfficeEquipment('Canon', 2022, 'white', ('black', 'color'), True, ['A4', 'A5'], 'China')

new_product = p1.brand + '_' + str(p1.year)

a = WarehouseOfficeEquipment(new_product, 2, 'A98')
WarehouseOfficeEquipment.get_info(new_product)

if __name__ == '__main__':
    new_v = input(f'Введите текущее кол-во продукта {new_product}: ')
    try:
        new_v = CheckVal.is_int(new_v) 
        WarehouseOfficeEquipment.change_value_product(new_product, new_v)
    except MyErrIsInt as er:
        print(er)

print(f'Юрий Смолов поменял позицию {new_product}')
WarehouseOfficeEquipment.transfer_to_department(new_product, 'AT56')