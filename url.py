from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor
from twisted.web.resource import Resource
from calendar import calendar

class YearPage(Resource):
    def __init__(self, year):
        Resource.__init__(self)
        self.year = year
    def render_GET(self, request):
        return "<html><body><pre>%s</pre></body></html>" % (calendar(self.year),)

class Calendar(Resource):
    def getChild(self, name, request):
        try:
            year = int(name)
        except ValueError:
            return "http 404"
        else:
            return YearPage(year)

root = Calendar()


resource = File('~/Documents/workspace/twisted/html/index.html')
resource.putChild('', resource)


factory = Site(root)
reactor.listenTCP(8888, factory)



reactor.run()


