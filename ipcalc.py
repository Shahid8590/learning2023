import ipaddress

def calculate_subnet(ip, subnet_mask):
    # Parse the IP address and subnet mask
    ip_address = ipaddress.IPv4Address(ip)
    subnet = ipaddress.IPv4Network(f'{ip}/{subnet_mask}', strict=False)

    # Get network details
    network_address = subnet.network_address
    broadcast_address = subnet.broadcast_address
    total_ips = subnet.num_addresses
    usable_ips = total_ips - 2  # Subtract network and broadcast addresses

    # Convert addresses to string representation
    network_address_str = str(network_address)
    broadcast_address_str = str(broadcast_address)

    return {
        "Network Address": network_address_str,
        "Broadcast Address": broadcast_address_str,
        "Total IPs": total_ips,
        "Usable IPs": usable_ips
    }

# Input IP address and subnet mask
ip_address = input("Enter IP address (e.g., 192.168.1.1): ")
subnet_mask = int(input("Enter subnet mask (e.g., 25 for /25): "))


# Calculate subnet information
subnet_info = calculate_subnet(ip_address, subnet_mask)

# Display subnet information
for key, value in subnet_info.items():
    print(f"{key}: {value}")
