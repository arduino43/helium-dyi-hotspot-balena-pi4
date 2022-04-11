#!/usr/bin/python3
import os
import os.path
import sys
import json
import time

region = os.environ.get("REGION","US915")
miner = os.environ.get("MINER_IP","10.10.110.20")

print("Modifying gateway_conf.json  %s %s" %(region,miner))

with open('./global_conf_%s.json' %(region)) as f:
  data = json.load(f)

data['gateway_conf']['server_address'] = miner



with open('/build/packet_forwarder/lora_pkt_fwd/global_conf.json', 'w') as outfile:
   outfile.write(json.dumps(data, indent=4))

print("global_conf.json recreated successfully")
