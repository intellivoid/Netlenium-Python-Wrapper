from netlenium.api import API
from netlenium.element import Element
from netlenium.exceptions import ElementNotFound
from netlenium.exceptions import SessionError
from netlenium.types import DriverType
from netlenium.window import Window


class Client(object):

    def __init__(self, endpoint="http://localhost:6410", target_driver=DriverType.auto, authentication=None):
        """
        Public Constructor
        公共构造函数

        :param endpoint:
        :param target_driver:
        :param authentication:
        """
        self.endpoint = endpoint
        self.target_driver = target_driver
        self.proxy = None
        self.api = API(endpoint, authentication)
        self.session_id = None

    def set_proxy_configuration(self, proxy):
        """
        Sets a proxy configuration, this will be applied when starting a new session
        设置代理配置，这将在启动新会话时应用

        :param proxy:
        :return:
        """
        self.proxy = proxy

    def check_session(self):
        """
        Checks if the session is running, throws an exception if it's not
        检查会话是否正在运行，如果不是，则抛出异常

        :return:
        """
        if self.session_id is None:
            raise SessionError("The session is not running", 0)

    def start(self):
        """
        Starts the session and returns the Session ID
        启动会话并返回会话ID

        :return str:
        """
        parameters = {}

        if self.target_driver != DriverType.auto:
            parameters["target_driver"] = self.target_driver.name.lower()

        if self.proxy is not None:
            parameters["proxy_host"] = self.proxy.host
            parameters["proxy_port"] = self.proxy.port
            parameters["proxy_scheme"] = self.proxy.scheme.name.lower()
            if self.proxy.authentication_required:
                parameters["proxy_username"] = self.proxy.username
                parameters["proxy_password"] = self.proxy.password

        response = self.api.send_request("sessions/create", parameters)
        self.session_id = response["SessionId"]
        return self.session_id

    def stop(self):
        """
        Stops the current session and closes the driver
        停止当前会话并关闭驱动程序

        :return bool:
        """
        self.check_session()
        self.api.send_request("sessions/close",
                              {
                                  "session_id": self.session_id
                              }, True
                              )
        self.session_id = None
        return True

    def load_url(self, url):
        """
        Loads the URL, returns True when the navigation is completed
        加载URL，导航完成后返回True

        :param url:
        :return bool:
        """
        self.check_session()
        self.api.send_request("navigation/load_url",
                              {
                                  "session_id": self.session_id,
                                  "url": url
                              }, True
                              )
        return True

    def go_back(self):
        """
        Navigates one step backwards in the history, returns true when completed.
        在历史记录中向后导航一步，完成后返回true。

        :return bool:
        """
        self.check_session()
        self.api.send_request("navigation/go_back",
                              {
                                  "session_id": self.session_id
                              }, True
                              )
        return True

    def go_forward(self):
        """
        Navigates one stop forward in the history, returns true when completed.
        在历史记录中向后导航一步，完成后返回真。

        :return bool:
        """
        self.check_session()
        self.api.send_request("navigation/go_forward",
                              {
                                  "session_id": self.session_id
                              }, True
                              )
        return True

    def reload(self):
        """
        Reloads the current document
        重新加载当前文档

        :return bool:
        """
        self.check_session()
        self.api.send_request("navigation/reload",
                              {
                                  "session_id": self.session_id
                              }, True
                              )
        return True

    def get_elements(self, by, value):
        """
        Returns a list of element objects
        返回元素对象列表

        :param by:
        :param value:
        :return List[Element]:
        """
        self.check_session()
        response = self.api.send_request("actions/get_elements",
                                         {
                                             "session_id": self.session_id,
                                             "by": by.name.lower(),
                                             "value": value
                                         }, True
                                         )

        element_results = []
        for element_index, element in enumerate(response["Elements"]):
            element_results.append(Element(self, by.name.lower(), value, element_index, element))

        return element_results

    def get_element(self, by, value):
        """
        Returns the first occurrence of the element
        返回元素的第一个匹配项

        :param by:
        :param value:
        :return Element:
        """
        results = self.get_elements(by, value)
        if len(results) == 0:
            raise ElementNotFound("The element was not found", 0, None)
        return results[0]

    def execute_javascript(self, code):
        """
        Executes the given Javascript code in the current window of the session
        在会话的当前窗口中执行给定的Javascript代码

        :param code:
        :return:
        """
        self.check_session()
        response = self.api.send_request("actions/execute_javascript",
                                         {
                                             "session_id": self.session_id,
                                             "code": code
                                         }, True
                                         )
        return response["Output"]

    def current_window(self):
        """
        Returns the current window that the session is currently focused on
        返回会话当前关注的当前窗口

        :return Window:
        """
        self.check_session()
        response = self.api.send_request("window_handler/current_window",
                                         {
                                             "session_id": self.session_id
                                         }, True
                                         )
        return Window(response["CurrentWindow"])

    def list_windows(self):
        """
        Returns a list of Window handler id's that are currently opened
        返回当前打开的Window处理程序ID的列表

        :return:
        """
        self.check_session()
        response = self.api.send_request("window_handler/list_windows",
                                         {
                                             "session_id": self.session_id
                                         }, True
                                         )
        return response["WindowHandles"]

    def switch_window(self, window_id):
        """
        Switches to the Window Handle using the given ID
        使用给定的ID切换到窗口句柄

        :param window_id:
        :return:
        """
        self.check_session()
        self.api.send_request("window_handler/switch_to",
                              {
                                  "session_id": self.session_id,
                                  "id": window_id
                              }, True
                              )
        return True
