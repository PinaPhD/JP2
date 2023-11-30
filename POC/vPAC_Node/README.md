
# inside vm
## install containernet

`sudo apt-get install ansible`

`git clone https://github.com/containernet/containernet.git`

`sudo ansible-playbook -i "localhost," -c local containernet/ansible/install.yml`

% to mount shared file between vm and host
`sudo mount -t virtiofs mount /mnt/images`

`sudo python3 containernet_3ieds_mms_goose.py`

`sudo docker load -i *image-name*`

`sudo docker run -it -v /mnt/images:/mnt --net container:mn.d2 nicolaka/netshoot`


# inside container
`d1: ./libiec61850_report 103 /tmp/iec61850_open_server/demo_cfg/cfg_report_goose/arkens_htb.cfg `


`d2: ./libiec61850_server_client d2-eth0 103 /tmp/iec61850_open_server/demo_cfg/cfg_report_goo/arkens_tg.cfg /tmp/iec61850_open_server/demo_cfg/cfg_report_goose/arkens_tg.ext 192.168.122.251 103 01`


`d3: ./libiec61850_server d3-eth0 103 /tmp/iec61850_open_server/demo_cfg/cfg_report_goose/arkens_hta.cfg /tmp/iec61850_open_server/demo_cfg/cfg_report_goose/arkens_hta.ext `


# inside netshoot
`tcpdump -i d2-eth0 -w /mnt/test.pcap`

