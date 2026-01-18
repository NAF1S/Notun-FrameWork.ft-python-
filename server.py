from wsgiref.simple_server import make_server
from app import middleware








if __name__ == "__main__":
    host = "localhost"
    port = 1234
    # server = make_server(host, port, middleware)
    # print(f"Listening on http://{host}:{port}")
    # server.serve_forever()

    with make_server(host,port,middleware) as server:
        print(f"Listening on http://{host}:{port}")
        server.serve_forever()
