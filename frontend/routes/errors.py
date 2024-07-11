from .. import app

# A decorator that is used to register a function given an error code. Example:
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

# You can also register handlers for arbitrary exceptions:

@app.errorhandler(ValueError)
def value_error_exception_handler(error:ValueError):
    return f'Value error {str(error)}'

@app.errorhandler(KeyError)
def key_error_exception_handler(error:KeyError):
    return f'Key error {str(error)}'