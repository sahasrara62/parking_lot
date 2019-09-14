from functional_spec.src import errors
from functional_spec.src.commands import commands
__all__ =['Parking']


class Parking(object):
    def __init__(self):
        self.commands = commands
        self.parking_capacity = 0
        self.slot_status = dict()
    def used_slots(self):
        return {i:self.slot_status[i] for i in self.slot_status if self.slot_status[i] is not None}
    def initialise_parking(self, size):
        if int(size) > 0:
            self.parking_capacity = int(size)
        else:
            self.parking_capacity = 0
            raise errors.SizeError('invalid parking size, size cannot be negative or zero.')

        self.slot_status = {i + 1: None for i in range(self.parking_capacity)}

    @property
    def get_parking_size(self):
        return self.parking_capacity

    def _avaiable_slot(self):
        slot = [_slot for _slot in self.slot_status if self.slot_status[_slot] is None]
        if len(slot) != 0:
            return min(slot)
        return None

    def __parked_cars(self):
        return {i:self.slot_status[i] for i in self.slot_status if self.slot_status[i] is not None}

    def add_car(self, car_object):

        if car_object.get_registration_number and car_object.get_color:
            slot_avaible = self._avaiable_slot()
            if slot_avaible is not None:
                self.slot_status.update({slot_avaible: car_object})
                return "{}".format(slot_avaible)
            raise errors.SlotError('Sorry, Parking lot is full.')
        raise errors.CarError('invalid car details')

    def remove_car(self, slot_number):
        if slot_number in self.slot_status.keys():
            if self.slot_status[slot_number] is not None:
                self.slot_status[slot_number] = None
                return True
            else:
                raise errors.SlotError('slot is already empty')
        else:
            raise errors.SlotError('invalid slot number')

    def get_status(self):
        return self.slot_status

    def get_car_reg_with_color(self, color):
        cars = [car.get_registration_number for car in self.__parked_cars().values() if car.get_color == color]
        if len(cars) > 0:
            return ', '.join(cars)
        else:
            raise errors.CarError('no car with color {} found '.format(color))

    def slot_num_with_color(self, color):
        slot_number =[_slot_number for _slot_number in self.__parked_cars().keys() if self.__parked_cars()[_slot_number].color==color]

        if len(slot_number)>0:
            slot_numbers = list(map(str, slot_number))

            return ', '.join(slot_numbers)
        else:
            raise errors.SlotError('NO car with the color  {} present in parking lot'.format(color))

    def slot_num_with_registration_number(self,reg_num):
        slot_number = [str(_slot_number) for _slot_number in self.__parked_cars().keys() if self.__parked_cars()[_slot_number].get_registration_number==reg_num]
        if len(slot_number)>0:
            return ', '.join(slot_number)
        else:
            raise errors.SlotError('No car with registration number {} found in parking lot'.format(reg_num))