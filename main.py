
from sanic.response import json

import logging

from models import Users
from sanic import Sanic,response
from sanic.log import logger
from tortoise.contrib.sanic import register_tortoise

from blue_controller import blue

logging.basicConfig(level=logging.DEBUG)

app=Sanic(__name__)

app.blueprint(blue)

@app.route('/')
async def req_get(request):
    return json({
        "parsed":True,
        "url": request.url,
        "query_string":request.query_string,
        "args": request.args,
        "query_args":request.query_args,
        "endpoint":request.endpoint
    })

@app.route('file/')
async def post_file(request):
    return json({"received": True, "file_names": request.method, "params":request.host})

#@app.route("/users")
#async def list_all(request):
#    users=await Users.all()
#    logger.info('yes test.py log')                #first request info view
#    return response.json({'users': [str(user) for user in users]})
#
#@app.route("/user")
#async def add_user(request):
#    user=await Users.create(name="new")
#    return response.json({'user':str(user)})
#
#register_tortoise(
#    app, db_url="sqlite://:memory",modules={"models": ["models"]},generate_schemas=True
#)


if __name__=="__main__":
    app.run(port=5000, access_log=True)