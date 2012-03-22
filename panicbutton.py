import usb.core
import time
import json
import os

def read_command():
    home = os.path.expanduser('~')
    f = open(home + '/.panicbutton/config.json')
    config = json.load(f)
    f.close()
    return config['command']

def pressed(device):
    """ Read the USB device
    Return 1 if pressed and released, 0 otherwise.
    """
    # Magic numbers are from http://search.cpan.org/~bkendi/Device-USB-PanicButton-0.04/lib/Device/USB/PanicButton.pm
    try:
        device.set_configuration()
        ct = device.ctrl_transfer(bmRequestType=0xA1, bRequest=1, wValue=0x300, data_or_wLength=8, timeout=250)
        result = ct[0]
    except Exception, e:
        result = 0
        print e
    return result

#    Product ID:    0x0202
#    Vendor ID:     0x1130    (Tenx Technology, Inc.)
#    Version:       1.00
#    Speed:         Up to 1.5 Mb/sec
device = usb.core.find(idVendor=0x1130, idProduct=0x0202)

print "Panic Button time! Press Ctrl-C to quit."
print "Looking for the Panic Button... please wait"
# loop until device is found
while 1:
    try:
        if not device:
            raise ValueError("Panic Button not found: Are you sure it's plugged in?")
    except Exception, e:
        print e
        time.sleep(1)
        device = usb.core.find(idVendor=0x1130, idProduct=0x0202)
        continue
    print "Panic Button found. Press away!"
    break

# do an initial read to clear out any stale button presses
pressed(device)

if __name__ == "__main__":
    try:
        while 1:
            if pressed(device):
                print "Command to execute: " + read_command()
            time.sleep(.15)
    except KeyboardInterrupt, e:
        exit(0)
