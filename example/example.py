
from src import icse

relays = icse.ICES('/dev/ttyUSB0')

relays.relay_on(1)

relays.relay_off(1)

relays.relays_on()

relays.relays_off()



