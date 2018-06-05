
## Motherboard LED

The Raspberry pi contains an LED that can also be used to provide us
with some information as to the status of the PI. It is usually used
for reporting the power status.

The green LED can be made blinking as follows in root

	echo 1 > /sys/class/leds/led0/brightness
	echo 0 > /sys/class/leds/led0/brightness

Naturally this ac be done via a remote command if your ssh keys are
uploaded and your originating computer is added to the
authorized_keys. Now you can can control them via ssh

	ssh pi@red03 "echo 1 > led; sudo cp led /sys/class/leds/led0/brightness"		
	ssh pi@red03 "echo 0 > led; sudo cp led /sys/class/leds/led0/brightness"

This is extremely useful as it allows us to check if we the OS is
available and we can access the PI.

One strategy is to for example switch the light of, once it is booted,
so we can see which board may be in trouble.
