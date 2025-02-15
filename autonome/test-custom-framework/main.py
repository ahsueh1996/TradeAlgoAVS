from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from typing import TypedDict, Optional

class ChatRequest(TypedDict):
    data: str

class ChatResponse(TypedDict):
    data: str

class AgentResponse(TypedDict):
    number_of_calls: int
    message: str

class ChatHandler(BaseHTTPRequestHandler):
    # Handler is a Singleton
    # Use properties instead of instance variables (ie constructor)
    number_of_calls = 0

    def _send_error(self, message: str, status_code: int = 400):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.cors_headers()
        self.end_headers()
        error_response = {'error': message + ":::: [Uncle Bob] custom error message end."}
        self.wfile.write(json.dumps(error_response).encode('utf-8'))

    def cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, PATCH, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'DNT,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization')


    def _validate_request(self, data: dict) -> Optional[ChatRequest]:
        if not isinstance(data, dict):
            return None
        if 'data' not in data:
            return None
        if not isinstance(data['data'], str):
            return None
        return ChatRequest(data=data['data'])

    def do_POST(self):
        self.number_of_calls += 1
        if self.path != '/chat':
            self._send_error(f'[Uncle Bob] POST "{self.path}" Not found', 404)
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
            # The heartbeat health check thing send {message: "healthz"}, so we need to handle that
            response: ChatResponse = {
                'data': f"[Uncle Bob] Unknown Schema. Received: {request_json}"
            }

        else:
            # Process the request (echo for this example)
            response: ChatResponse = {
                'data': f"[Uncle Bob] Received: {validated_request['data']}"
            }

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_GET(self):
        self.number_of_calls += 1
        if self.path == '/agents':
            # Process the request (let's tell the user about how many times we've been called)
            response: ChatResponse = {
                'number_of_calls': self.number_of_calls,
                'message': '[Uncle Bob] This is a GET request to /agents'
            }

            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self._send_error(f'[Uncle Bob] GET "{self.path}" Not found', 404)
            return
        # self._send_error('[Uncle Bob] Method not allowed', 405)

def run(server_class=HTTPServer, handler_class=ChatHandler, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    print(f'Chat endpoint available at http://localhost:{port}/chat')
    httpd.serve_forever()

if __name__ == '__main__':
    run()