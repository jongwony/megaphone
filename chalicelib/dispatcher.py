import json

import jmespath

from .slack import Slack


class TypeDiverge:
    @classmethod
    def url_verification(cls, chalice_req):
        return {'challenge': chalice_req.json_body.get('challenge')}

    @classmethod
    def event_callback(cls, chalice_req):
        return dispatcher(MessageTypeDiverge, chalice_req, 'event.type')


class MessageTypeDiverge:
    @classmethod
    def message(cls, chalice_req):
        body = chalice_req.json_body
        blocks_payload = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": jmespath.search('event.text', body),
                }
            }
        ]
        bot = Slack(channel='#random', username='Megaphone')
        bot.post_message(blocks=json.dumps(blocks_payload), icon_emoji=':mega:')


def dispatcher(cls, chalice_req, query):
    body = chalice_req.json_body
    query_diverge = getattr(cls, jmespath.search(query, body) or '', None)
    if callable(query_diverge):
        return query_diverge(chalice_req)


def main(chalice_req):
    # Slack Error
    if reason := chalice_req.headers.get('X-Slack-Retry-Reason'):
        print(reason)
        return Slack.server_response(500, headers={'X-Slack-No-Retry': 1})

    result = dispatcher(TypeDiverge, chalice_req, 'type')
    return Slack.server_response(200, body=result)
