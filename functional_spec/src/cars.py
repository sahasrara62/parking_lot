
__all__ = ['Car']

class Car(object):
    """
    defining the property of the car
    property include : car "registration number" and "colour" of the car
    """

    def __init__(self, registation_number, color):
        """
        intialising the car object

        :param registation_number: registation number of car
        :param color: color of car
        """
        self._reg_number = registation_number
        self._color = color

    @property
    def get_registration_number(self):
        return self._reg_number

    @property
    def get_color(self):
        return self._color
