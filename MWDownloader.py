#-------------------------------------------------------------------------------
# Name:        Sample Downloader Class - MWDownloader
# Purpose:     The script is a Class that can be used to download malware samples
#              from remote sources. The Class has the possibility to:
#              1. modify the User-Agent
#              2. modify the Referer
#              This script has been used to:
#              - Automatically download polymorphic generated files from servers
#              - Download ExploitKits landing pages bypassing User-Agent and Referer checks
#
# Author:      Ptr32Void - @Ptr32Void
#-------------------------------------------------------------------------------
import os
import sys
import urllib2
import socket
import hashlib

class MWDownloader:
    user_agent = 'Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1'
    refer = 'https://www.google.com'
    request_timeout = 10

    sample_path = "C:\\samples"

    def get_md5_sample(self, data):
        hash = hashlib.md5()
        hash.update(data)
        return hash.hexdigest()

    def download_sample(self, url):
        headers = { 'User-Agent' : self.user_agent }
        try:
            socket.setdefaulttimeout(self.request_timeout)
            req = urllib2.Request(url, None, headers)
            req.add_header('Referer', self.refer)
            response = urllib2.urlopen(req)
            response = response.read()
        except Exception as e:
            print "[-] Exception %s in download_sample()\n" % (str(e))
            return -1

        md5_sample = self.get_md5_sample(response)
        fh = open(os.path.join(self.sample_path, md5_sample), 'wb')
        fh.write(response)
        fh.close()

def main():
    md = MWDownloader()
    md.download_sample('http://whateverurlhere.com/samplehere')

if __name__ == '__main__':
    main()