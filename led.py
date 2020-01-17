from gpiozero import LED

led_green = LED(6)
led_blue = LED(13)
led_red = LED(26)

def led_on(color):
	if color is "red":
		led_red.on()
	elif color is "blue":
		led_blue.on()
	elif color is "green":
		led_green.on()
	else:
		pass


def led_off(color):
        if color is "red":
                led_red.off()
        elif color is "blue":
                led_blue.off()
        elif color is "green":
                led_green.off()
        else:
                pass

	
