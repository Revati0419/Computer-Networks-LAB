import socket
import sys

def resolve_hostname(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"IP address of {hostname}: {ip_address}")
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname '{hostname}'")

def main():
    if len(sys.argv) != 2:
        print("Usage: python resolve_hostname.py <hostname>")
        sys.exit(1)

    hostname = sys.argv[1]
    resolve_hostname(hostname)

if __name__ == "__main__":
    main()