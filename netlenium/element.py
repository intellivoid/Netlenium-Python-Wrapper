class Element(object):

    def __init__(self, client, by, value, index, data=None):
        """
        Public Constructor
        公共构造函数

        :param client:
        :param by:
        :param value:
        :param index:
        :param data:
        """

        self.client = client
        self.by = by
        self.value = value
        self.index = index
        if data is not None:
            self.enabled = data["Enabled"]
            self.is_selected = data["IsSelected"]
            self.location = {
                "x": data["ElementLocation"]["X"],
                "y": data["ElementLocation"]["Y"]
            }
            self.size = {
                "width": data["ElementSize"]["Width"],
                "Height": data["ElementSize"]["Height"]
            }
            self.tag_name = data["TagName"],
            self.inner_text = data["InnerText"]

    def send_keys(self, keys_input):
        """
        Simulates typing into the element using the given input
        使用给定输入模拟键入元素

        :param keys_input:
        :return:
        """

        self.client.check_session()
        self.client.api.send_request("web_element/send_keys",
                                     {
                                         "session_id": self.client.session_id,
                                         "by": self.by,
                                         "value": self.value,
                                         "index": str(self.index),
                                         "input": str(keys_input)
                                     }
                                     )
        return True

    def click(self):
        """
        Simulates a click event on the element
        模拟元素上的单击事件

        :return bool:
        """

        self.client.check_session()
        self.client.api.send_request("web_element/click",
                                     {
                                         "session_id": self.client.session_id,
                                         "by": self.by,
                                         "value": self.value,
                                         "index": str(self.index)
                                     }
                                     )
        return True

    def clear(self):
        """
        Clears the element's inner content
        清除元素的内部内容

        :return:
        """

        self.client.check_session()
        self.client.api.send_request("web_element/clear",
                                     {
                                         "session_id": self.client.session_id,
                                         "by": self.by,
                                         "value": self.value,
                                         "index": self.index
                                     }
                                     )
        return True

    def move_to(self):
        """
        Moves into the element's view
        移动到元素的视图中

        :return:
        """
        self.client.check_session()
        self.client.api.send_request("web_element/move_to",
                                     {
                                         "session_id": self.client.session_id,
                                         "by": self.by,
                                         "value": self.value,
                                         "index": self.index
                                     }
                                     )
        return True

    def submit(self):
        """
        Submits the element to the remote web server
        将元素提交到远程Web服务器

        :return:
        """
        self.client.check_session()
        self.client.api.send_request("web_element/submit",
                                     {
                                         "session_id": self.client.session_id,
                                         "by": self.by,
                                         "value": self.value,
                                         "index": self.index
                                     }
                                     )
        return True

    def get_attribute(self, attribute_name):
        """
        Get's the element's value for an attribute
        获取属性的元素值

        :param attribute_name:
        :return:
        """
        self.client.check_session()
        response = self.client.api.send_request("web_element/get_attribute",
                                                {
                                                    "session_id": self.client.session_id,
                                                    "by": self.by,
                                                    "value": self.value,
                                                    "index": self.index,
                                                    "attribute_name": attribute_name
                                                }
                                                )
        return response["AttributeValue"]

    def set_attribute(self, attribute_name, attribute_value):
        """
        Sets a value to the given element's attribute, if the attribute does not exist it will be created
        将值设置为给定元素的属性，如果该属性不存在，则将创建该属性

        :param attribute_name:
        :param attribute_value:
        :return:
        """
        self.client.check_session()
        self.client.api.send_request("web_element/set_attribute",
                                     {
                                         "session_id": self.client.session_id,
                                         "by": self.by,
                                         "value": self.value,
                                         "index": self.index,
                                         "attribute_name": attribute_name,
                                         "attribute_value": attribute_value
                                     }
                                     )
        return True
