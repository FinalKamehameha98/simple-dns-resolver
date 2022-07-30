import socket
import struct
import sys
import constants
import enum

class DNSType(enum.Enum):
    A = 1
    NS = 2
    CNAME = 5
    SOA = 6
    MX = 15


def main():
    """
    """
    if len(sys.argv) == 2:
        print("Get IP Address")
        resolve_hostname(sys.argv[1])
        return 0
    elif len(sys.argv) == 3 and sys.argv[1] == "-m":
        print("Get Mail exchange server")
        resolve_hostname(DNSType.MX, sys.argv[2])
        return 0
    else:
        print(f'Usage: [{sys.argv[0]}] [-m] HOST_NAME')
        return 1


def resolve_hostname(dns_type=DNSType.A, hostname=""):
    root_servers = get_root_servers(constants.ROOT_SERVERS_FILE)
    dns_socket = get_socket()

    for server in root_servers:
        query = make_query(dns_type, hostname)
        try:
            #dns_socket.sendto(query, (server, constants.DNS_PORT))
            #packed_bytes = dns_socket.recvfrom(constants.BUFF_MAX_SIZE)[0]
        except socket.timeout as e:
            print(f'No response from {server}.')
            print("Trying next server...\n")

    if len(packed_bytes) < 0:
        sys.exit("Packed bytes error")
    else:
        print("Packed bytes recv'd")

    dns_socket.close()


def get_root_servers(filename=constants.ROOT_SERVERS_FILE):
    """


    """
    server_list = []
    with open(filename) as server_file:
        for server in server_file:
            server_list.append(server.rstrip("\n"))

    return server_list


def get_socket():
    """

    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    sock.settimeout(constants.TIMEOUT_VAL)
    return sock

def make_query(dns_type=DNSType.A, hostname=""):
    """
    """
    pass

if __name__ == "__main__":
    sys.exit(main())
