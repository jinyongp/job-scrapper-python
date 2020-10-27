from scrappers.soup_generator import get_soup

base_url = "https://stackoverflow.com"


def get_url(query, id="", page="1"):
    return f"{base_url}/jobs?r=true&id={id}&q={query}&pg={page}"


def get_company_info(company):
    try:
        logo = company.find("img") or company.find("svg")
        logo_type = "img"
        if logo.name == "img":
            logo = logo.attrs["src"]
        else:
            logo_type = "svg"
        anchor = company .find("a", {"class": "stretched-link"})
        title = anchor.attrs["title"]
        apply = f"{base_url}" + anchor.attrs["href"]
        name = company.find("h3").find("span").get_text(strip=True)

        return (
            {
                "name": name,
                "link": apply,
                "logo": logo,
                "logo_type": logo_type,
                "title": title,
                "apply": apply,
                "offer": ("Stack Overflow", f"{base_url}/jobs")
            }
        )

    except BaseException as error:
        print(error)
        return None


def is_result_empty(soup):
    checker = soup.find("div", {"class": "s-empty-state"})
    return bool(checker)


def extract_jobs(keyword):
    try:
        soup = get_soup(get_url(keyword))

        jobs_number = soup \
            .find_all("span", {"class": ["description", "fc-light", "fs-body1"]})[-1]  \
            .get_text(strip=True)[:-4]
        jobs_number = int(jobs_number)

        if is_result_empty(soup):
            return []
        companies = soup.find_all("div", {"class": "-job"})
        jobs = []
        for company in companies:
            if not jobs_number:
                break
            jobs_number -= 1
            job = get_company_info(company)
            if job is not None:
                jobs.append(job)

        return jobs

    except BaseException as error:
        print(error)
        return []
