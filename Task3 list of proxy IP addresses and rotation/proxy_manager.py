from collections import defaultdict
import random

class ProxyManager:
    def __init__(self, proxies):
        self.proxies = proxies
        self.request_counts = defaultdict(int)
        self.max_requests_per_proxy = 10

    def get_proxy(self):
        available_proxies = [proxy for proxy in self.proxies if self.request_counts[proxy] < self.max_requests_per_proxy]
        if not available_proxies:
            raise Exception("No available proxies left with request limits not reached")
        selected_proxy = random.choice(available_proxies)
        self.request_counts[selected_proxy] += 1
        return selected_proxy

