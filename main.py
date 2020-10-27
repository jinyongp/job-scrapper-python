import os
import database
from flask import Flask, render_template, request, redirect, send_file
from exporter import export_to_csv

os.system("clear")

"""
Auto Reloading on Save

$ FLASK_APP=main.py FLASK_ENV=development flask run
"""

app = Flask("FinalChallenge")


@app.route("/")
def home():
    """ Main Page Route """

    return render_template(
        "home.html"
    )


@app.route("/search")
def search():
    """Search Result Page Route"""
    keyword = request.args.get("keyword")

    if not keyword:
        return redirect("/")
    keyword = keyword.lower()
    jobs = database.get_jobs(keyword)

    return render_template(
        "search.html",
        jobs=jobs,
        keyword=keyword,
    )


@app.route("/export")
def export():
    """Export to CSV Route"""
    try:
        keyword = request.args.get("keyword")
        keyword = keyword.lower()
        jobs = database.get_jobs(keyword)
        if not jobs:
            raise Exception(f"No {keyword} jobs in database")

        export_to_csv(
            ["Title", "Company", "Link"],
            [[job["title"], job["name"], job["apply"]] for job in jobs],
            keyword
        )

        return send_file(
            f"outputs/{keyword}.csv",
            mimetype="application/x-csv",
            attachment_filename=f"{keyword}.csv",
            as_attachment=True
        )
    except BaseException as error:
        print(error)
        return redirect("/")


app.run(host="0.0.0.0")
