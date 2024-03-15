class HouseScheme:
    def __init__(self, amount_of_rooms, house_area, combined_bathroom):
        if not (house_area >= 0 and isinstance(combined_bathroom, bool)):
            raise ValueError('Invalid value')
        self.amount_of_rooms = amount_of_rooms
        self.house_area = house_area
        self.combined_bathroom = combined_bathroom


class CountryHouse(HouseScheme):
    def __init__(self, amount_of_rooms, house_area, combined_bathroom, amount_of_floor, area):
        super().__init__(amount_of_rooms, house_area, combined_bathroom)
        self.amount_of_floor = amount_of_floor
        self.area = area

    def __str__(self):
        return 'Country House: Количество жилых комнат {}, ' \
               'Жилая площадь {}, Совмещенный санузел {}, ' \
               'Количество этажей {}, Площадь участка {}.' \
            .format(self.amount_of_rooms, self.house_area, self.combined_bathroom,
                    self.amount_of_floor, self.area)

    def __eq__(self, other):
        if self.house_area == other.house_area and self.area == other.area \
                and abs(self.amount_of_floor - other.amount_of_floor) <= 1:
            return True
        return False


class Apartment(HouseScheme):
    def __init__(self, amount_of_rooms, house_area, combined_bathroom, floor, window_side):
        super().__init__(amount_of_rooms, house_area, combined_bathroom)
        if not (0 < floor < 16 and window_side in ('N', 'S', 'W', 'E')):
            raise ValueError('Invalid value')
        self.floor = floor
        self.window_side = window_side

    def __str__(self):
        return 'Apartment: Количество жилых комнат {}, Жилая площадь {}, ' \
               'Совмещенный санузел {}, Этаж {}, Окна выходят на {}.' \
            .format(self.amount_of_rooms, self.house_area, self.combined_bathroom,
                    self.floor, self.window_side)


class CountryHouseList(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def append(self, p_object):
        if not isinstance(p_object, CountryHouse):
            raise TypeError('Invalid type {}'.format(str(type(p_object))))
        super().append(p_object)

    def total_square(self):
        overall_area = 0
        for house in self:
            overall_area += house.house_area
        return overall_area


class ApartmentList(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def extend(self, iterable):
        for item in iterable:
            if isinstance(item, Apartment):
                super().append(item)

    def floor_view(self, floors, directions):
        for apartment in list(filter(lambda item: max(floors) >= int(item.floor) >= min(floors) and
                                                  item.window_side in directions, self)):
            print('{}: {}'.format(apartment.window_side, apartment.floor))

