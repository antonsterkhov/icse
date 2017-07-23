import icse
import time


relays = icse.ICES('/dev/ttyUSB0')

relays.relay_on(1)
time.sleep(2)

relays.relay_off(1)


