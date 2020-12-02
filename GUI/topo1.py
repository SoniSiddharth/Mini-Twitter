#!/usr/bin/python
import socket 

ip = socket.gethostbyname(socket.gethostname())
print(ip)



from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call


    
def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=Controller,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)

    info( '*** Add links\n')
    a0 = {'bw':1000}
    a1 = {'bw':1000}
    a2 = {'bw':1000}
    a3 = {'bw':1000}
    a4 = {'bw':1000}
    a5 = {'bw':1000}
    a6 = {'bw':1000}
    a7 = {'bw':1000}
    a8 = {'bw':1000}
    a9 = {'bw':1000}
    a10 ={'bw':1000}
    a11 ={'bw':1000}
   
    
    
    net.addLink(s4, h8,**a0)
    net.addLink(h7, s7,**a1)
    net.addLink(h1, s1,**a2)
    net.addLink(s1, h2,**a3)
    net.addLink(h3, s2,**a4)
    net.addLink(s2, h4,**a11)
    net.addLink(h5, s3,**a5)
    net.addLink(s3, h6,**a6)
    net.addLink(s1, s4,**a7)
    net.addLink(s4, s2,**a8)
    net.addLink(s2, s7,**a9)
    net.addLink(s7, s3,**a10)


    res1 = h7.cmdPrint('python3 a_server.py 10.0.0.7 12345'+' '+ip + ' &')

    print(res1)


    









    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s7').start([c0])
    net.get('s4').start([c0])
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

