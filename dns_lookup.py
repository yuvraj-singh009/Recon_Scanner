import dns.resolver

def get_dns_records(domain):
    try:
        result = ""
        for qtype in ['A', 'MX', 'NS', 'TXT']:
            answers = dns.resolver.resolve(domain, qtype, raise_on_no_answer=False)
            result += f"{qtype} Records:\n"
            for rdata in answers:
                result += f" - {rdata.to_text()}\n"
        return result
    except Exception as e:
        return f"DNS lookup failed: {e}"
