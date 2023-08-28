import sys

print("sys.platform:", sys.platform)

if sys.platform == "linux":
    print("We are on linux!")
    #if 1: #try:
        #import requests
        #raise Exception("Excepted to fail.")
    #except:

if sys.platform == "darwin":
    print("We are on Mac!")

if sys.platform == "nt":
    print("We are on Windows, oh no...")
