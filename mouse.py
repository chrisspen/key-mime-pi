#!/usr/bin/env python3
import time


def write_report(report):
    with open('/dev/hidg1', 'wb+') as fd:
        print('Sending ' +
              report.hex())  # Convert bytes to hex string for display
        fd.write(report)
        print('Finished sending')
    print('Closed fd')


def alternate_left_right():
    # s1 = b'\x00\x7f\x00'  # Move right
    # s2 = b'\x00\x90\x00'  # Move left
    s1 = bytes([0, 127, 0])  # Move right, i.e. b'\x00\x7f\x00'
    s2 = bytes([0, 144, 0])  # Move left, i.e. b'\x00\x90\x00'
    for i in range(100):
        write_report(s1)
        time.sleep(0.3)
        write_report(s2)
        time.sleep(0.3)


alternate_left_right()
