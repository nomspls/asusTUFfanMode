# Check fan mode of asus TUF laptops

* This is a simple script that I wrote for personal usage since asus is too lazy to support it's drivers with linux

* Script simply checks which fan mode is currently active(balanced, silent, overboost)

* I bound it to ctrl+f

The original plan was to make it switch between modes as well as send an OSD notification.
I have yet to figuire out how to interact with acpi drivers in python thus I cannot(don't know how to) use any asus function keys in the code since it is controled by driver and acpi and linux can't read key presses of fn keys(although they are working, only way to see some keycodes is by acpi-listen command)

* Finished script would do the following:
	* Switch between fan modes on fn+f5 keypress
	* Send an OSD on what mode it's set to

# License

* MIT

