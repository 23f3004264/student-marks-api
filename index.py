import json
from http.server import BaseHTTPRequestHandler
import urllib.parse as urlparse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = urlparse.parse_qs(urlparse.urlparse(self.path).query)
        names = query.get('name', [])

        # Sample marks database
        marks_data = {
            "John": 10,
            "Jane": 20,
            "Alice": 30,
            "Bob": 40
        }

        # Fetch marks for the given names
        marks = [marks_data.get(name, 0) for name in names]

        # Prepare JSON response
        response = {"marks": marks}

        # Send HTTP response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))
