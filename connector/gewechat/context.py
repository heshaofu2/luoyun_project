# encoding:utf-8

from enum import Enum


class ContextType(Enum):
    TEXT = 1  # 文本消息
    VOICE = 2  # 音频消息
    IMAGE = 3  # 图片消息
    FILE = 4  # 文件信息
    VIDEO = 5  # 视频信息
    STATUS_SYNC = 6  # 微信客户端的状态同步消息，可以忽略 eggs: 打开/退出某个聊天窗口
    NON_USER_MSG = 7  # 来自公众号、腾讯游戏、微信团队等非用户账号的消息
    UNKNOWN = 8  # 未知类型

    IMAGE_CREATE = 10  # 创建图片命令
    ACCEPT_FRIEND = 19 # 同意好友请求
    JOIN_GROUP = 20  # 加入群聊
    PATPAT = 21  # 拍了拍
    FUNCTION = 22  # 函数调用
    EXIT_GROUP = 23 #退出

    def __str__(self):
        return self.name


class Context(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = ContextType.UNKNOWN

    def __contains__(self, key):
        if key == "type":
            return self.type is not None
        elif key == "content":
            return self.content is not None
        else:
            return key in self.kwargs

    def __getitem__(self, key):
        if key == "type":
            return self.type
        elif key == "content":
            return self.content
        else:
            return self.kwargs[key]

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def __setitem__(self, key, value):
        if key == "type":
            self.type = value
        elif key == "content":
            self.content = value
        else:
            self.kwargs[key] = value

    def __delitem__(self, key):
        if key == "type":
            self.type = None
        elif key == "content":
            self.content = None
        else:
            del self.kwargs[key]

    def __str__(self):
        return "Context(type={}, content={}, kwargs={})".format(self.type, self.content, self.kwargs)
