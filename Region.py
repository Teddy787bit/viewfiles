import requests,ipaddress
import json
from collections import Counter

def getJSON():
    res = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json')
    data_json=res.json()
    data_list = data_json.get("prefixes", [])
    return data_list

def getIp_cnt(data_str):
    Ip_adr={}
    for data in data_str:
        if data.get("region") not in Ip_adr.keys():
            Ip_adr[data.get("region")] = [data.get("ip_prefix",)]
        else:
            Ip_adr[data.get("region")].append(data.get("ip_prefix"))
    print("-" * 34)
    print("Region".ljust(16) + "IP Address Count".rjust(18))
    print("-" * 34)
    for region , ip_cnt in Ip_adr.items():
         print(region.ljust(16) + str(len(ip_cnt)).rjust(18))
    print("-" * 34)
    

def getRegion_cnt(data_list):
    Region_cnt= Counter(reg['region'] for reg in data_list)
    print("-" * 34)
    print("Region".ljust(16) + "Occurrences".rjust(18))
    print("-" * 34)
    for region,cnt in Region_cnt.items():
        print(region.ljust(16) + str(cnt).rjust(18))
    print("-" * 34)

def main():
    Json_data=getJSON()
    getRegion_cnt(Json_data)
    getIp_cnt(Json_data)



main()


