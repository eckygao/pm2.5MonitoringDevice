from machine import UART, Pin, I2C
from ssd1306 import SSD1306_I2C
import utime, time

def getnum(hn,ln):
    return hn*256+ln

def display( oled, d1,d25,d10,active):
    line_1 = 30
    line_2 = 80
    # 
    oled.fill(0)
    #
    oled.text('PM1.0',  line_1, 20)
    oled.text(str( d1), line_2, 20)
    oled.text('PM2.5',   line_1, 30)
    oled.text(str( d25), line_2, 30)
    oled.text('PM10',    line_1, 40)
    oled.text(str( d10), line_2, 40)
    if 1 == active:
        oled.text('.', 120, 50)
    # show
    oled.show()

# init sensor
uart = UART(2, baudrate=9600, rx=14,timeout=10)

# init oled
i2c = I2C(scl=Pin(26), sda=Pin(27))
oled = SSD1306_I2C(128, 64, i2c)

# start
count = 0
while True:
    if uart.any():
        # readbuffer
        utime.sleep_ms(100)
        bin_data = uart.read()
        if 32 != len(bin_data):
            print (len(bin_data))
            continue
        # getdata
        dlist = [ time.time()]
        for i in range(14):
            dlist.append( bin_data[i*2+4]*256+bin_data[i*2+5])

        check = 0
        for i in range(30):
            check += bin_data[i]

        dlist.append(check)
        # print
        display( oled, dlist[1], dlist[2], dlist[3], count%2)
        # 
        count += 1
    utime.sleep_ms(100)
