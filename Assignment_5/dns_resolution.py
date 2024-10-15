import socket

def resolve_domain():
    # Prompt the user to enter a domain name
    domain = input("Enter the domain name: ")

    try:
        # Get the list of addresses associated with the domain
        addr_info = socket.getaddrinfo(domain, None)

        # Extract and print the IP addresses from the addr_info
        print(f"IP addresses associated with {domain}:")
        for result in addr_info:
            ip_address = result[4][0]
            print(ip_address)

    except socket.gaierror:
        print(f"Error: Unable to resolve domain '{domain}'")

if __name__ == "__main__":
    resolve_domain()
