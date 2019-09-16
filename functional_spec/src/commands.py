import sys

from functional_spec.src.cars import Car

# comands used in system

commands = {'leave': 'LEAVE',
            'create_parking_lot': 'CREATE',
            'status': 'STATUS',
            'park': 'PARK',
            'registration_numbers_for_cars_with_colour': 'CAR_WITH_COLOR',
            'slot_numbers_for_cars_with_colour': 'SLOT_WITH_COLOR',
            'slot_number_for_registration_number': 'SLOT_WITH_REG_NUM',
            'exit': 'EXIT'
            }


# command functions


def command(line, parking_lot):
    """
    it it used to run the commands mentioned in prking lot system
    :param line: command given to system to process
    :param parking_lot: parking_lot object
    :return: data as per command
    """

    data = line.split()
    if data[0] in commands:
        if data[0] == 'create_parking_lot':
            try:
                parking_lot.initialise_parking(data[1])
                return 'Created a parking lot with {} slots'.format(data[1])
            except IndexError:
                return 'please provide the size of parking lot'

        if data[0] == 'park':
            if len(data) == 3:
                try:
                    car = Car(data[1], data[2])
                    slot = parking_lot.add_car(car)
                    return 'Allocated Slot Number: {}'.format(slot)
                except:
                    return 'Sorry, parking lot is full'
            else:
                return 'invalid arguments'
        elif data[0] == 'leave':
            if len(data) == 2:
                try:
                    slot = parking_lot.remove_car(int(data[1]))
                    if slot:
                        return 'slot number {} is free'.format(data[1])
                except:
                    return 'invalid slot number: either empty or doesnot exit.'
            else:
                return 'invaid arguments'

        elif data[0] == 'status':

            if len(data) == 1:
                _str_ = '{:10}\t{:25}\t{:10}'.format('  Slot No', 'Registration No', 'Color', width=25)
                slot_status = parking_lot.used_slots()

                if len(slot_status.keys()) == 0:
                    return "parking lot is empty."
                else:
                    final_str = ''
                    final_str += _str_ + '\n'
                    for i in slot_status.keys():
                        _str = '{:10}\t{:25}\t{:10}'.format(i, slot_status[i].get_registration_number,
                                                            slot_status[i].get_color, width=25)
                        # print(i,slot_status[i].get_registration_number,slot_status[i].get_color,sep='\t\t')
                        final_str += _str + '\n'
                    return final_str.strip()
            else:
                return 'please enter the right command'
        elif data[0] == 'registration_numbers_for_cars_with_colour':
            try:
                cars = parking_lot.get_car_reg_with_color(data[1])
                return cars
            except:
                return 'Not Found'

        elif data[0] == 'slot_numbers_for_cars_with_colour':
            cars = parking_lot.slot_num_with_color(data[1])
            if cars == 0:
                return 'Not Found'
            else:
                return cars

        elif data[0] == 'slot_number_for_registration_number':
            cars = parking_lot.slot_num_with_registration_number(data[1])
            if cars != 0:
                return cars
            else:
                return 'Not Found'

        elif data[0] == 'exit':

            print("exiting the system.")
            sys.exit(0)

    else:
        return 'invalid command'
        # print('valid commands are :')
        # for i, v in enumerate(commands):
        #     print("{}. {}".format(i + 1, v))
