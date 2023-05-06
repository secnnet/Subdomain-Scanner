import argparse
import socket

def main():
    parser = argparse.ArgumentParser(description="Scan subdomains of a domain")
    parser.add_argument("domain", help="The domain to scan")
    args = parser.parse_args()

    subdomains = ["www", "mail", "ftp", "blog", "admin", "dev", "webmail", "api", "cdn", "store", "forum", "wiki", "shop", "test"]

    for subdomain in subdomains:
        url = f"{subdomain}.{args.domain}"

        try:
            socket.gethostbyname(url)
            print(f"[+] Found subdomain: {url}")
        except socket.error:
            pass

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
