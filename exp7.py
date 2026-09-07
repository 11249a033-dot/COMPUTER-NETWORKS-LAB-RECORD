class ARP_RARP_Simulator:
    def __init__(self):
        self.arp_table = {
            "192.168.1.1": "00:0a:95:9d:68:16",
            "192.168.1.2": "00:0a:95:9d:68:17",
            "192.168.1.3": "00:0a:95:9d:68:18",
        }
        self.rarp_table = {v: k for k, v in self.arp_table.items()}

    def arp_request(self, ip_address):
        """Simulate an ARP request to get the MAC address
        for a given IP address."""

        print(f"ARP Request: Who has {ip_address}? "
              f"Tell me your MAC address.")

        mac_address = self.arp_table.get(ip_address)

        if mac_address:
            print(f"ARP Reply: {ip_address} is at {mac_address}.")
            return mac_address
        else:
            print(f"ARP Reply: {ip_address} is not found.")
            return None

    def rarp_request(self, mac_address):
        """Simulate a RARP request to get the IP address
        for a given MAC address."""

        print(f"RARP Request: Who has MAC address {mac_address}? "
              f"Tell me your IP address.")

        ip_address = self.rarp_table.get(mac_address)

        if ip_address:
            print(f"RARP Reply: {mac_address} is associated "
                  f"with IP {ip_address}.")
            return ip_address
        else:
            print(f"RARP Reply: {mac_address} is not found.")
            return None
if __name__ == "__main__":
    simulator = ARP_RARP_Simulator()
    simulator.arp_request("192.168.1.1")
    simulator.arp_request("192.168.1.100")
    simulator.rarp_request("00:0a:95:9d:68:16")
    simulator.rarp_request("00:0a:95:9d:68:99")