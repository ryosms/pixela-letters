import os
from datetime import datetime, timedelta

import dotenv
import requests

from pixela_letters.date_converter import find_last_monday, convert_to_ymd_string


def run():
    dotenv.load_dotenv()
    user_name = os.environ.get('PIXELA_USER')
    token = os.environ.get('PIXELA_TOKEN')
    graph_name = "hoge"

    graphs = []
    target_date = find_last_monday(datetime.now() - timedelta(days=len(graphs)))
    endpoint = f"https://pixe.la/v1/users/{user_name}/graphs/{graph_name}"
    header = {'X-USER-TOKEN': token}

    for q in graphs:
        date = convert_to_ymd_string(target_date)
        payload = {'date': f"{date}", 'quantity': f"{q}"}
        response = requests.post(endpoint, headers=header, json=payload)
        print(f"{date}: {response.status_code}")
        target_date = target_date + timedelta(days=1)

    print("Finish")


if __name__ == '__main__':
    run()
