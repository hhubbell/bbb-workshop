#!/usr/bin/python
# Author : Richard St-Pierre June 12, 2014
# BeagleBone Black Temperature Sensor Demonstration
# Thermistor = Semitec 103AT sensor  

# === Python Libraries ===
# Adafruit_BBIO must be downloaded 

import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import math
import time
#import requests


# === Variable Declarations ===

#ADC_PIN = "P9_39"	#AIN0
#ADC_PIN = "P9_40"	#AIN1
#ADC_PIN = "P9_37"	#AIN2
#ADC_PIN = "P9_38"	#AIN3
#ADC_PIN = "P9_33"	#AIN4
ADC_PIN = "P9_36"	#AIN5
#ADC_PIN = "P9_35"	#AIN6

LED_RED  = "P9_14"      #active high
LED_YEL  = "P9_16"      #active high
LED_GRN  = "P8_19"      #active high
BUZZER   = "P3_13"      #active high
PWM_PIN  = "P9_22"      #Fan speed control     
PUSHBUTTON = "P8_26"    #active low, pull-up

#=== Temperature Sensor ====
adc_value = 0           #analog input value (0-1.0) raw (0-1800)
R_BIAS	 = 10000        #bias resistor value to GND
r_therm  = 0            #calculated thermistor resistance
temp_C   = 0            #calculated Temperature CELSIUS 
temp_F   = 0         	#calculated Temperature Fahrenheit
R_ALPHA  = 0.09919      #Ro * e^(-B/To) in K, To=298
C2KELVIN = 273.15       #Celsius to Kelvin offset
B_VALUE  = 3435         #from thermistor datasheet

#=== Setup Hardware ===
GPIO.setup(LED_RED,GPIO.OUT);
GPIO.setup(LED_YEL,GPIO.OUT);
GPIO.setup(LED_GRN,GPIO.OUT);
GPIO.setup(BUZZER,GPIO.OUT);
GPIO.setup(PUSHBUTTON,GPIO.IN);

#=== Initialize Pin Level ===
GPIO.output(LED_RED,GPIO.LOW);
GPIO.output(LED_YEL,GPIO.LOW);
GPIO.output(LED_GRN,GPIO.LOW);
GPIO.output(BUZZER,GPIO.LOW);

ADC.setup()

# === Function declarations ===


# === Turn On LEDs ===
def led_on_green():
	GPIO.output(LED_GRN,GPIO.HIGH);

def led_on_yellow():
	GPIO.output(LED_YEL,GPIO.HIGH);

def led_on_red():
	GPIO.output(LED_RED,GPIO.HIGH);

#== Turn Off LEDs ==
def led_on_green():
	GPIO.output(LED_GRN,GPIO.LOW);

def led_on_yellow():
	GPIO.output(LED_YEL,GPIO.LOW);

def led_on_red():
	GPIO.output(LED_RED,GPIO.LOW);

#== Turn On/Off Buzzer
def buzzer_on():
	GPIO.output(BUZZER, GPIO.HIGH);

def buzzer_off():
	GPIO.output(BUZZER,GPIO.LOW);



def get_temp(): # === ADC Reading and Calculation ===
    adc_value = ADC.read(ADC_PIN);
    r_therm   = ((1/adc_value)-1)*R_BIAS
    temp_C    = round(B_VALUE/math.log(r_therm/R_ALPHA)-C2KELVIN,2);
    temp_F    = round( (temp_C *9/5)+32,2);

def print_temp(): # === Display Results ===
    print '<i> ADC = ',ADC.read(ADC_PIN),' raw = ', ADC.read_raw(ADC_PIN)
    print 'T(C)= ', temp_C , ' T(F)= ', temp_F, '\n'



print "running!"

led_yellow_on()

led_red_off()


'''
myData = {'id':1, 'temp':12}
r1 = requests.post('http://localhost:8888', data=myData)



'''
'''
# === Display Program info ===

print "\nBBB LED AND  ADC DEMO"
print "Press button to read temperature"
print "< Control+C to exit >\n"


while True:
	if (GPIO.input(PUSHBUTTON)==0): 
            GPIO.output(LED_GRN,GPIO.HIGH);
            adc_value = ADC.read(ADC_PIN);
            r_therm   = ((1/adc_value)-1)*R_BIAS
            temp_C    = round(B_VALUE/math.log(r_therm/R_ALPHA)-C2KELVIN,2);
            temp_F    = round( (temp_C *9/5)+32,2);
            print_temp(); 
        time.sleep(0.5);         
        GPIO.output(LED_GRN,GPIO.LOW); 
'''
