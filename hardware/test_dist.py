from hcsr04sensor import sensor as sens
import time

while True:
    value = sens.Measurement(17, 27)
    dist = value.raw_distance(sample_size=11, sample_wait=0.01)
    dist = value.distance(dist)

    print("dist: ", round(dist, 1))
    #time.sleep(0.01)

