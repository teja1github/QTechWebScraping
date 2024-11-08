from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that are not familier with')
unfamilier_skill=input('>')
print(f'Filtering out {unfamilier_skill}')

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date=job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            company_name=job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            skills_element = job.find('span', class_='srp-skills')
            if skills_element:
                skills = skills_element.text.replace(' ', '')
            else:
                skills = 'No skills listed'

            more_info=job.header.h2.a['href']
            if unfamilier_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name: {company_name.strip()}")
                    f.write(f"required Skills: {skills.strip()}")
                    f.write(f"More Info: {more_info}")
                print('File saved : {index}')
                
if __name__ =='__main__':
    while True:
        find_jobs()
        time_wait=1
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)
        

