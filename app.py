from chalice import Chalice

from chalicelib.slack import Slack
from chalicelib.command_dispatcher import main

app = Chalice(app_name='megaphone')
app.debug = True


@app.route('/', methods=['POST'])
def index():
    request = app.current_request
    print(request.__dict__)
    payload = {
        "response_type": "in_channel",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "text": "*Link Database.*",
                    "type": "mrkdwn"
                },
            },
            *[{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": s,
                }
            } for s in ['text', 'fewa']]
        ]
    }
    return Slack.server_response(200, body=payload)

#
# @app.lambda_function()
# def anon(event, context):
#     request = app.current_request
#     print(request.raw_body)
#     print(event)
