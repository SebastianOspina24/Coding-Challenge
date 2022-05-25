import requests


def main():
    activites_response = requests.get(
        "https://api.slangapp.com/challenges/v1/activities",
        headers={
            "Authorization": "Basic OTM6Q3FtUnNPeHFHQmkySkpoYzNYazdOeDd2MStKbjBCV0JUMmxqRURLc1FMOD0="
        },
    )
    activites_response_json = activites_response.json()
    print(activites_response_json)
    requests.post(
        " https://api.slangapp.com/challenges/v1/activities/sessions",
        headers={
            "Authorization": "Basic OTM6Q3FtUnNPeHFHQmkySkpoYzNYazdOeDd2MStKbjBCV0JUMmxqRURLc1FMOD0="
        },
        json=activites_response_json,
    )


main()
