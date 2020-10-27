from scrappers.soup_generator import get_soup

base_url = "https://weworkremotely.com"


def get_url(query):
    return f"{base_url}/remote-jobs/search?term={query}"


def extract_company_logo(element):
    '''
    element = <div class="flag-logo" style="background-image:url(https://we-work-remotely.imgix.net/logos/0015/8605/logo.gif?ixlib=rails-4.0.0&amp;w=50&amp;h=50&amp;dpr=2&amp;fit=fill&amp;auto=compress)" loading="lazy"></div>
    '''
    try:
        style = element.attrs["style"]
        return style[21:-1]
    except Exception as error:
        raise error


def is_result_empty(soup):
    checker = soup.find("div", {"class": "no_results"})
    return bool(checker)


def get_company_info(company):
    try:
        logo_container = company.find("div", {"class": "tooltip"})
        logo = None
        logo_type = None
        link = None
        if logo_container is not None:
            logo = company.find("div", {"class": "flag-logo"})
            logo = extract_company_logo(logo)
            logo_type = "img"
            link = base_url + logo_container.find("a").attrs["href"]
        name = company.find("span", {"class": "company"}).get_text(strip=True)
        title = company.find("span", {"class": "title"}).get_text(strip=True)
        anchors = company.find_all("a")
        apply = anchors[-1].attrs["href"]
        if apply == "/top-remote-companies":
            apply = base_url + anchors[-2].attrs["href"]
        else:
            apply = base_url + apply

        return (
            {
                "name": name,
                "link": link or apply,
                "logo": logo,
                "logo_type": logo_type,
                "title": title,
                "apply": apply,
                "offer": ("We Work Remotely", f"{base_url}/remote-jobs")
            }
        )
    except BaseException as error:
        return None


def extract_jobs(keyword):
    try:
        soup = get_soup(get_url(keyword))
        if is_result_empty(soup):
            return []
        section = soup.find("section", id="category-2")
        companies = section.find_all("li")
        jobs = []
        for company in companies:
            job = get_company_info(company)
            if job is not None:
                jobs.append(job)

        return jobs
    except:
        return []
