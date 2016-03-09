from __future__ import division, print_function
from pint import UnitRegistry
from pint.quantity import _Quantity

'''
    :copyright: 2016 by The Autoprotocol Development Team, see AUTHORS
        for more details.
    :license: BSD, see LICENSE for more details

'''

# Preload UnitRegistry
ureg = UnitRegistry("autoprotocol/units_en.txt")


class Unit(_Quantity):
    """
        Uses Pint's Quantity as a base class for implementing units.
    """
    def __new__(cls, value, units=None):
        cls._REGISTRY = ureg
        cls.force_ndarray = False
        return super(Unit, cls).__new__(cls, value, units)

    def __init__(self, value, units=None):
        super(Unit, self).__init__()
        self.unit = self.units.__str__()

    @staticmethod
    def fromstring(s):
        """
        Convert a string representation of a unit into a Unit object.

        Example
        -------

        .. code-block:: python

            Unit.fromstring("10:microliter")

        becomes

        .. code-block:: python

            Unit(10, "microliter")

        Parameters
        ----------
        s : str
            String in the format of "value:unit"

        """
        if isinstance(s, Unit):
            return s
        else:
            try:
                value, unit = s.split(":")
            except:
                raise ValueError("Incorrect Unit format. Unit has to be "
                                 "in 1:meter format.")
            return Unit(float(value), unit)

    def __str__(self):
        return ":".join([str(self.value), self.unit])

    def __repr__(self):
        return "Unit({0}, '{1}')".format(self._magnitude, self._units)
