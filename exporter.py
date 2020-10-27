import csv


def export_to_csv(headers, rows, filename):
    try:
        file = open(f"outputs/{filename}.csv", mode="w")
        writer = csv.writer(file)
        writer.writerow(headers)
        for row in rows:
            writer.writerow(row)
        return "Export Complete"
    except Exception as error:
        print(error)
        return None
