import requests
from typing import Dict, List, Any

def google_job_api(query: str, location: str, max_results: int = 5) -> List[Dict[str, str]]:
    api_key = "c48b63afb7252beb68424ace28f904566269c665a6de862413691490f55f636d"
    jobs: List[Dict[str, str]] = []
    results_per_page = 5
    pages = (max_results // results_per_page) + 1
    
    for page in range(pages):
        params: Dict[str, Any] = {
            "engine": "google_jobs",
            "q": query,
            "hl": "en",
            "location": location,
            "google_domain": "google.com",
            "api_key": api_key,
            "no_cache": True,
            "start": page * results_per_page
        }

        response = requests.get(url='https://serpapi.com/search', params=params)
        data = response.json()
        results = data.get("jobs_results", [])

        for result in results:
            job = {}
            job["title"] = result.get("title")
            job["company_name"] = result.get("company_name")
            job["location"] = result.get("location", None)
            job["link"] = result.get("related_links", [{}])[0].get("link", None)
            job["image"] = result.get("thumbnail", None)
            job["schedule_type"] = result.get("detected_extensions", {}).get("schedule_type")

            salary = result.get("detected_extensions", {}).get("salary")
            if salary:
                job["salary"] = process_salary(salary, job["schedule_type"])
            else:
                job["salary"] = None
            
            jobs.append(job)
        
        if not results:
            break

    return jobs

def convert_to_hourly(salary_str):
    salary_float = float(salary_str) if "." in salary_str else int(salary_str)
    return round(salary_float / 2080, 2)


def process_salary(salary: str, schedule_type: str) -> str:
    if schedule_type != "Full-time":
        return None

    if "a year" not in salary:
        return f"€ {salary}"

    yearly_salary = salary.replace(" a year", "").replace("K", "000").replace(",", "")
    min_max_salary = []

    if "-" in yearly_salary:
        min_max_salary = yearly_salary.split("-")
    elif "–" in yearly_salary:
        min_max_salary = yearly_salary.split("–")

    if min_max_salary:
        min_salary = convert_to_hourly(min_max_salary[0])
        max_salary = convert_to_hourly(min_max_salary[1])
        return f"€ {min_salary} - {max_salary} an hour"
    else:
        hourly_salary = convert_to_hourly(yearly_salary)
        return f"€ {hourly_salary} an hour"
