# 
# Example file for retrieving data from the internet
#

import urllib.request

def main():
    weburl = urllib.request.urlopen("www.baidu.com")
    print("result code: " + str(weburl.getcode()) )
    data = weburl.read()
    print(data)


if __name__ == "__main__":
    main()
