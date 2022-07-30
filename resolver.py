import socket
import struct
import sys
import constants


def main():
    """
    """
    if len(sys.argv) == 2:
        print("Get IP Address")
        return 0
    elif len(sys.argv) == 3 and sys.argv[1] == "-m":
        print("Get Mail exchange server")
        return 0
    else:
        print(f'Usage: [{sys.argv[0]}] [-m] HOST_NAME')
        return 1


if __name__ == "__main__":
    sys.exit(main())

def get_root_servers(filename="root-servers.txt"):
    server_list = []
    with open(filename) as server_file:
        for server in server_file:
            server_list.append(server.rstrip("\n"))

    return server_list


