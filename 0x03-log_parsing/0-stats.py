#!/usr/bin/python3
import sys
import signal
import re


total_file_size = 0
status_code_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
}
line_count = 0

log_pattern = re.compile(r'^\d{1,3}(\.\d{1,3}){3} - \[.*?\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')


def print_statistics():
    """Print the computed statistics."""
    global total_file_size, status_code_counts
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def handle_interrupt(signum, frame):
    """Handle keyboard interrupt signal."""
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

for line in sys.stdin:
    match = log_pattern.match(line.strip())
    if match:
        status_code = int(match.group(2))
        file_size = int(match.group(3))

        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_statistics()

print_statistics()
