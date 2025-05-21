import hal.hal_input_switch as input_switch
import hal.hal_led as led
import time 
import PiDemo as blink
i=0
def main():
    led.init()
    input_switch.init()

    switchValue=input_switch.read_slide_switch()
    if switchValue==1:
       while switchValue==1:
        blink.blink_led(0.1)
    else:
       while (i<25):
        blink.blink_led(0.05)
        i+=1

if __name__=="__main__":
 main()
