import time
from src import icse

relays = icse.ICES('/dev/ttyUSB0')

# The number of relays for control depends on the model of the board.
#

time.sleep(1)

while True:

    for i in range(1,4):
        relays.relay_on(i)
        time.sleep(.5)

    for i in range(1,4):
        relays.relay_off(i)
        time.sleep(.5)
