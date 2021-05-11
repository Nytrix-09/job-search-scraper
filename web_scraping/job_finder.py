import time
import requests
from bs4 import BeautifulSoup

job_skill = ""
print("Pls Enter Job Profile for Job Search")
job_profile = input(">")
for letter in job_profile:
    if(letter == " "):
        job_skill = job_skill+"+"
    job_skill += letter
job_skill.replace(" ", "")
print("Add an Industry Skill not familiar with (max 2):")
print("Enter 'null' if not applicable")
dunno_skill = input(">Unfimiliar Skill 1:")
dunno_skill2 = input(">Unfimiliar Skill 2:")
print("Filtering jobs posted in last few days...")
print(f'Filters Applicable : {dunno_skill} & {dunno_skill2}')


def job_finder():
    html_text = requests.get(
        f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={job_skill.strip()}&txtLocation=").text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find(
                'h3', class_='joblist-comp-name').text.strip()
            key_skills = job.find('span', class_='srp-skills').text.strip()
            details = job.header.h2.a['href']

            if dunno_skill == "null" and dunno_skill2 == "null":
                with open(f'jobs/ {index}.txt', 'w') as f:
                    f.write(f"Comapny name: {company_name.strip()}")
                    f.write(f"Required Skills: {key_skills.strip()}")
                    f.write(f'Additional Info: {details}')
                print(f'File Saved... {index}')

            if dunno_skill not in key_skills and dunno_skill2 == "null":
                with open(f'jobs/ {index}.txt', 'w') as f:
                    f.write(f"Comapny name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {key_skills.strip()} \n")
                    f.write(f'Additional Info: {details}')
                print(f'File Saved... {index}')

            elif dunno_skill2 not in key_skills and dunno_skill == "null":
                with open(f'jobs/ {index}.txt', 'w') as f:
                    f.write(f"Comapny name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {key_skills.strip()} \n")
                    f.write(f'Additional Info: {details}')
                print(f'File Saved... {index}')

            elif dunno_skill and dunno_skill2 not in key_skills:
                with open(f'jobs/ {index}.txt', 'w') as f:
                    f.write(f"Comapny name: {company_name.strip()}")
                    f.write(f"Required Skills: {key_skills.strip()}")
                    f.write(f'Additional Info: {details}')
                print(f'File Saved... {index}')


if __name__ == '__main__':
    while True:
        job_finder()
        time_wait = 15
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)
