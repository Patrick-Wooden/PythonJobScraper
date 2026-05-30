# PythonJobScraper

This is a simple web scraper that collects job listings from the [Fake Python Jobs](https://realpython.github.io/fake-jobs/) website and saves the result to a CSV file.

# Features
- Scrapes job posting getting the title, company, location and job detail URL.
- Exports the job postings to CSV format so it can be easily analyized 
- Handles missing data
- Clean easy to understand code structure

# Requirements
- Python 3.x
- requests
- beautifulsoup4
- pandas

# Installation
```bash
    pip install requests beautifulsoup4 pandas
```
# Usage

Simply run the script:
```bash
python main.py
```
The scraped job postings will then be saved to  `data/job_postings.csv`
