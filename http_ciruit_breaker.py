

class CircuitBreaker:
    def __init__(self, max_failures, timeout):
        self.max_failures = max_failures
        self.timeout = timeout
        self.failures = 0
        self.last_failure = 0

    def do_request(self):
        if self.failures > self.max_failures:
            if time.time() - self.last_failure > self.timeout:
                self.failures = 0
        else:
            self.failures += 1
            self.last_failure = time.time()


if __name__ == "__main__":
    breaker = CircuitBreaker(3, 5)
    for i in range(10):
        breaker.do_request()
        print(breaker.failures)
