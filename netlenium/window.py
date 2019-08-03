class Window(object):

    def __init__(self, data=None):
        """
        Public Constructor
        公共构造函数

        :param data:
        """
        if data is not None:
            self.id = data["ID"]
            self.url = data["Url"]
            self.title = data["Title"]
