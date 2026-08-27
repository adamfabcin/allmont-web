#!/usr/bin/env python3
"""ALL MONT, lokalny nahlad. Server, ktory zakazuje kesovanie, aby prehliadac
nikdy neukazal starsiu verziu stranky po zmene suborov."""
import http.server, socketserver, sys, os

class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header("Accept-Ranges", "bytes")
        super().end_headers()
    def send_header(self, key, value):
        if key.lower() == "last-modified":
            return
        super().send_header(key, value)
    def log_message(self, fmt, *args):
        pass

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8123
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("127.0.0.1", port), H) as httpd:
        print(f"  ALL MONT, nahlad webu")
        print(f"  ---------------------")
        print(f"  Adresa:  http://localhost:{port}")
        print(f"")
        print(f"  Toto okno nechajte otvorene. Zatvorenim sa nahlad vypne.")
        print(f"  Kesovanie je vypnute, takze vzdy vidite aktualnu verziu.")
        httpd.serve_forever()
