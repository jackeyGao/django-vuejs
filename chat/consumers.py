import logging

log = logging.getLogger(__name__)

def ws_connect(message):
    log.debug('ws_connect path={path}'.format(**message.content))

def ws_receive(message):
    log.debug('ws_receive text={text}'.format(**message.content))
    message.reply_channel.send({'text': message['text']})
