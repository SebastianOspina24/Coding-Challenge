import requests


def build_user_sessions(arr):
    """
    Build the new user sessions dictionary where
    is group by the user_id (Key of the dictionary), the value is an array of sessions.

    Args:
        arr: array of activities.
    """
    user_sessions = dict()
    for i in arr:
        user_sessions = check_users_groups(i, user_sessions)
    return user_sessions


def main():
    """
    fetch information from api, then build a dictionary with the
    user sessions and post it.
    """
    activites_response = requests.get(
        "https://api.slangapp.com/challenges/v1/activities",
        headers={
            "Authorization": "Basic OTM6Q3FtUnNPeHFHQmkySkpoYzNYazdOeDd2MStKbjBCV0JUMmxqRURLc1FMOD0="
        },
    )
    activites_response_json = activites_response.json()
    print(activites_response_json)
    # requests.post(
    #     " https://api.slangapp.com/challenges/v1/activities/sessions",
    #     headers={
    #         "Authorization": "Basic OTM6Q3FtUnNPeHFHQmkySkpoYzNYazdOeDd2MStKbjBCV0JUMmxqRURLc1FMOD0="
    #     },
    #     json=activites_response_json,
    # )


main()
