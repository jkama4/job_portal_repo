import requests
from typing import Dict, List, Any

def google_job_api(query: str, location: str, max_results: int = 5) -> List[Dict[str, str]]:
    """Function that reaches out to SerpAPI using an API key to gather data (JSON) from Google Jobs.
    param: query (str): The search query given by the user.
    param: location (str): The location given by the user.
    param: max_results (int): The maximum number of job listings to fetch. Defaults to 5.
    return: a list of jobs, where each job is a dictionary
    """
    api_key = "866adaf9f3d141423a14b4223599732c5ba7c1da3586b9efc42bc276003e0d59"
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

def convert_to_hourly(salary_str: str) -> float:
    """ Converts a yearly salary string to an hourly rate.
        param: salary_str (str): The yearly salary as a string, which can be a float or an integer.
        return: The equivalent hourly salary, rounded to two decimal places.
    """
    salary_float = float(salary_str) if "." in salary_str else int(salary_str)
    return round(salary_float / 2080, 2)


def process_salary(salary: str, schedule_type: str) -> str:
    """ Processes the salary string and converts it to an hourly rate if applicable.
        param: salary (str): The salary string, which may include yearly salary information.
        param: schedule_type (str): The schedule type of the job (e.g., full-time, part-time).
        return: The processed salary string as an hourly rate if the job is full-time and the salary is given in yearly terms, otherwise returns None.
    """
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
