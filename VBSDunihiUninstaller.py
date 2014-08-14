#-------------------------------------------------------------------------------
# Name:        Dunihi Remote Malware Uninstaller
# Purpose:     This script is a remote VBS.Dunihi Malware Uninstaller.
#              It is a small web server that will replace the Dunihi C&C server
#              in order to uninstall the malware from the infected systems.
#
# Author:      Ptr32Void
#
# Date:        14/08/2014
#-------------------------------------------------------------------------------

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import string
import sys

http_port= 80

class httpdHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write("GET handler...")
        return

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        ua = str(self.headers['user-agent'])
        dunihi_data = ua.split('<|>')
        print '[!] Dunihi requested operation %s' % (self.path)
        print '[!] Infected PC name: %s' % (dunihi_data[1])
        print '[!] Infected PC UserName: %s' % (dunihi_data[2])
        print '[!] Infected PC OS: %s' % (dunihi_data[3])
        if ( self.path.find('is-ready') != -1):
            print '[!] Dunihi malware ready, sending uninstall command...'
            self.wfile.write("uninstall")
            print '[+] Uninstall command sent!'

        return

def main():
    try:
        server = HTTPServer(('', http_port), httpdHandler)
        print '[+] Dunihi HTTPd server started'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'CTRL+C, shutting down the server'
        server.socket.close()

if __name__ == '__main__':
    main()