__author__ = 'Prashant Rana'
__email__ = 'sahasrara62@gmail.com'


import sys
import  os
from copy import  deepcopy as dcopy
from functional_spec.src.parking import Parking
from functional_spec.src.cars import  Car
from functional_spec.src.commands import commands, command



def run():
    parking = Parking()

    if len(sys.argv)>1:
            file_path = sys.argv[1]
            if os.path.exists(file_path):
                parking_lot = Parking()
                with open(file_path, 'r') as file:
                    for line in file.readlines():
                        command(line, parking_lot)
    else:
        cmd = None
        while True:
            cmd = input()
            if cmd:
                command(cmd, parking)




if __name__=='__main__':
    run()