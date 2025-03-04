import unittest
from datetime import datetime, timedelta

MAX_TOKEN = 6

def solution(user_info, data_info):
    answer = {}
    for user in user_info:
        answer[user] = MAX_TOKEN
    time = datetime.strptime("00:00:00", "%H:%M:%S")

    for data in data_info:
        user = data[0]
        info = data[1]
        request_time = datetime.strptime(data[2], "%H:%M:%S")
        diff_min = (request_time - time).seconds // 60

        if  diff_min > 0:
            time += timedelta(minutes=diff_min)
            answer = token_update(answer,user_info, diff_min)

        if answer[user] > 0 and info == "request":
            answer[user] -= 1
    return answer

def token_update(answer, user_info, token_number):
    for user in user_info:
        if answer[user] + token_number >= MAX_TOKEN:
            answer[user] = MAX_TOKEN
        else:
            answer[user] += token_number
    return answer

class TestTokenBucket(unittest.TestCase):
    def test01(self):
        user_info = ["A","B","C"]
        data_info = [
            ["A","request","00:00:00"],
            ["B", "request", "00:00:20"],
            ["A", "request", "00:00:30"],
            ["A", "request", "00:00:40"],
            ["A", "delete", "00:00:50"],
            ["A", "request", "00:01:00"],
            ["A", "delete", "00:01:10"],
            ["A", "request", "00:01:20"],
            ["B", "request", "00:01:30"],
            ["C", "request", "00:01:40"],
            ["C", "request", "00:01:50"],
        ]
        answer = {"A":2,"B":5,"C":4}
        result = solution(user_info, data_info)
        assert result == answer

    def test02(self):
        user_info = ["A","B","C"]
        data_info = [
            ["A","request","00:00:00"],
            ["B", "request", "00:01:20"],
            ["A", "request", "00:03:30"],
            ["A", "request", "00:05:40"],
            ["A", "request", "00:06:40"],
        ]
        answer = {"A":5,"B":6,"C":6}
        result = solution(user_info, data_info)
        assert result == answer

    def test03(self):
        user_info = ["A","B","C"]
        data_info = [
            ["A","request","00:00:00"],
            ["A", "request", "00:00:30"],
            ["C", "request", "00:00:50"],
            ["B", "request", "00:01:20"],
            ["B", "request", "00:01:50"],
            ["C", "request", "00:01:50"],
            ["A", "request", "00:05:40"],
            ["C", "request", "00:05:50"],
            ["A", "request", "00:06:40"],
        ]
        answer = {"A":5,"B":6,"C":6}
        result = solution(user_info, data_info)
        assert result == answer