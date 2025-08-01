import socket

def scan_ports(ip):
    open_ports = []
    try:
        for port in [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 8080]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        return "\n".join(f"Port {p} is open" for p in open_ports) or "No common ports open"
    except Exception as e:
        return f"Port scan failed: {e}"
