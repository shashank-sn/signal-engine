import http.server
import functools

directory = '/Users/shasha/Library/Mobile Documents/com~apple~CloudDocs/Signal Engine'
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=directory)
with http.server.HTTPServer(('', 3000), handler) as httpd:
    print(f'Serving at http://localhost:3000')
    httpd.serve_forever()
