# Import the required files
from pythonosc import dispatcher
from pythonosc import osc_server

# The origin of the OSC message
ip = "127.0.0.1"
port = 7001

# The address that will be listened to
address = "/composition/layers/1/position"

# Data handler
def data_handler(address, message):
    # Do something with the returned OSC message
    print(message)

# Create a dispatcher
dispatcher = dispatcher.Dispatcher()

# Map the dispatcher to the address and the data handler
dispatcher.map(address, data_handler)

# Create an OSC server with the origin and the dispatcher
server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)

# Start the server
print("Serving on {}".format(server.server_address))
server.serve_forever()