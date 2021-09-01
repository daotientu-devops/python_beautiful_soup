from bs4 import BeautifulSoup
import requests
url = "https://realpython.github.io/fake-jobs/"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")
results = soup.find(id="ResultsContainer")
print(results.prettify())
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
python_jobs = results.find_all("h2", class_="title")
print(python_jobs)
# You're passing an anonymous function to the string argument. The lambda function looks at the text of each <h2> element,
# converts it to lowercase and checks whether the sybstring "python" is found anywhere
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
print(len(python_jobs))
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
for job_element in python_job_elements:
    links = job_element.find_all('a')
    for link in links:
        # Using ["href"] to extract
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")