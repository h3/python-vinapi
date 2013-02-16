from xml.dom.minidom import parse
import urllib2


class VinApi(object):
    vin = None
    headers = {'Content-Type': 'application/xml'}

    def __init__(self, api_key, cache=False,\
            base_url='http://vinapi.skizmo.com/vins/%s.xml'):
        self.cache = cache
        self.api_key = api_key
        self.url = base_url

    def get_headers(self):
        self.headers['X-VinApiKey'] = self.api_key
        return self.headers

    def get_url(self):
        if self.complete:
            return self.url % self.vin + '?complete=true'
        else:
            return self.url % self.vin

    def fetch(self):
        req = urllib2.Request(self.get_url(), None, self.get_headers())
        return urllib2.urlopen(req)

    def xml_to_dict(self):
        node = self.dom.documentElement
        root = self.dom.getElementsByTagName('hash')[0]
        out = {}
        for n in root.childNodes:
            if n.nodeType != node.TEXT_NODE:
                try:
                    v = n.childNodes[0].nodeValue
                    out[n.nodeName] = v == u'\u2014' and True or v
                except IndexError:
                    out[n.nodeName] = ''
        return out

    def find(self, vin, complete=True):
        self.vin = vin
        self.complete = complete
        self.dom = parse(self.fetch())
        return self.xml_to_dict()

    def status(self):
        return self.find('account_information')
