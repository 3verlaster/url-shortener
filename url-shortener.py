# -*- coding: utf-8 -*-
import argparse
import requests
try:
    from pyperclip import copy as pcopy
except:
    print('Failed to import module "pyperclip"\nInstall it with the command:\npip install pyperclip')
    pass

print("URL Shortener [v1.0.0] by https://github.com/3verlaster")

def spcopy(pUrl):
    try:
        pcopy(pUrl)
        print("The link was successfully copied to the clipboard")
    except:
        print("Failed to copy URL to clipboard. [TERMUX?]")


def main():
    parser = argparse.ArgumentParser(description="Print a URL")
    parser.add_argument("-u", "--url", type=str)
    
    args = parser.parse_args()
    if args.url:
        #args.url
        print()
        print("[WARNING] v.gd domain is not recommended because warns that the link may be dangerous")
        print()
        print("1 - v.gd | 2 - is.gd")
        hMethod = input(str("Please select a domain: "))
        if hMethod == "1":
            hSelectedDomainAPI = "https://v.gd/create.php"
            params = {
                "format": "json",
                "url": args.url
            }
            response = requests.get(hSelectedDomainAPI, params=params)
            if response.status_code == 200:
                print("[v.gd API] - [*] Data send succefully...")
                print("[v.gd API] - [*] Reading response...")
                data = response.json()
                hShortURL = data.get("shorturl")
                print("Here's your shortened link:", hShortURL)
                spcopy(hShortURL)
            else:
                print("Request error:", response.status_code)
        elif hMethod == "2":
            hSelectedDomainAPI = "https://is.gd/create.php"
            params = {
                "format": "json",
                "url": args.url
            }
            response = requests.get(hSelectedDomainAPI, params=params)
            if response.status_code == 200:
                print("[is.gd API] - [*] Data send succefully...")
                print("[is.gd API] - [*] Reading response...")
                data = response.json()
                hShortURL = data.get("shorturl")
                print("Here's your shortened link:", hShortURL)
                spcopy(hShortURL)
            else:
                print("Request error:", response.status_code)
        else:
            print("Unkown domain selected. Try again!")
    else:
        print("No URL provided!\nExample:\npython url-shortener.py -u example.com")

if __name__ == "__main__":
    main()
