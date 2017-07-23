import serial
import time


class ICES:
    _is_port = False
    _model = ''
    _bits = 0x00

    _list_model = {'ices12a': 4, 'ices13a': 2, 'ices14a': 8}

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
                time.sleep(.2)
                return 'ices12a'
            elif self._port.read(1) == b'\xad':
                self._port.write(b'\x51')
                time.sleep(.2)
                return 'ices13a'
            elif self._port.read(1) == b'\xac':
                self._port.write(b'\x51')
                time.sleep(.2)
                return 'ices14a'
            else:
                return 'ices14a'

    def relays_on(self):
        self._bits = b'\xff'
        self._port.write(b'\xff')

    def relays_off(self):
        self._bits = b'\x00'
        self._port.write(b'\x00')

    def relay_on(self, num_relay):
        if num_relay <= self._list_model[self._model]:
            self._set_bit(bits=self._bits, number_bit=num_relay - 1)
        else:
            print ('Model relay board {name} max relay {count}'.
                   format(name=self._model, count=self._list_model[self._model]))

    def relay_off(self, num_relay):
        if num_relay <= self._list_model[self._model]:
            self._remove_bit(bits=self._bits, number_bit=num_relay - 1)
        else:
            print ('Model relay board {name} max relay {count}'.
                   format(name=self._model, count=self._list_model[self._model]))

    def _set_bit(self, bits, number_bit):
        bits = bits | (1 << number_bit)
        self._port.write(bytes([bits]))

    def _remove_bit(self, bits, number_bit):
        bits = bits & ~ (1 << number_bit)
        self._port.write(bytes([bits]))
