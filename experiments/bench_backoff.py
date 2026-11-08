"""Backoff latency benchmark."""

import time

from nettlewood.resilience.backoff import BackoffConfig, next_delay


def bench(attempts=50):
    config = BackoffConfig(base_delay=0.01, max_delay=0.25)
    samples = []
    for attempt in range(attempts):
        samples.append(next_delay(attempt, config))
    return {"p95": sorted(samples)[int(len(samples) * 0.95) - 1], "samples": len(samples)}
