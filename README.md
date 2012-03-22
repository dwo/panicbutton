USB Panic Button
================

I got given a [USB Panic Button](http://www.firebox.com/product/1742/USB-Panic-Button)
for christmas a few years ago.

I'm trying to make it do things on Mac OSX with Python.

Shout Outs
----------

Shamelessly learned what calls to make from [Ken Shirriff's experiences on Linux](http://www.arcfn.com/2010/04/usb-panic-button-with-linux-and-python.html)
who also copied some magic number knowledges from [Benjamin Kendinibilir's adventures in Perl](http://search.cpan.org/~bkendi/Device-USB-PanicButton-0.04/lib/Device/USB/PanicButton.pm).

What I done to make it run
--------------------------

I used [libusb](http://sourceforge.net/projects/libusb/) but it's possible that 
[OpenUSB](http://sourceforge.net/projects/openusb/) would work too. For 
convenience, I used [homebrew](https://github.com/mxcl/homebrew).
  
    brew install libusb

I ran Python 2.7.2 through [virtualenv](https://github.com/pypa/virtualenv). Then,
I got some [PyUSB](https://github.com/walac/pyusb)

    pip install pyusb

After hacking about on Ken's script for a while

    python panicbutton.py

will print "NUKE'D" when you press the panic button.
