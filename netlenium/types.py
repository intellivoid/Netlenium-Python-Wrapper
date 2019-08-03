from enum import Enum


class DriverType(Enum):
    """
    Supported Driver Type
    支持的驱动程序
    """
    auto = 1
    chrome = 2
    firefox = 3
    opera = 4


class ProxyScheme(Enum):
    """
    Supported Proxy Scheme
    支持的代理方案
    """
    http = 1
    https = 2


class By(Enum):
    """
    Search elements by value
    按值搜索元素
    """
    class_name = 1
    css_selector = 2
    id = 3
    name = 4
    tag_name = 5
    xpath = 6
