from sanic import response
from sanic import Blueprint

blue=Blueprint('my_bu')

@blue.route('/blue')
def my_bu_req(request):
    return response.text('blue')