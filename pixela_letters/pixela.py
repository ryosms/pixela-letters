import os
from datetime import datetime, timedelta

import dotenv
import requests

from pixela_letters.date_converter import convert_to_ymd_string, find_last_start_date
from pixela_letters.letters import Letters
from pixela_letters.parameters import Parameters


def run():
    dotenv.load_dotenv()

    parameters = Parameters()
    parameters.parse(os.environ.get("PIXELA_USER"), os.environ.get("PIXELA_TOKEN"))

    letters = Letters()
    graphs = letters.create_quantities(parameters.poem)
    target_date = find_last_start_date(datetime.now() - timedelta(days=len(graphs)))
    endpoint = f"https://pixe.la/v1/users/{parameters.user_name}/graphs/{parameters.graph_name}"
    header = {"X-USER-TOKEN": parameters.token}

    for q in graphs:
        quantity = ((q * 4) + 1) * 5  # min: 5, max: 25
        date = convert_to_ymd_string(target_date)
        payload = {"date": f"{date}", "quantity": f"{quantity}"}
        response = requests.post(endpoint, headers=header, json=payload)
        print(f"{date}: {response.status_code}")
        target_date = target_date + timedelta(days=1)

    print("Finish")


if __name__ == "__main__":
    run()
