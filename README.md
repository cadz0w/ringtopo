# Mininet Ring Topology

Dynamic Ring topology generator for Mininet python API.

## Installation

Please make sure to install [Mininet](http://mininet.org/download/) before running the script

## Usage
By default, this script creates a ring with 4 switches and each switch has 2 hosts attached, you can also modify the parameters to have more switches and hosts in line 41.

*Note the parameters: Switches = swnum, Hosts = hnum.*
```python
net = Mininet(topo=GenericRing(swnum=4, hnum=2), host=CPULimitedHost, controller=None)
```
## Run
Simply just run the script using python.
```
>sudo python ringtopo.py
```
