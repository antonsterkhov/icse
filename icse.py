import serial
import time


class ICES:

    _is_port=False
    _model=''

    def __init__(self, nameport):
        try:
            self._port = serial.Serial(nameport, 9600, timeout=.1)
            self._model = self._get_model()
        except:
            self._is_port = True
            print('****Wrong name {}****'.format(nameport))

    def _get_model(self):
        if not self._is_port:
            self._port.write(b'\x50')
            if self._port.read(1) == b'\xab':
                self._port.write(b'\x51')
                return 'ices12a'
            elif self._port.read(1) == b'\xad':
                self._port.write(b'\x51')
                return 'ices13a'
            elif self._port.read(1) == b'\xac':
                self._port.write(b'\x51')
                return 'ices14a'
            else:
                return 'model none'



    def relays_on(self):
        self._port.write(b'\x00')


    def relays_off(self):
        self._port.write(b'\xff')
