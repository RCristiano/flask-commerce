from flask import jsonify
from flask_login import login_required
from app.main import main

@main.route('/')
@login_required
def index():
    """Deafult
    Default page.
    ---
    security:
        - cookieAuth: []
    tags:
        - Main
    produces:
        - application/json
    definitions:
        ApiResponse:
            type: object
            required:
            - msg
            description: Message response
            properties:
                msg:
                    type: string
    responses:
        200:
            description: Welcome message.
            schema:
                allOf:
                - $ref: '#/definitions/ApiResponse'
                example:
                    msg: Welcome
        401:
            $ref: '#/definitions/Unauthorized'
        default:
            description: Unexpected error.
    """
    return jsonify(msg='Welcome')
