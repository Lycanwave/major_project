from mininet.topo import Topo

class MyTopo( Topo ):
	
	def __init__( self ):
		
		Topo.__init__(self)
		
		#Add hosts and Switches
		leftHost = self.addHost('h1')
		rightHost = self.addHost('h2')
		leftSwitch = self.addSwitch('s1')
		rightSwitch = self.addSwitch('s2')
		
		#Add Links
		self.addLink(leftHost,leftSwitch)
		self.addLink(leftSwitch,rightSwitch)
		self.addLink(rightSwitch,rightHost)
		
topos = {'mytopo': ( lambda: MyTopo() )}
