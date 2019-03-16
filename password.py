import sys
import requests
import hashlib

def main():
    sha = hashlib.sha1(bytes(" ".join(sys.argv[1:]), 'utf-8')).hexdigest()
    suffix = sha[0:5]
    r = requests.get(url = "https://api.pwnedpasswords.com/range/"+suffix)
    dataList = list(map(lambda x:x.split(":"),r.text.split("\n")))
    for item in dataList:
        if (sha[5:].upper() in item):
            print("Found " + sha + " w/ + " + str(item[1][:-1]) + " breaches")
            return
    print("None found. For now")

if __name__ == '__main__':
    if (len(sys.argv) >= 2):
        main()
    else:
        print("Invalid format")
        print("Use 'python(3) password.py {password to check}'")
