import subprocess
subprocess.call("python tcp_serial_redirect_timeout.py -p /dev/ttyACM0 -b 9600 -P 21",shell=True)
