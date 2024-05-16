#!/usr/bin/python3

import re
import sys
import signal

# Initialize metrics
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

# Regular expression pattern to match the log line format
log_pattern = re.compile(
    r'^\d{1,3}(\.\d{1,3}){3} - \[.*?\] '
    r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
)


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


# Set up signal handler for keyboard interruption
signal.signal(signal.SIGINT, handle_interrupt)


def process_line(line):
    """Process a single line of input"""
    global total_file_size, line_count
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


# Read lines from stdin
try:
    for line in sys.stdin:
        process_line(line)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
finally:
    # Print final statistics
    print_statistics()
