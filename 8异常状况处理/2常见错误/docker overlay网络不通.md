sysctl -w net.bridge.bridge-nf-call-ip6tables = 1
sysctl -w net.bridge.bridge-nf-call-iptables = 1
sysctl -w net.bridge.bridge-nf-call-arptables = 1
sysctl -w net.ipv4.ip_forward=1