import requests


def test_check_access_admin(url):
    endpoint = "api/user-access"

    test_cases = [
        {"data": {"Username": "joe", "role": "admin"}, "expected": "True"},
        {"data": {"Username": "jane", "role": "manager"}, "expected": "True"},
        {"data": {"Username": "joe", "role": "developer"}, "expected": "False"},
        {"data": {"Username": "", "role": "admin"}, "expected": "False"},
        {"data": {"Username": "", "role": ""}, "expected": "False"},
    ]

    for case in test_cases:
        r = requests.post(f"{url}/{endpoint}", json=case["data"], verify=False)
        assert r.json() == {"hasAccess": case["expected"]}


# pytest -p no:typhoon
