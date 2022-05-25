import requests
from datetime import datetime
from datetime import timedelta


def extend_session(activity, session):
    """
    Its going to extend the session updating the data

    Args:
        activity: activity that extend the session
        session: sessions thats going to be extend
    return:
        sessions updated
    """
    if session["ended_at"] < activity["answered_at"]:
        session["ended_at"] = activity["answered_at"]
        session["duration_seconds"] = substract_times(
            session["ended_at"], session["started_at"]
        ).total_seconds()
    session["activity_ids"].append(activity["id"])
    return session


def substract_times(start, end):
    """
    substract 2 date time in format iso
    """
    return datetime.fromisoformat(start) - datetime.fromisoformat(end)


def add_session(activity):
    """
    Create a new session

    Args:
        activity: activity that start the new session
    return:
        new session
    """
    session = {
        "ended_at": activity["answered_at"],
        "started_at": activity["first_seen_at"],
        "activity_ids": [activity["id"]],
        "duration_seconds": (
            datetime.fromisoformat(activity["answered_at"])
            - datetime.fromisoformat(activity["first_seen_at"])
        ).total_seconds(),
    }
    return session


def check_session(activity, array_sessions):
    """
    Check if the activity is in the same session or in diferent

    Args:
        activity: activity thats need to be check
        array_sessions: sort array of sessions where the last is the last active session where check
    """
    if substract_times(
        activity["first_seen_at"], array_sessions[-1]["ended_at"]
    ) <= timedelta(minutes=5):
        array_sessions[-1] = extend_session(activity, array_sessions[-1])
    else:
        array_sessions.append(add_session(activity))
    return array_sessions


def create_user_session(activity):
    """
    create a new list of user sessions
    """
    return [add_session(activity)]


def check_users_groups(activity, dictionary):
    """
    Check if the user is in the dictionary, if not its going to add it.

    Args:
        activity: Activity of a user
        dictionary: dictionary in where check

    Return:
        dictionary adding the new user, or modifing the existing
    """
    if activity["user_id"] in dictionary:
        dictionary[activity["user_id"]] = check_session(
            activity, dictionary[activity["user_id"]]
        )
    else:
        dictionary[activity["user_id"]] = create_user_session(activity)
    return dictionary


def build_user_sessions(arr):
    """
    Build the new user sessions dictionary where
    is group by the user_id (Key of the dictionary), the value is an array of sessions.

    Args:
        arr: array of activities.

    return:
        dictionary with user sessions
    """
    arr = sorted(arr, key=lambda k: (k["user_id"], k["first_seen_at"]))
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
    user_sessions = {
        "user_sessions": build_user_sessions(activites_response_json.get("activities"))
    }
    requests.post(
        " https://api.slangapp.com/challenges/v1/activities/sessions",
        headers={
            "Authorization": "Basic OTM6Q3FtUnNPeHFHQmkySkpoYzNYazdOeDd2MStKbjBCV0JUMmxqRURLc1FMOD0="
        },
        json=user_sessions,
    )


main()
