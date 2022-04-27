# To write a program which prints speed in real time. Pressing the W key shoukd should increase the 
# speed by 10 m/s^2. Similarly, once stopped pressing the key should decrease the speed by 10 m/s^2

from prompt_toolkit.key_binding import KeyBindings

bindings = KeyBindings()

@bindings.add("w")
def test():
	print("w")
