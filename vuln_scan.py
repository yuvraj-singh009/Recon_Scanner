import subprocess

def basic_vuln_scan(target):
    try:
        result = subprocess.check_output(["nmap", "--script", "vuln",  target], stderr=subprocess.STDOUT, text=True)
        return result
    except Exception as e:
        return f"Nmap vuln scan failed: {e}"
