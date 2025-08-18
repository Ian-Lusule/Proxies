import requests
import os

# Dictionary of raw GitHub URLs for different proxy types
proxy_sources = {
    'http': [
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"
    ],
    'socks4': [
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt"
    ],
    'socks5': [
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"
    ]
}

def fetch_and_write_proxies():
    all_proxies = set()
    output_dir = "proxies"
    os.makedirs(output_dir, exist_ok=True)

    for proxy_type, urls in proxy_sources.items():
        type_proxies = set()
        for url in urls:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    proxies = response.text.strip().split('\n')
                    type_proxies.update(proxies)
            except requests.RequestException as e:
                print(f"Failed to fetch {url} for {proxy_type} proxies: {e}")

        # Save to individual proxy type file
        if type_proxies:
            file_path = os.path.join(output_dir, f'{proxy_type}.txt')
            with open(file_path, 'w') as f:
                for proxy in sorted(list(type_proxies)):
                    f.write(f'{proxy}\n')
            print(f"Saved {len(type_proxies)} {proxy_type} proxies to {file_path}")
            all_proxies.update(type_proxies)

    # Consolidate, sort, and save all proxies
    if all_proxies:
        all_proxies_file = os.path.join(output_dir, 'all_proxies.txt')
        with open(all_proxies_file, 'w') as f:
            for proxy in sorted(list(all_proxies)):
                f.write(f'{proxy}\n')
        print(f"Consolidated and saved {len(all_proxies)} unique proxies to {all_proxies_file}")

if __name__ == '__main__':
    fetch_and_write_proxies()
