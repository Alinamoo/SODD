To run swarm commands:

Connect to drone wifi and run set_ap.py 
with wifi pwd and name
(if drone wifi isnt showing up, turn on drone,
and hold down power button until it turns off.
This resets the drone back to broadcasting wifi)

Connect to wifi and turn on drones

in command prompt 'arp -a' to list ips, 
look for dynamic ips like
192.168.175.48        60-60-1f-cb-fa-8c     dynamic
the drones should be under some of these 
(might take some playing around to get the right ips,
turn on the drones 1 by 1 to find them easier)

Make sure ips match drone sn in swarm.py
(both sn2ip and ip2id)

in the cmd files (cmd1.txt, etc.) make sure scan x 
is the number of drones you want to use,
add commands in there as per https://tello.oneoffcoder.com/swarm.html

To run commands:
python planned_flight.py -f cmd1.txt *or another file*