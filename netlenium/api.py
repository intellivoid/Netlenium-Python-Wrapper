import json

import requests

from netlenium.exceptions import *


class API(object):

    def __init__(self, endpoint="http://localhost:6410", authentication=None):
        """
        Public Constructor
        公共构造函数

        :param endpoint:
        :param authentication:
        """

        self.endpoint = endpoint
        self.authentication = authentication

    @staticmethod
    def parse_error(response):
        """
        Determines the error and throws the appropriate exception
        确定错误并引发相应的异常

        :param response:
        :return:
        """

        payload = json.loads(response.text)
        error_code = payload["ErrorCode"]
        if error_code == 1:
            raise NetleniumException(response.text, response.status_code, response.text)
        if error_code == 100:
            raise NetleniumException(payload["Error"], response.status_code, response.text)
        if error_code == 101:
            raise AttributeNotFound(payload["Message"], response.status_code, response.text)
        if error_code == 102:
            raise InvalidProxyScheme(payload["Message"], response.status_code, response.text)
        if error_code == 103:
            raise UnsupportedDriver(payload["Message"], response.status_code, response.text)
        if error_code == 104:
            raise UnsupportedRequestMethod(payload["Message"], response.status_code, response.text)
        if error_code == 105:
            raise SessionExpired(payload["Message"], response.status_code, response.text)
        if error_code == 106:
            raise WindowHandlerNotFound(payload["Message"], response.status_code, response.text)
        if error_code == 107:
            raise SessionError(payload["Message"], response.status_code, response.text)
        if error_code == 108:
            raise SessionNotFound(payload["Message"], response.status_code, response.text)
        if error_code == 109:
            raise Unauthorized(payload["Message"], response.status_code, response.text)
        if error_code == 110:
            raise TooManySessions(payload["Message"], response.status_code, response.text)
        if error_code == 111:
            raise ResourceNotFound(payload["Message"], response.status_code, response.text)
        if error_code == 112:
            raise JavascriptExecutionError(payload["Message"], response.status_code, response.text)
        if error_code == 113:
            raise MissingParameter(payload["Message"], response.status_code, response.text)
        if error_code == 114:
            raise InvalidSearchValue(payload["Message"], response.status_code, response.text)
        if error_code == 115:
            raise DriverDisabled(payload["Message"], response.status_code, response.text)
        if error_code == 116:
            raise ElementNotFound(payload["Message"], response.status_code, response.text)
        raise Exception(response.text)

    def send_request(self, command, parameters, require_auth=False):
        """
        Sends a request to the remote server
        向远程服务器发送请求

        :param command:
        :param parameters:
        :param require_auth:
        :return Response:
        """
        if require_auth:
            if self.authentication is not None:
                parameters["auth"] = self.authentication
        if command is None:
            response = requests.post(
                "{0}/".format(self.endpoint), parameters
            )
        else:
            response = requests.post(
                "{0}/{1}".format(self.endpoint, command), parameters
            )

        if response.status_code != 200:
            self.parse_error(response)
        return json.loads(response.text)
