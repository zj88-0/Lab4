import hal.hal_input_switch as input_switch
import hal.hal_led as led
import time 

def main():
    led.init()
    input_switch.init()

    switchValue=input_switch.read_slide_switch()
    if switchValue==1:
        led.set_output(24,1)
        time.sleep(0.1)
        led.set_output(24,0)
        time.sleep(0.1)
    else:
       led.set_output(24,0)

if __name__=="__main__":
 main()
