from functional_spec.src.cars import Car

commands = {'leave': 'LEAVE',
            'create_parking_lot': 'CREATE',
            'status': 'STATUS',
            'park': 'PARK',
            'registration_numbers_for_cars_with_colour': 'CAR_WITH_COLOR',
            'slot_numbers_for_cars_with_colour': 'SLOT_WITH_COLOR',
            'slot_number_for_registration_number': 'SLOT_WITH_REG_NUM'
            }

def command(line, parking_lot):
                        data = line.split()
                        if data[0] in commands:
                            if data[0]=='create_parking_lot':

                                parking_lot.initialise_parking(data[1])
                                print('Created a parking lot with {} slots'.format(data[1]))

                            if data[0]=='park':
                                if len(data)==3:
                                    try:
                                        car = Car(data[1],data[2])
                                        slot = parking_lot.add_car(car)
                                        print('Allocated Slot Numeber: {}'.format(slot))
                                    except:
                                        print('Sorry, parking lot is full')
                                else:
                                    print('invalid arguments')
                            if data[0]=='leave':
                                if len(data)==2:
                                    try:
                                        slot = parking_lot.remove_car(int(data[1]))
                                        if slot:
                                            print('slot number {} is free'.format(data[1]))
                                    except:
                                            print('invalid slot number')
                                else:
                                    print('invaid arguments')
                            if data[0]=='status':
                                if len(data)==1:

                                    str = '{}\t{}\t\t{}'.format('slot no', 'registration no', 'color', width=15)
                                    print(str)
                                    slot_status = parking_lot.used_slots()
                                    for i in slot_status.keys():
                                        _str = '{}\t\t{}\t\t{}'.format(i,slot_status[i].get_registration_number, slot_status[i].get_color,width =22)
                                        # print(i,slot_status[i].get_registration_number,slot_status[i].get_color,sep='\t\t')
                                        print(_str)

                                else:
                                    print('error')
                            if data[0]=='registration_numbers_for_cars_with_colour':
                                try:
                                    cars = parking_lot.get_car_reg_with_color(data[1])
                                    print(cars)
                                except:
                                    print('Not Found')


                            if data[0]=='slot_numbers_for_cars_with_colour':
                                try:
                                    cars = parking_lot.slot_num_with_color(data[1])
                                    print(cars)
                                except:
                                    print('Not Found')


                            if data[0] == 'slot_number_for_registration_number':
                                try:
                                        cars = parking_lot.slot_num_with_registration_number(data[1])
                                        print(cars)
                                except:
                                        print('Not Found')
                            if data[0]=='exit':
                                exit(-1)