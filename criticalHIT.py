#!/usr/bin/env python
import requests
import json
import random
from supersecretparameters import slack_token, slack_icon_url, slack_user_name, slack_channel


# Available dice: D20, D12, D10, D8, D6, D4
# Exercises are tuples with (dice (int), exercise (string))
exercises = [(10, 'pushups'),
             (6, "x10 second planking"),
             (20, "body weight squats"),
             (20, "tricep dips"),
             (20, "jumping jacks"),
             (20, "walking lunges"),
             (4, "x10 seconds mountain climbers"),
             (8, "burpees with push up"),
            ]


def post_message_to_slack(text, blocks = None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': text,
        'icon_url': slack_icon_url,
        'username': slack_user_name,
        'blocks': json.dumps(blocks) if blocks else None
    }).json()


if __name__ == "__main__":
    slack_info = "Who is ready to do some training? Give me:"
    for dice, exercise in random.sample(exercises, 3):
        num_times = random.randint(1, dice)
        if num_times == dice:
            slack_info += "\n :d{}: CRITICAL HIT! {} {}!!!".format(dice, num_times, exercise)
        else:
            slack_info += "\n :d{}: {} {}".format(dice, num_times, exercise)
    slack_info += "\nLike this message once you did all exercises!"

    post_message_to_slack(slack_info)
