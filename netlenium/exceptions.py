class NetleniumException(Exception):
    def __init__(self, message, status_code, content=None):
        """
        Generic Netlenium Exception
        通用Netlenium异常

        :param message:
        :param status_code:
        :param content:
        """
        super(NetleniumException, self).__init__(message)
        self.status_code = status_code
        self.error_code = 1
        self.content = content


class AttributeNotFound(Exception):
    def __init__(self, message, status_code, content=None):
        """
        Exception thrown when the attribute value for the element was not found
        未找到元素的属性值时抛出异常

        :param message:
        :param status_code:
        :param content:
        """
        super(AttributeNotFound, self).__init__(message)
        self.status_code = status_code
        self.error_code = 101
        self.content = content


class InvalidProxyScheme(Exception):
    def __init__(self, message, status_code, content=None):
        """
        The given proxy scheme is invalid
        给定的代理方案无效

        :param message:
        :param status_code:
        :param content:
        """
        super(InvalidProxyScheme, self).__init__(message)
        self.status_code = status_code
        self.error_code = 102
        self.content = content


class UnsupportedDriver(Exception):
    def __init__(self, message, status_code, content=None):
        """
        Thrown when the given driver is unsupported on the remote server (New version maybe?)
        在远程服务器上不支持给定驱动程序时抛出（可能是新版本？）

        :param message:
        :param status_code:
        :param content:
        """
        super(UnsupportedDriver, self).__init__(message)
        self.status_code = status_code
        self.error_code = 103
        self.content = content


class UnsupportedRequestMethod(Exception):
    def __init__(self, message, status_code, content=None):
        """
        The request method used is not supported
        不支持使用的请求方法

        :param message:
        :param status_code:
        :param content:
        """
        super(UnsupportedRequestMethod, self).__init__(message)
        self.status_code = status_code
        self.error_code = 104
        self.content = content


class SessionExpired(Exception):
    def __init__(self, message, status_code, content=None):
        """
        The session has expired and is no longer available
        会话已过期，不再可用

        :param message:
        :param status_code:
        :param content:
        """
        super(SessionExpired, self).__init__(message)
        self.status_code = status_code
        self.error_code = 105
        self.content = content


class WindowHandlerNotFound(Exception):
    def __init__(self, message, status_code, content=None):
        """
        The given Window Handler was not found in the session
        在会话中找不到给定的窗口处理程序

        :param message:
        :param status_code:
        :param content:
        """
        super(WindowHandlerNotFound, self).__init__(message)
        self.status_code = status_code
        self.error_code = 106
        self.content = content


class SessionError(Exception):
    def __init__(self, message, status_code, content=None):
        """
        There was a unexpected error with the session
        会话出现意外错误

        :param message:
        :param status_code:
        :param content:
        """
        super(SessionError, self).__init__(message)
        self.status_code = status_code
        self.error_code = 107
        self.content = content


class SessionNotFound(Exception):
    def __init__(self, message, status_code, content=None):
        """
        The session was not found on the server
        在服务器上找不到该会话

        :param message:
        :param status_code:
        :param content:
        """
        super(SessionNotFound, self).__init__(message)
        self.status_code = status_code
        self.error_code = 108
        self.content = content


class Unauthorized(Exception):
    def __init__(self, message, status_code, content=None):
        """
        You don't have authorized access to make this request.
        您没有授权访问权来发出此请求。

        :param message:
        :param status_code:
        :param content:
        """
        super(Unauthorized, self).__init__(message)
        self.status_code = status_code
        self.error_code = 109
        self.content = content


class TooManySessions(Exception):
    def __init__(self, message, status_code, content=None):
        """
        The server cannot handle anymore sessions
        服务器无法再处理会话

        :param message:
        :param status_code:
        :param content:
        """
        super(TooManySessions, self).__init__(message)
        self.status_code = status_code
        self.error_code = 110
        self.content = content


class ResourceNotFound(Exception):
    def __init__(self, message, status_code, content=None):
        """
        The requested resource was not found
        找不到请求的资源

        :param message:
        :param status_code:
        :param content:
        """
        super(ResourceNotFound, self).__init__(message)
        self.status_code = status_code
        self.error_code = 111
        self.content = content


class JavascriptExecutionError(Exception):
    def __init__(self, message, status_code, content=None):
        """
        The given JavaScript code failed to be executed
        给定的JavaScript代码无法执行

        :param message:
        :param status_code:
        :param content:
        """
        super(JavascriptExecutionError, self).__init__(message)
        self.status_code = status_code
        self.error_code = 112
        self.content = content


class MissingParameter(Exception):
    def __init__(self, message, status_code, content=None):
        """
        The request is missing a required parameter
        请求缺少必需参数

        :param message:
        :param status_code:
        :param content:
        """
        super(MissingParameter, self).__init__(message)
        self.status_code = status_code
        self.error_code = 113
        self.content = content


class InvalidSearchValue(Exception):
    def __init__(self, message, status_code, content=None):
        """
        The given search value for finding elements is not supported/is invalid
        查找元素的给定搜索值不受支持/无效

        :param message:
        :param status_code:
        :param content:
        """
        super(InvalidSearchValue, self).__init__(message)
        self.status_code = status_code
        self.error_code = 114
        self.content = content


class DriverDisabled(Exception):
    def __init__(self, message, status_code, content=None):
        """
        The administrator has disabled support for this driver
        管理员已禁用对此驱动程序的支持

        :param message:
        :param status_code:
        :param content:
        """
        super(DriverDisabled, self).__init__(message)
        self.status_code = status_code
        self.error_code = 115
        self.content = content


class ElementNotFound(Exception):
    def __init__(self, message, status_code, content=None):
        """
        The element was not found
        找不到该元素

        :param message:
        :param status_code:
        :param content:
        """
        super(ElementNotFound, self).__init__(message)
        self.status_code = status_code
        self.error_code = 116
        self.content = content
