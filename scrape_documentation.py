import requests, re
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def main():
    
    versions = []
    num_mentions = []
    for minor in range(0, 14):
        n_error = 0
        version = "3." +  str(minor)

        page = requests.get(f"https://docs.python.org/3/whatsnew/{version}.html")
        
        soup = BeautifulSoup(page.content, "html.parser")

        results_err = soup.find_all(string=re.compile("error", re.IGNORECASE))
        results_exc = soup.find_all(string=re.compile("exception", re.IGNORECASE))

        n_error += len(results_err)
        n_error += len(results_exc)
        
        print(version, n_error)
        versions.append(version)
        num_mentions.append(n_error)
            
    plt.figure(figsize=(10, 8))
    plt.style.use("fivethirtyeight")
    
    plt.bar(versions, num_mentions)
    
    plt.xlabel("Python 3 Versions")
    plt.ylabel("Mentions of either 'error' or 'exception'")  
    
    plt.subplots_adjust(left=0.15, right=1, top=0.85, bottom=0.15)
    plt.savefig("p3_err.png", bbox_inches='tight')
    

if __name__ == "__main__":
    main()
