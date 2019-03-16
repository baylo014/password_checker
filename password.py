import sys
import requests
import hashlib

def main():
    sha = hashlib.sha1(bytes(" ".join(sys.argv[1:]), 'utf-8')).hexdigest()
    suffix = sha[0:5]
    r = requests.get(url = "https://api.pwnedpasswords.com/range/"+suffix)
    #TODO: Figure out how to remove the last char from the 2nd array element for each return
    # Essentially do what is on line 14:47-64 on line 11:34-46
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
