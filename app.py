from http.server import BaseHTTPRequestHandler, HTTPServer

class DummyServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        response = b'{"status": "success", "message": "Hello from the dummy Python server!"}'
        self.wfile.write(response)

if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, DummyServer)
    print("Running dummy web app on port 8080...")
    httpd.serve_forever()
