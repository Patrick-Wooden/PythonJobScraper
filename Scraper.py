import requests
from bs4 import BeautifulSoup
import pandas as pd




def scrape_jobs(url):
    # Fetch HTML content from target URL
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    
    jobs = []
    
    # Find all job posting cards on the page
    job_cards = soup.find_all("div",class_="card")
    
    for card in job_cards:
        # Extract individual fields from each job card
        job_title = card.find("h2", class_="title")
        job_company = card.find("h3", class_="company")
        job_location = card.find("p", class_="location")
        footer_links = card.find_all("a",  class_="card-footer-item")
        job_url = footer_links[1]["href"]  
    
        # Store the cleaned job data
        jobs.append({
            "title": job_title.get_text(strip=True) if job_title else "N/A",
            "company": job_company.get_text(strip=True) if job_company else "N/A",
            "location": job_location.get_text(strip=True) if job_location else "N/A",
            "url": job_url if job_url else "N/A"
        })
    
    return jobs
    

def main():
    
    url = "https://realpython.github.io/fake-jobs/"

    # Run the scraper
    results = scrape_jobs(url)    
    print(f"Scraped {len(results)} job postings")

    #Convert results into CSV file
    df = pd.DataFrame(results)
    df.to_csv("job_postings.csv", index=False)
    
    print("Saved job_postings.csv")
    
if __name__ == "__main__":
    main()