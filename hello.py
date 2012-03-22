# USB Panic Button interface code
# Copyright 2010 Ken Shirriff
# http://arcfn.com
#
""" PanicButton - interface to USB Panic Button

This code requires PyUSB.
"""

import usb.core
import time
import os

# Device is: ID 1130:0202 Tenx Technology, Inc. 
dev = usb.core.find(idVendor=0x1130, idProduct=0x0202)

if not dev:
  raise ValueError("Panic Button not found")
    
#try:
#  self.dev.detach_kernel_driver(0) # Get rid of hidraw
#except Exception, e:
#  pass # already unregistered

def read(dev):
  """ Read the USB port.
  Return 1 if pressed and released, 0 otherwise.
  """
  # Magic numbers are from http://search.cpan.org/~bkendi/Device-USB-PanicButton-0.04/lib/Device/USB/PanicButton.pm
  try:
    dev.set_configuration()
    ct = dev.ctrl_transfer(bmRequestType=0xA1, bRequest=1, wValue=0x300, data_or_wLength=8, timeout=250)
    result = ct[0]
  except Exception, e:
    result = False
    print e
  return result

if __name__ == "__main__":
  while 1:
    if read(dev):
      print "NUKE'D"
    time.sleep(.15)

