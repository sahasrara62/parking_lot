
__all__ = ['Car']


class Car(object):
    """
    defining the property of the car
    property include : car "registration number" and "colour" of the car
    """

    def __init__(self, registration_number, color):
        """
        initialising the car object

        :param registration_number: registation number of car
        :param color: color of car
        """
        self._reg_number = registration_number
        self._color = color

    @property
    def get_registration_number(self):
        """
        give registration number of the car
        :return:
        """
        return self._reg_number

    @property
    def get_color(self):
        """
        return color of car
        :return:
        """
        return self._color
