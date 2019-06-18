import sys

lines = sys.stdin.readlines()

# We get the last time from clingo's output (CPU Time: XXXs), grab the time, and remove the s.
print(lines[-1].split(':')[1][:-2])