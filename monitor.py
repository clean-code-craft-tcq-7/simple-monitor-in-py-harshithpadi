
from time import sleep
import sys

def vital_alert(x):
  print(x)
  for i in range(6):
    print('\r*',end='')
    sleep(1)
    print('\r*',end="")
    sleep(1)

def vitals_ok(temperature, pulseRate, spo2):
  return 

def is_pulse_rate_ok(pulseRate)
  if pulseRate < 60 or pulseRate > 100:
    vital_alert('Pulse Rate is out of range!')
    return False

def is_spo2_ok(spo2)
  if spo2 < 90:
    vital_alert('Oxygen Saturation out of range!')
    return False
  return True

Class Monitortest(unittest.Testcase):

