import logging
import requests
from scrappers.soup_generator import get_soup

base_url = "https://remoteok.io"


def get_url(query):
    return f"{base_url}/remote-dev+{query}-jobs"


def get_company_info(company):
    try:
        apply = company \
            .find("a", {"rel": ["noindex", "nofollow"]}) \
            .attrs["href"]

        link = base_url + company \
            .find("a", {"class": "companyLink"}) \
            .attrs["href"]

        if apply.startswith("/l/"):
            apply = base_url + apply
        else:
            apply = link

        logo = company \
            .find("img", {"itemprop": "image"}) \
            .attrs["src"]
        logo_type = "img"
        title = company \
            .find("h2", {"itemprop": "title"}) \
            .get_text(strip=True)
        name = company \
            .find("h3", {"itemprop": "name"}) \
            .get_text(strip=True)

        return (
            {
                "name": name,
                "link": link,
                "logo": logo,
                "logo_type": logo_type,
                "title": title,
                "apply": apply,
                "offer": ("Remote OK", base_url)
            }
        )

    except:
        return None


def extract_jobs(keyword):
    try:
        soup = get_soup(get_url(keyword))
        companies = soup.find_all("tr", {"class": "job"})

        jobs = []
        for company in companies:
            job = get_company_info(company)
            if job is not None:
                jobs.append(job)

        return jobs

    except Exception as error:
        print(error)
        return []
