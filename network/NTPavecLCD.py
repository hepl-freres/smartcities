import network, socket
import struct
from secrets import *
from machine import I2C,Pin,ADC
from lcd1602 import LCD1602
from time import sleep
import utime
import time

# lCD display settings
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16) # number of lines and characters per lines
d.display()




# Offset = shift from UTC time in sec 7200 = 2h (UTC + 1 + DST)
# DTS = 1 hour whenthis program was written.
# To be correct Daylight Saving Time (DST) should be taken into account automatically

# delta is the seconds difference between 1.1.1970 and 1.1.1900
# It is related to the way datetime is coded in NTP and
# the way the UNIX date used in Python is coded
def get_time(offset=7200, delta=2208988800, host="pool.ntp.org"):
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B # version 3 mode 3
    
    # Server name resolution
    addr = socket.getaddrinfo(host, 123)[0][-1] # 123 is the port number for NTP
    # the getaddrinfo() returns the IP address of the host and other info
    # in the form of a list of 5 tuples, the last tuple [-1] containing
    # a tuple with IP address as a string and port number as an integer
    
    # Creates a socket (= a connection to a service) on the NTP server
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP/IP
    
    try:
        s.settimeout(1)
        res = s.sendto(NTP_QUERY, addr) # Sends query to FTP server (an empty packet
                                        # with field LI, VN & MODE specifications
        msg = s.recv(48) # Gets answer
    finally:
        s.close() # Closes the socket connection
    
    val = struct.unpack("!I", msg[40:44])[0] # extracts integer data, big endian coded
    # msg[40:44] contains the integer part of the transmit time stamp.
    # for details see https://labs.apnic.net/index.php/2014/03/10/protocol-basics-the-network-time-protocol/
    t = val - delta # converts from NTP time format to Python (Unix) type   
    tm = utime.gmtime(t+offset) # adds offset according your timezone
    return tm  # year month, day, hour, minute, second, weekday (0-6), yearday)


#WiFi connection
wlan = network.WLAN(network.STA_IF) # create and initialize a wlan object
wlan.active(True)
wlan.connect('WiFi-2.4-9B4E', 'ws4k7a7cksa6j') # access point and password


# Waits for connection or exit with error code if it fails

while not wlan.isconnected() and wlan.status() >= 0:
    print("Connexion...")
    time.sleep(1)
time.sleep(0.5)
print("Connected")



# Now we can use the connection to access Internet.

t_now=get_time() # Use of the NTP protocol to get the time and date
print("Heure: {:2d}:{:02d}:{:02d}".format(t_now[3],t_now[4],t_now[5])) # show time in console
    
    


while True:
    sleep(0.25)
    d.clear()                 # clears the LCD display
    d.print('Date: ')
    d.print(str(t_now[2]) +"/" + str(t_now[1]) +"/" + str(t_now[0]))     # Displays the date on the first line
    d.setCursor(0, 1)            # move the cursor
    d.print('Heure: ')            
    d.print(str(t_now[3]) +":" + str(t_now[4])) # Display the time on the second line
    time.sleep(1)


wlan.disconnect()
 