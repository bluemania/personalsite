import os
from operator import itemgetter


def get_file_details(filename):

    try:
        details, filetype = filename.split(".")

        date, major_type, title, tags = details.split("_")

        title_cap = title.replace("-"," ").capitalize()

        if tags:
            tags = tags.split("-")
        else:
            tags = []

        year, month, day = date.split("-")

        if month in ["01", "02", "03", "04"]:
            period = f"{year}_early"
        elif month in ["05", "06", "07", "08"]:
            period = f"{year}_mid"
        elif month in ["09", "10", "11", "12"]:
            period = f"{year}_late"
        else:
            period = None

        url_helper = f"{major_type}/{year}/{month}/{day}/{title}"

        article = open_article(filename)

        return {"filename": filename, "date": date, "major_type": major_type, "title": title, "tags": tags, "year": year, 
                "month": month, "day": day, "period": period, "filename": filename, "filetype": filetype, 
                "title_cap": title_cap, "url_helper": url_helper, "teaser": article[0], "article": article}

    except:
        return None

def open_article(filename):
    with open(os.path.join("local", filename), 'r') as f:
        article = f.readlines()
    return article



def get_all_files():
    files = [get_file_details(x) for x in os.listdir("local")]
    return files


def parse_files_and_filters(filters):
    files = get_all_files()

    for key, value in filters.items():
        if files:
            if value:
                if key=="tags":
                    files = [x for x in files if value in x[key]]
                else:
                    files = [x for x in files if x[key]==value]

    files = sorted(files, key=itemgetter('date'), reverse=True)

    return files

