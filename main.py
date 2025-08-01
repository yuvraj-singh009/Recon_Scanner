import os
import sys
from modules import dns_lookup, whois_info, port_scan, ssl_info, vuln_scan

def run_scan(target):
    os.makedirs("output", exist_ok=True)
    output_path = f"output/scan_report_{target.replace('.', '_')}.txt"
    with open(output_path, "w") as f:
        f.write(f"*** Reconnaissance Report for {target} ***\n\n")

        f.write("===== WHOIS INFO =====\n")
        f.write(whois_info.get_whois(target) + "\n\n")

        f.write("===== DNS INFO =====\n")
        f.write(dns_lookup.get_dns_records(target) + "\n\n")

        f.write("===== PORT SCAN =====\n")
        f.write(port_scan.scan_ports(target) + "\n\n")

        f.write("===== SSL CERTIFICATE INFO =====\n")
        f.write(ssl_info.get_ssl_info(target) + "\n\n")

        f.write("===== BASIC VULNERABILITY SCAN =====\n")
        f.write(vuln_scan.basic_vuln_scan(target) + "\n\n")

    print(f"\n✅ Scan complete. Output saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <target IP or domain>")
        sys.exit(1)
    run_scan(sys.argv[1])

