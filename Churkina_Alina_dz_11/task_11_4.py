import datetime

class WarehouseOfficeEquipment:
    products = {}
    def __init__(self, name: str, value: int, place: str) -> None:
        self.name = name
        self.value = value
        self.plase = place
        dict_key = name + datetime.datetime.now()
        WarehouseOfficeEquipment.products = {dict_key : [value, place]}
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
