from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from typing import TypedDict, Optional

from chatbot import run_chat_mode, initialize_agent

import threading

class ChatRequest(TypedDict):
    data: str

class ChatResponse(TypedDict):
    data: str

class AgentResponse(TypedDict):
    number_of_calls: int
    message: str

class ChatHandler(BaseHTTPRequestHandler):
    # Handler is made PER request so there's no states.
    # Use self.server.variable to store states.

    def _send_error(self, message: str, status_code: int = 400):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.cors_headers()
        self.end_headers()
        error_response = {'error': message + ":::: [AgentKit+] custom error message end."}
        self.wfile.write(json.dumps(error_response).encode('utf-8'))

    def cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, PATCH, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'DNT,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization')


    def _validate_chat_schema(self, json_data: dict) -> Optional[ChatRequest]:
        if not isinstance(data, dict):
            return None
        # expect either of:
        # {'data': str} OR
        # {'message': str}
        msg = None
        if 'data' in json_data:
            msg = json_data['data']
        elif 'message' in json_data:
            msg = json_data['message']
        else:
            return None
        return ChatRequest(data=msg)

    def do_POST(self):
        self.server.reqID += 1
        if self.path != '/chat':
            self._send_error(f'[AgentKit+][{self.server.reqID}] POST "{self.path}" Not found', 404)
            return

        # Read and parse request body
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            request_json = json.loads(post_data.decode('utf-8'))
        except (KeyError, json.JSONDecodeError):
            self._send_error('[AgentKit+][{self.server.reqID}] Invalid JSON payload')
            return

        # Validate request schema
        validated_request = self._validate_chat_schema(request_json)
        if validated_request is None:
            # We'll still allow bad json data from the request.
            # Originally this was to fix the heartbeat issue, which could hang up the deployment for hours.
            response: ChatResponse = {
                'data': f"[AgentKit+][{self.server.reqID}] Unknown Schema. Received: {request_json}"
            }
        else:
            # Process the request
            # We'll pass the data to the agentkit chat.


            response: ChatResponse = {
                'data': f"[AgentKit+][{self.server.reqID}] Received: {validated_request['data']}"
            }

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_GET(self):
        self.server.reqID += 1
        if self.path == '/agents':
            # Process the request (let's tell the user about how many times we've been called)
            response: ChatResponse = {
                'reqID': self.server.reqID,
                'message': '[AgentKit+][{self.server.reqID}] This is a request using the GET Method to the /agents path'
            }

            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self._send_error(f'[AgentKit+] GET "{self.path}" Not found', 404)
            return
        # self._send_error('[AgentKit+] Method not allowed', 405)

class AgentKitServer(HTTPServer):
    def __init__(self, address, handler):
        self.reqID = 0
        super().__init__(address, handler)

def run(server_class=AgentKitServer, handler_class=ChatHandler, port=3000):

    print(f'Starting chat agent thread...')
    agent_executor, agent_config = initialize_agent()
    chat_agent_thread = threading.Thread(target=run_chat_mode, daemon=True)
    chat_agent_thread.start()

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    print(f'Chat endpoint available at http://localhost:{port}/chat')
    httpd.serve_forever()

if __name__ == '__main__':
    run()