from netlenium.types import ProxyScheme


class Proxy(object):

    def __init__(self, host, port,
                 scheme=ProxyScheme.https, authentication_required=False, username=None, password=None
                 ):
        """
        Proxy Configuration
        代理配置

        :param host:
        :param port:
        :param scheme:
        :param authentication_required:
        :param username:
        :param password:
        """
        self.host = host
        self.port = port
        self.scheme = scheme
        self.authentication_required = authentication_required
        self.username = username
        self.password = password
        self.enabled = True
