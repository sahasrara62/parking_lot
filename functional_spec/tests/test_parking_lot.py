import pytest

from functional_spec.src.cars import Car
from functional_spec.src.commands import command
from functional_spec.src.parking import Parking

"""
using pytest testing module here
"""


class TestClass:
    def test_parking_creation(self):
        """
        checking the parking is creating or not, IF Creating then instance of class should be same
        :return:
        """
        parking = Parking()
        assert isinstance(parking, Parking)

    def test_invalid_commands(self):
        """
        adding  a invalid command to check if it work or not
        :return:
        """

        parking_lot = Parking()
        invalid_command = 'this is invalid command'
        assert command(invalid_command, parking_lot) == 'invalid command'

    def test_add_car(self):
        """
        adding a new care to the parking lot
        :return:
        """
        num_plate = 'aa-aa-11'
        color = 'white'
        car = Car(num_plate, color)
        assert isinstance(car, Car)

    def test_parking_lot_creation(self):
        """
        create a parking lot with  specified number
        :return:
        """
        parking_lot = Parking()
        user_command = 'create_parking_lot 4'
        x = command(user_command, parking_lot)
        assert x == 'Created a parking lot with 4 slots'

    def test_adding_car_to_parking_lot(self):
        """
        adding a car to parking lot
        :return:
        """
        parking_lot = Parking()
        user_commands = ['create_parking_lot 2', 'park mh-01-01 white', 'park ho']
        assert command(user_commands[0], parking_lot) == 'Created a parking lot with 2 slots'
        assert command(user_commands[1], parking_lot) == 'Allocated Slot Number: 1'
        assert command(user_commands[2], parking_lot) == 'invalid arguments'

    def test_checking_status_of_parking_lot(self):
        """
        give out the list of car and there color present in the system
        :return:
        """
        parking_lot = Parking()
        user_commands = ['create_parking_lot 2', 'park mh-01-01 white', 'status', 'status kjs']
        assert command(user_commands[0], parking_lot) == 'Created a parking lot with 2 slots'
        assert command(user_commands[1], parking_lot) == 'Allocated Slot Number: 1'
        assert len(command(user_commands[2], parking_lot)) > 0
        assert command(user_commands[3], parking_lot) == 'please enter the right command'

    def test_check_leave_of_parking_lot(self):
        """
        check if leave function is good or not
        :return:
        """
        parking_lot = Parking()
        user_commands = ['create_parking_lot 2', 'park mh-01-01 white', 'park  a1-01-01 blue', 'leave 1', 'leave 101']
        assert command(user_commands[0], parking_lot) == 'Created a parking lot with 2 slots'
        assert command(user_commands[1], parking_lot) == 'Allocated Slot Number: 1'
        assert command(user_commands[2], parking_lot) == 'Allocated Slot Number: 2'
        assert command(user_commands[3], parking_lot) == 'slot number 1 is free'
        assert command(user_commands[4], parking_lot) == 'invalid slot number: either empty or doesnot exit.'

    def test_check_registration_numbers_for_cars_with_colour(self):
        """
        give registration number of car with a specified color
        :return:
        """
        parking_lot = Parking()
        user_commands = ['create_parking_lot 5', 'park mh-01-01 white', 'park  a1-01-01 blue', 'park aa-bb-cc blue',
                         'park aa-ff-01 red', 'registration_numbers_for_cars_with_colour blue',
                         'registration_numbers_for_cars_with_colour purple']

        assert command(user_commands[0], parking_lot) == 'Created a parking lot with 5 slots'
        assert command(user_commands[1], parking_lot) == 'Allocated Slot Number: 1'
        assert command(user_commands[2], parking_lot) == 'Allocated Slot Number: 2'
        assert command(user_commands[3], parking_lot) == 'Allocated Slot Number: 3'
        assert command(user_commands[4], parking_lot) == 'Allocated Slot Number: 4'
        assert command(user_commands[5], parking_lot) == 'a1-01-01, aa-bb-cc'
        assert command(user_commands[6], parking_lot) == 'Not Found'

    def test_slot_numbers_for_cars_with_colour(self):
        """
        test slot no of car with a spectific color
        :return:
        """
        parking_lot = Parking()
        user_commands = ['create_parking_lot 5', 'park mh-01-01 white', 'park  a1-01-01 blue', 'park aa-bb-cc blue',
                         'park aa-ff-01 red', 'slot_numbers_for_cars_with_colour blue',
                         'slot_numbers_for_cars_with_colour purple']
        assert command(user_commands[0], parking_lot) == 'Created a parking lot with 5 slots'
        assert command(user_commands[1], parking_lot) == 'Allocated Slot Number: 1'
        assert command(user_commands[2], parking_lot) == 'Allocated Slot Number: 2'
        assert command(user_commands[3], parking_lot) == 'Allocated Slot Number: 3'
        assert command(user_commands[4], parking_lot) == 'Allocated Slot Number: 4'
        assert command(user_commands[5], parking_lot) == '2, 3'
        assert command(user_commands[6], parking_lot) == 'Not Found'

    def test_slot_number_for_registration_number(self):
        """ test the slot no of regisration number"""

        parking_lot = Parking()
        user_commands = ['create_parking_lot 5', 'park mh-01-01 white', 'park  a1-01-01 blue', 'park aa-bb-cc blue',
                         'park aa-ff-01 red', 'slot_number_for_registration_number mh-01-01',
                         'slot_number_for_registration_number a-a-a']
        assert command(user_commands[0], parking_lot) == 'Created a parking lot with 5 slots'
        assert command(user_commands[1], parking_lot) == 'Allocated Slot Number: 1'
        assert command(user_commands[2], parking_lot) == 'Allocated Slot Number: 2'
        assert command(user_commands[3], parking_lot) == 'Allocated Slot Number: 3'
        assert command(user_commands[4], parking_lot) == 'Allocated Slot Number: 4'
        assert command(user_commands[5], parking_lot) == '1'
        assert command(user_commands[6], parking_lot) == 'Not Found'

    def test_exit_condition(self):
        """test if exit condition is working ord not"""
        parking_lot = Parking()
        user_command = 'exit'

        with pytest.raises(SystemExit) as pytest_wrapped_e:
            command(user_command, parking_lot)
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 0
