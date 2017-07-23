import serial
import time


class ICES:

    _is_port=False

    def __init__(self, nameport):
        try:
            self._port = serial.Serial(nameport, 9600, timeout=.1)
        except:
            self._is_port = True
            print('****Wrong name {}****'.format(nameport))

    def _get_model(self):
        if not self._is_port:
            self._port.write(b'\x50')
            if self._port.read(1) == b'\xab':
                return 'ices12a'
            elif self._port.read(1) == b'\xad':
                return 'ices13a'
            elif self._port.read(1) == b'\xac':
                return 'ices14a'
            else:
                return 'model none'

    def get_model(self):
        return self._get_model()
