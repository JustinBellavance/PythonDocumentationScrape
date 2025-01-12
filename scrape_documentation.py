import requests, re
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def main():
    
    versions = []
    num_mentions = []
    # version 2
    for minor in range(0, 8):
        n_error = 0
        version = "2." +  str(minor)

        page = requests.get(f"https://docs.python.org/2/whatsnew/{version}.html")
        
        soup = BeautifulSoup(page.text, "html.parser")
        
        # Extract all text from the page
        text = soup.get_text()

        # Split the text into words and count them
        words = text.split()

        # Count the total number of words
        word_count = len(words)

        results_err = soup.find_all(string=re.compile("error", re.IGNORECASE))
        # results_exc = soup.find_all(string=re.compile("exception", re.IGNORECASE))

        n_error += len(results_err)
        # n_error += len(results_exc)
        
        print(version, round(n_error / word_count * 100, 2))
        versions.append(version)
        num_mentions.append(round(n_error / word_count * 100, 2))
    
    # version 3
    for minor in range(0, 14):
        n_error = 0
        version = "3." +  str(minor)

        page = requests.get(f"https://docs.python.org/3/whatsnew/{version}.html")
        
        soup = BeautifulSoup(page.text, "html.parser")
        
        # Extract all text from the page
        text = soup.get_text()

        # Split the text into words and count them
        words = text.split()

        # Count the total number of words
        word_count = len(words)

        results_err = soup.find_all(string=re.compile("error", re.IGNORECASE))
        # results_exc = soup.find_all(string=re.compile("exception", re.IGNORECASE))

        n_error += len(results_err)
        # n_error += len(results_exc)
        
        print(version, round(n_error / word_count * 100, 2))
        versions.append(version)
        num_mentions.append(round(n_error / word_count * 100, 2))
            
    plt.figure(figsize=(14, 8))
    plt.style.use("fivethirtyeight")
    
    plt.bar(versions, num_mentions)
    
    plt.xlabel("Python 3 Versions")
    plt.ylabel("'error' mentions per word (%)")  
    
    plt.subplots_adjust(left=0.15, right=1, top=0.85, bottom=0.15)
    plt.savefig("p3_err.png", bbox_inches='tight')
    

if __name__ == "__main__":
    main()
