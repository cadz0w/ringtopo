from mininet.node import CPULimitedHost
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink

class GenericRing(Topo):
	"""Simple topology example."""
	def __init__( self, swnum=3, hnum=1 ):
		# Numbering: h1..N, s1..M
		Topo.__init__(self)
		self.hostNum = 1
		self.switchNum = 1
		self.one = True
		self.origin = None
		self.addRing(swnum,hnum)

	def addRing(self, swnum, hnum):
		node = self.addSwitch( 's%s' % self.switchNum )
		self.switchNum += 1
		if self.origin == None:
			self.origin = node
		if swnum>1:
			child = self.addRing(swnum-1, hnum)
			self.addLink( node, child )
		for i in range(hnum):
			hnode=self.addHost( 'h%s' % self.hostNum )
			self.addLink( node, hnode )
			self.hostNum += 1
		if self.one:
			self.addLink( node, self.origin )
			self.one = False

		return node

def run():
	c = RemoteController('c', '0.0.0.0', 6633)
	# Change the args of GenericTree() to your desired values. You could even get them from command line.
	net = Mininet(topo=GenericRing(swnum=4, hnum=2), host=CPULimitedHost, controller=None)
	net.addController(c)
	net.start()
	CLI(net)
	net.stop()
if __name__ == '__main__':
	setLogLevel('info')
	run()
	
