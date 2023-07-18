# please run the command "pip install pyshorteners" for this to work

import pyshorteners

def shorten_url(url):
    # Create a Shortener object
    shortener = pyshorteners.Shortener()

    # Shorten the URL
    shortened_url = shortener.tinyurl.short(url)

    return shortened_url

def main():
    url = input("Enter the URL to shorten: ")
    shortened_url = shorten_url(url)
    print("Shortened URL:", shortened_url)

if __name__ == "__main__":
    main()
