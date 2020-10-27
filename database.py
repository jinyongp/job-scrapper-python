from scrappers import \
    remote_ok as ro, \
    stack_overflow as so, \
    we_work_remotely as ww

db = {}


def get_jobs(keyword):
    if keyword in db:
        return db[keyword]
    else:
        jobs = ro.extract_jobs(keyword)
        jobs += so.extract_jobs(keyword)
        jobs += ww.extract_jobs(keyword)
        db[keyword] = jobs
        return jobs
