from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=Controller)
info('*** Adding controller\n')
net.addController('c0')
info('*** Adding docker containers\n')
#d1 = net.addDocker('d1', volumes=["/home/nadine_k/Documents/containernet/examples/nadine/demo_cfg/cfg_report_goose:/cfg"], ip='192.168.0.251', dimage="httpd:latest", network_mode="open_server61850_macvlan1")
#d2 = net.addDocker('d2', volumes=["/home/nadine_k/Documents/containernet/examples/nadine/demo_cfg/cfg_report_goose:/cfg"], ip='192.168.0.252', dimage="httpd:latest", network_mode="open_server61850_macvlan1")

d1 = net.addDocker('d1', ip='192.168.10.251', dcmd="nohup ./libiec61850_report 102 /tmp/iec61850_open_server/demo_cfg/cfg_report_goose/arkens_htb.cfg &", dimage="open_report61850:v2")
d2 = net.addDocker('d2', ip='192.168.10.252', dimage="open_server_client61850:v2")
d3 = net.addDocker('d3', ip='192.168.10.253', dcmd= "nohup ./libiec61850_server d3-eth0 102 /tmp/iec61850_open_server/demo_cfg/cfg_report_goose/arkens_hta.cfg /tmp/iec61850_open_server/demo_cfg/cfg_report_goose/arkens_hta.ext &", dimage="open_server61850:v2")

info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
info('*** Creating links\n')
net.addLink(s1, d1)
net.addLink(s2, d2)
net.addLink(s2,d3)
net.addLink(s1, s2, cls=TCLink, delay='100ms', bw=1)

info('*** Starting network\n')
net.start()
info('*** Testing connectivity\n')
net.ping([d1, d2])
net.ping([d1, d3])
info('*** Running CLI\n')
info('Execute command d2 \n')
info(d2.cmd("nohup ./libiec61850_server_client d2-eth0 102 /tmp/iec61850_open_server/demo_cfg/cfg_report_goose/arkens_tg.cfg /tmp/iec61850_open_server/demo_cfg/cfg_report_goose/arkens_tg.ext 192.168.10.251 102 01 &" ) + "\n")

CLI(net)

net.stop()
