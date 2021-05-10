# BootBit
For the [Cardboard Macintosh project][cmp] - A simple on-boot emulation application chooser.

## Starting on GUI Startup
I used the LXDE autostart for this. In my installation, I had no local Autostart and apparently [local *overrides* rather than compliments][ldir], so run this before continuing if yours doesn't exist too.

`cp /etc/xdg/lxsession/LXDE-pi/autostart ~/.config/lxsession/LXDE-pi`

Adding the following to the end of your newly-available local copy:

`@lxterminal --working-directory=/home/pi/BootBit -e python3 main.py`

[cmp]: https://www.soupbowl.io/2021/04/i-made-cardboard-macintosh-with-a-raspberry-pi/
[ldir]: https://raspberrypi.stackexchange.com/a/102297