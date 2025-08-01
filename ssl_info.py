import ssl
import socket

def get_ssl_info(domain):
    try:
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(), server_hostname=domain)
        conn.settimeout(3)
        conn.connect((domain, 443))
        cert = conn.getpeercert()
        result = f"Issuer: {cert['issuer']}\n"
        result += f"Valid from: {cert['notBefore']}\n"
        result += f"Valid until: {cert['notAfter']}\n"
        result += f"Subject: {cert['subject']}\n"
        conn.close()
        return result
    except Exception as e:
        return f"SSL scan failed: {e}"
