# BootBit
For the [Cardboard Macintosh project][cmp] - A simple on-boot emulation application chooser.

![image](https://user-images.githubusercontent.com/11209477/117720836-0e3e9700-b1d7-11eb-8f55-941694225e3a.png)

## Installing
You need **Python 3** installed, and to install the script dependencies using `pip3 install -r requirements.txt`.

Drop the script anywhere you want (I put it in a folder `BootBit` in the home directory) and run it by running `python3 main.py`.

## Config
Uses a simple **config.json** file. An example can be found supplied with the project.

## Starting on GUI Startup
I used the LXDE autostart for this. In my installation, I had no local Autostart and apparently [local *overrides* rather than compliments][ldir], so run this before continuing if yours doesn't exist too.

`cp /etc/xdg/lxsession/LXDE-pi/autostart ~/.config/lxsession/LXDE-pi`

Adding the following to the end of your newly-available local copy (assumes you installed in BootBit folder in home directory, adjust if otherwise):

`@lxterminal --working-directory=/home/pi/BootBit -e python3 main.py`

[cmp]: https://soupbowl.blog/2021/04/i-made-cardboard-macintosh-with-a-raspberry-pi
[ldir]: https://raspberrypi.stackexchange.com/a/102297
