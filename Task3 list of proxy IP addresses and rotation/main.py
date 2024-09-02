import requests
from proxy_manager import ProxyManager

# List of proxy IP addresses
proxy_list = [
    "http://51.79.50.31:9300",   # Free proxy IP 1
    "http://104.248.63.17:8080",  # Free proxy IP 2
    "http://123.456.78.90:8080",  # Free proxy IP 3 (example IP, may not be valid)
    "http://192.241.245.207:8080", # Free proxy IP 4
    "http://188.166.83.24:8080",  # Free proxy IP 5
    "http://159.203.116.41:8080",  # Free proxy IP 6
    "http://45.77.24.222:8080",  # Free proxy IP 7
    "http://103.55.49.124:8080",  # Free proxy IP 8
    "http://185.107.232.226:8080",  # Free proxy IP 9
    "http://34.143.95.104:8080",  # Free proxy IP 10
]

# Initialize ProxyManager
proxy_manager = ProxyManager(proxy_list)

def make_request(url):
    proxy = proxy_manager.get_proxy()
    proxies = {"http": proxy, "https": proxy}
    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        print(f"Response from {proxy}: {response.json()}")
    except requests.RequestException as e:
        print(f"Request failed for {proxy}: {e}")

if __name__ == "__main__":
    # Example URL to make requests to
    target_url = "https://httpbin.org/get"
    
    # Making multiple requests
    for _ in range(30):  # Adjust the number of requests as needed
        make_request(target_url)

