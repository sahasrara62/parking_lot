from functional_spec.src import errors
from functional_spec.src.commands import commands

__all__ = ['Parking']


class Parking(object):
    """
    main class which is parking and all the insertion and deletion of data with the parking is done using this.
    it is core component of the code base.
    """

    def __init__(self):
        self.commands = commands
        self.parking_capacity = 0
        self.slot_status = dict()

    def used_slots(self):
        """
        gives a dict which tells us that which slots are currently occupied by car in the parking lot.
        :return:  dict of used parking lot
        """
        return {i: self.slot_status[i] for i in self.slot_status if self.slot_status[i] is not None}

    def initialise_parking(self, size):
        """
        create the parking with given size
        :param size: no of cars slot to be created in the parking
        :return: None
        """
        if int(size) > 0:
            self.parking_capacity = int(size)
        else:
            self.parking_capacity = 0
            raise errors.SizeError('invalid parking size, size cannot be negative or zero.')

        self.slot_status = {i + 1: None for i in range(self.parking_capacity)}

    @property
    def get_parking_size(self):
        """
        give back the size of the parking
        :return: total no of slot in the parking
        """

        return self.parking_capacity

    def _avaiable_slot(self):
        """
        give list of slot which are no occupiecd yet.
        :return:
        """
        slot = [_slot for _slot in self.slot_status if self.slot_status[_slot] is None]
        if len(slot) != 0:
            return min(slot)
        return None

    def __parked_cars(self):
        """
        give dictionary which tells us the slot and cars details whre they are parkid
        :return:
        """
        return {i: self.slot_status[i] for i in self.slot_status if self.slot_status[i] is not None}

    def add_car(self, car_object):
        """
        adding car object to the parking lot to occupy a slot
        :param car_object:  Car class instance
        :return: tell the status if car is parked or not
        """

        if car_object.get_registration_number and car_object.get_color:
            slot_avaible = self._avaiable_slot()
            if slot_avaible is not None:
                self.slot_status.update({slot_avaible: car_object})
                return "{}".format(slot_avaible)
            raise errors.SlotError('Sorry, Parking lot is full.')
        raise errors.CarError('invalid car details')

    def remove_car(self, slot_number):
        """
        remove the care from a slot number and make it avaiable again
        :param slot_number: slot number of car
        :return: status regarding slot is avaibale or not
        """

        if slot_number in self.slot_status.keys():
            if self.slot_status[slot_number] is not None:
                self.slot_status[slot_number] = None
                return True
            else:
                raise errors.SlotError('slot is already empty')
        else:
            raise errors.SlotError('invalid slot number')

    def get_status(self):
        """
        gives status of all the slot avaiable in the parking lot
        :return:
        """
        return self.slot_status

    def get_car_reg_with_color(self, color):
        """
        give back str of list of car seperarated by comma
        :param color: color of the car to find
        :return: string of all the registration no if car wih user defined color
        """
        cars = [car.get_registration_number for car in self.__parked_cars().values() if car.get_color == color]
        if len(cars) > 0:
            return ', '.join(cars)
        else:
            raise errors.CarError('no car with color {} found '.format(color))

    def slot_num_with_color(self, color):

        """
        give back slot no of car having a color
        :param color: color of car slot to found
        :return: str of slot no
        """
        slot_number = [_slot_number for _slot_number in self.__parked_cars().keys()
                       if self.__parked_cars()[_slot_number].get_color == color]

        if len(slot_number) > 0:
            slot_numbers = list(map(str, slot_number))
            return ', '.join(slot_numbers)
        return 0

    def slot_num_with_registration_number(self, reg_num):
        """
        give the slot no of car with given registration np
        :param reg_num: registration no of car to found
        :return: slot no of car with given registration number
        """
        slot_number = [str(_slot_number) for _slot_number in self.__parked_cars().keys()
                       if self.__parked_cars()[_slot_number].get_registration_number == reg_num]
        if len(slot_number) > 0:
            return ', '.join(slot_number)
        return 0
