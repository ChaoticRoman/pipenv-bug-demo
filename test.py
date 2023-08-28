import sys

print("sys.platform:", sys.platform)

if sys.platform == "linux":
    import requests
    print("Import works!")
    exit(0)

try:
    import requests
    raise Exception("Expected to fail.")
except ImportError:
    print("Import failed as expected")
