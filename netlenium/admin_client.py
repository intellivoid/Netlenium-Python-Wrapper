from netlenium.api import API
from netlenium.session import Session


class AdminClient(object):

    def __init__(self, endpoint="http://localhost:6410", authentication=None):
        """
        Public Constructor
        公共构造函数

        :param endpoint:
        :param authentication:
        """
        self.endpoint = endpoint
        self.api = API(endpoint, authentication)

    def get_sessions(self):
        response = self.api.send_request("admin/active_sessions", {}, True)

        session_results = []
        for session in response["Sessions"]:
            session_results.append(Session(session))

        return session_results
