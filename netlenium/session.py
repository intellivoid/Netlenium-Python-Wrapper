from netlenium.client import Client
from netlenium.proxy import Proxy
from netlenium.types import ProxyScheme, DriverType
from netlenium.window import Window


class Session(object):

    def __init__(self, data=None):
        """
        Public Constructor
        公共构造函数

        :param data:
        """

        if data is not None:
            self.id = data["ID"]
            self.created = data["Created"]
            self.last_activity = data["LastActivity"]
            self.driver = data["Driver"]
            self.headless = data["Headless"]

            scheme = None
            if data["ProxyConfiguration"]["Scheme"] == "http":
                scheme = ProxyScheme.http
            if data["ProxyConfiguration"]["Scheme"] == "https":
                scheme = ProxyScheme.https
            self.proxy_configuration = Proxy(
                host=data["ProxyConfiguration"]["Host"],
                port=data["ProxyConfiguration"]["Port"],
                scheme=scheme,
                authentication_required=data["ProxyConfiguration"]["AuthenticationRequired"],
                username=data["ProxyConfiguration"]["Username"],
                password=data["ProxyConfiguration"]["Password"]
            )
            self.proxy_configuration.enabled = data["ProxyConfiguration"]["Enabled"]

            self.current_window = Window()
            self.current_window.id = data["CurrentWindow"]["ID"]
            self.current_window.title = data["CurrentWindow"]["Title"]
            self.current_window.url = data["CurrentWindow"]["Url"]

    def create_client(self, admin_client, authentication=None):
        """
        Creates a client from this session
        从此会话创建客户端

        :type authentication: str
        :param authentication:
        :type admin_client: AdminClient
        :param admin_client:
        :return:
        """

        client = Client()

        if self.proxy_configuration.enabled:
            client.set_proxy_configuration(self.proxy_configuration)

        client.session_id = self.id
        client.endpoint = admin_client.endpoint

        if authentication is not None:
            client.api.authentication = authentication

        if self.driver == "chrome":
            client.target_driver = DriverType.chrome
        if self.driver == "opera":
            client.target_driver = DriverType.opera
        if self.driver == "firefox":
            client.target_driver = DriverType.firefox

        return client
