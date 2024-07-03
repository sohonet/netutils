from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="sysname HP-JKT-01", parents=()),
    ConfigLine(config_line="dhcp enable", parents=()),
    ConfigLine(config_line="dhcp server forbidden-ip 10.10.10.1 10.10.10.100", parents=()),
    ConfigLine(config_line="dhcp server always-broadcast", parents=()),
    ConfigLine(config_line="dhcp server ip-pool CKP", parents=()),
    ConfigLine(config_line=" gateway-list 10.10.10.1", parents=("dhcp server ip-pool CKP",)),
    ConfigLine(config_line=" domain-name intra.data.co.id", parents=("dhcp server ip-pool CKP",)),
    ConfigLine(config_line=" expired day 30", parents=("dhcp server ip-pool CKP",)),
    ConfigLine(config_line=" netbios-type b-node", parents=("dhcp server ip-pool CKP",)),
    ConfigLine(config_line="bgp 65330", parents=()),
    ConfigLine(config_line=" router-id 10.10.10.254", parents=("bgp 65330",)),
    ConfigLine(config_line=" graceful-restart", parents=("bgp 65330",)),
    ConfigLine(config_line=" graceful-restart timer restart 120", parents=("bgp 65330",)),
    ConfigLine(config_line=" graceful-restart timer wait-for-rib 360", parents=("bgp 65330",)),
    ConfigLine(config_line=" peer 10.20.240.1 description ***Point to Point Connection**", parents=("bgp 65330",)),
    ConfigLine(config_line=" peer 10.20.240.1 ebgp-max-hop 10", parents=("bgp 65330",)),
    ConfigLine(
        config_line=" peer 10.30.240.1 password cipher $x$x$xxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxx==",
        parents=("bgp 65330",),
    ),
    ConfigLine(
        config_line="  address-family ipv4 unicast",
        parents=("bgp 65330", " peer 10.30.240.1 password cipher $x$x$xxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxx=="),
    ),
    ConfigLine(
        config_line="  balance 4",
        parents=("bgp 65330", " peer 10.30.240.1 password cipher $x$x$xxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxx=="),
    ),
    ConfigLine(
        config_line="  peer 10.30.240.1 enable",
        parents=("bgp 65330", " peer 10.30.240.1 password cipher $x$x$xxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxx=="),
    ),
    ConfigLine(
        config_line="  peer 10.30.240.1 route-policy P2P-FirstTry import",
        parents=("bgp 65330", " peer 10.30.240.1 password cipher $x$x$xxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxx=="),
    ),
    ConfigLine(
        config_line="  peer 10.30.240.1 route-policy P2P-FirstTry export",
        parents=("bgp 65330", " peer 10.30.240.1 password cipher $x$x$xxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxx=="),
    ),
    ConfigLine(config_line="snmp-agent", parents=()),
    ConfigLine(config_line="snmp-agent local-engineid 8000XXX123456789AB503C00000001", parents=()),
    ConfigLine(config_line="snmp-agent community read RO", parents=()),
    ConfigLine(config_line="snmp-agent community read read", parents=()),
    ConfigLine(config_line="snmp-agent community read ro", parents=()),
    ConfigLine(config_line="acl advanced name HPE", parents=()),
    ConfigLine(
        config_line=" rule 1 permit source 10.180.50.254 0 destination 10.1.0.249 0", parents=("acl advanced name HPE",)
    ),
    ConfigLine(
        config_line=" rule 2 permit source 10.180.50.0 0.0.0.127 destination 10.1.4.62 0",
        parents=("acl advanced name HPE",),
    ),
    ConfigLine(
        config_line=" rule 3 permit source 10.180.50.0 0.0.0.127 destination 10.2.4.62 0",
        parents=("acl advanced name HPE",),
    ),
    ConfigLine(config_line="header motd #", parents=()),
    ConfigLine(
        config_line="===================================================\n!!! WARNING !!!\nsystem monitoring for law enforcement and other\npurpose. Unauthorized use of this machine may\nsubject you to criminal prosecution and penalties\n==================================================#",
        parents=("header motd #",),
    ),
    ConfigLine(config_line="return", parents=()),
]
