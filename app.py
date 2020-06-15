from chalice import Chalice

from chalicelib.dispatcher import main

app = Chalice(app_name='megaphone')
app.debug = True


@app.route('/', methods=['POST'])
def index():
    request = app.current_request
    print(request.raw_body)
    return main(request)
