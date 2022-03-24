class WarehouseOfficeEquipment:
    """Не поняла смысл создания этого класса"""

class OfficeEquipment:
    def __init__(self, brand: str, year:int, app_color:str, possible_colors: tuple, two_sided_printing: bool, sheet_format: list, value: int) -> None:
        self.brand = brand
        self.year = year
        self.app_color = app_color
        self.possible_colors = possible_colors  
        self.two_sided_printing = two_sided_printing   
        self.sheet_format = sheet_format
        self.value = value

class Printer(OfficeEquipment):
    def __init__(self, brand: str, year: int, app_color: str, possible_colors: tuple, two_sided_printing: bool, usb_port:int, sheet_format: list, value: int) -> None:
        super().__init__(brand, year, app_color, possible_colors, two_sided_printing, sheet_format, value)
        self.usb_port = usb_port

class Scanner(OfficeEquipment):
        def __init__(self, brand: str, year: int, app_color: str, possible_colors: tuple, scanner_glass_area: float, value: int) -> None:
            super().__init__(brand, year, app_color, possible_colors, value)
            self.scanner_glass_area = scanner_glass_area

class Copier(OfficeEquipment):
    def __init__(self, brand: str, year: int, app_color: str, possible_colors: tuple, two_sided_printing: bool, sheet_format: list, value: int) -> None:
        super().__init__(brand, year, app_color, possible_colors,two_sided_printing, sheet_format, value)
