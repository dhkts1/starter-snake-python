import json
import random

import bottle

from app.api import move_response


@bottle.post('/move')
def move():
    data = bottle.request.json

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    data = json.dumps(data)
    # print data
    json_data = json.loads(data)
    print json_data['board']['food']

    directions = ['up', 'down', 'left', 'right']
    direction = random.choice(directions)

    return move_response(direction)