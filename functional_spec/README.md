# Parking lot

    Author: Prashant Rana
    Email:  sahasrara62@gmail.com



**Problem Statement**

I own a multi-storey parking lot that can hold up to 'n' cars at any given point in time.
Each slot is given a number starting at 1 increasing with increasing distance from the
entry point in steps of one. I want to create an automated ticketing system that
allows my customers to use my parking lot without human intervention.
When a car enters my parking lot, I want to have a ticket issued to the driver. The
ticket issuing process includes us documenting the registration number (number
plate) and the colour of the car and allocating an available parking slot to the car
before actually handing over a ticket to the driver (we assume that our customers are
nice enough to always park in the slots allocated to them). The customer should be
allocated a parking slot which is nearest to the entry. At the exit the customer returns
the ticket which then marks the slot they were using as being available.
Due to government regulation, the system should provide me with the ability to find
out:
●●●Registration numbers of all cars of a particular colour.
Slot number in which a car with a given registration number is parked.
Slot numbers of all slots where a car of a particular colour is parked.
We interact with the system via a simple set of commands which produce a specific
output. Please take a look at the example below, which includes all the commands
you need to support - they're self explanatory. The system should allow input in two
ways. Just to clarify, the same codebase should support both modes of input - we
don't want two distinct submissions.
1) It should provide us with an interactive command prompt based shell where
commands can be typed in
2) It should accept a filename as a parameter at the command prompt and read the
commands from that file

**System Details**

    1. Operating system: Kubuntu 18.04.4 LTS
    2. Python version 3.6
    3. shell used : Bash
    4. Python path: /usr/bin/python3
    
    
**Requirements**

    1. Python 3
    2. Pytest
    3. linux machine 

To install go to bin folder and run command `bash setup.sh` 

Note : Go to bin folder through terminal, running command
through outside won't work.

** Command Available**

    1. leave
    2. create_parking_lot
    3. status
    4. park
    5. registration_numbers_for_cars_with_colour
    6. slot_numbers_for_cars_with_colour
    7. slot_number_for_registration_number
    8. exit




**instruction on how to use**
    
1. To install setup:
   
        a. go to bin folder
        b. in bin folder run command `bash setup.sh`
        
2. To run the functional test do:
       
        a. go to bin folder
        b. run bash command `bash run_functional_tests.sh`
     
3. To run the system do with out the input file

        a. go to bin folder
        b. run `bash parking_lot.sh` 
        
4. To run  application:
   
   In base folder i.e. <b>parking_lot</b>, run command
   
   a. Run using custom input 
   
        python main.py
        
      To exit the system use  `exit`
    
   b. Run using input file
   
        python main.py <path to the input file>