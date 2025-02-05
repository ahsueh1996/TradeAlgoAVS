from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from typing import TypedDict, Optional

class ChatRequest(TypedDict):
    data: str

class ChatResponse(TypedDict):
    data: str

class ChatHandler(BaseHTTPRequestHandler):
    def _send_error(self, message: str, status_code: int = 400):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET')
        self.send_header('Access-Control-Allow-Headers', 'Authorization, Content-Type')
        self.end_headers()
        error_response = {'error': message + ":::: [Uncle Bob] custom error message end."}
        self.wfile.write(json.dumps(error_response).encode('utf-8'))

    def _validate_request(self, data: dict) -> Optional[ChatRequest]:
        if not isinstance(data, dict):
            return None
        if 'data' not in data:
            return None
        if not isinstance(data['data'], str):
            return None
        return ChatRequest(data=data['data'])

    def do_POST(self):
        if self.path != '/chat':
            self._send_error('[Uncle Bob] Not found', 404)
            return

        # Read and parse request body
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            request_json = json.loads(post_data.decode('utf-8'))
        except (KeyError, json.JSONDecodeError):
            self._send_error('[Uncle Bob] Invalid JSON payload')
            return

        # Validate request schema
        validated_request = self._validate_request(request_json)
        if validated_request is None:
            self._send_error('[Uncle Bob] Invalid request schema')
            return

        # Process the request (echo for this example)
        response: ChatResponse = {
            'data': f"[Uncle Bob] Received: {validated_request['data']}"
        }

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET')
        self.send_header('Access-Control-Allow-Headers', 'Authorization, Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_GET(self):
        self._send_error('[Uncle Bob] Method not allowed', 405)

def run(server_class=HTTPServer, handler_class=ChatHandler, port=3000):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    print(f'Chat endpoint available at http://localhost:{port}/chat')
    httpd.serve_forever()

if __name__ == '__main__':
    run()