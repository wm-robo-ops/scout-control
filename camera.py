import subprocess
subprocess.call("raspivid -t 0 -w 640 -h 480 -fps 15 -b 500000 -o - | nc -l -p 443 -k",shell=True)