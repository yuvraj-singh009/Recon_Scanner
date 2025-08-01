import whois

def get_whois(domain):
    try:
        info = whois.whois(domain)
        return str(info)
    except Exception as e:
        return f"WHOIS lookup failed: {e}"
