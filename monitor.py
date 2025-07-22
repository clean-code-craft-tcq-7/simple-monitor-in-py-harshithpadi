
from time import sleep
import sys

def vital_alert(x):
  

def vitals_ok(temperature, pulseRate, spo2):
  if temperature > 102 or temperature < 95:
    vital_alert('Temperature critical!')
    return False
  return True

def is_pulse_rate_ok(pulseRate)
  if pulseRate < 60 or pulseRate > 100:
    vital_alert('Pulse Rate is out of range!')
    return False

def is_spo2_ok(spo2)
  if spo2 < 90:
    vital_alert('Oxygen Saturation out of range!')
    return False
  return True
