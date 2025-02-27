from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="configure snmp", parents=()),
    ConfigLine(config_line='  add community "secret" readwrite', parents=("configure snmp",)),
    ConfigLine(
        config_line='  add target-address "target1" "10.0.0.2:161" ipv4 60 3 "info" "Params" enabled',
        parents=("configure snmp",),
    ),
    ConfigLine(
        config_line='  add target-address "target2" "10.0.0.5:161" ipv4 60 3 "info" "Params" enabled',
        parents=("configure snmp",),
    ),
    ConfigLine(
        config_line='  add target-params "Params" snmpv2c snmpv2c "secret" no-auth', parents=("configure snmp",)
    ),
    ConfigLine(
        config_line='  configure target-address "target1" bulk-traps-control disabled', parents=("configure snmp",)
    ),
    ConfigLine(
        config_line='  configure target-address "target2" bulk-traps-control disabled', parents=("configure snmp",)
    ),
    ConfigLine(config_line='  delete community "private"', parents=("configure snmp",)),
    ConfigLine(config_line='  delete community "public"', parents=("configure snmp",)),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte ntexg108-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-3",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1"),
    ),
    ConfigLine(
        config_line="      a2n-push-port-vid disabled",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      admin-state unassigned",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      admin-state in-service",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line='      alias "CUST-HANDOFF"',
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-00 pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-01 pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-02 pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-03 pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-04 pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-05 pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-06 pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-07 pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-08 pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-09 pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0a pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0b pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0c pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0d pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0e pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0f pass-thru",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      port-vlan-id 1-0",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      priority-mapping-profile prio_map_profile-1",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      service-type evpl",
        parents=("network-element ne-1", "  configure nte ntexg108-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
]
