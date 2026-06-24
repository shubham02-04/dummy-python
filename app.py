from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class DummyServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(
            b'{"status":"success","message":"Hello from Azure Web App"}'
        )

port = int(os.environ.get("PORT", 8080))

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    server_address = ("", port)

    httpd = HTTPServer(server_address, DummyServer)
    print(f"Running on port {port}")
    httpd.serve_forever()
