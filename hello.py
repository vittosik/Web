def wsgi_application(environ, start_response):
    status = '200 OK'
    body = [bytes(i + '\n', 'utf-8') for i in environ['QUERY_STRING'].split('&')]
    headers = [
        ("Content-Type", "text/plain"), 
        ('Content-Length', str(len(body)))
        ]    
    start_response(status, headers)
    return body
