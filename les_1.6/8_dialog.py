TYPE_OS = 1


class DialogWindows:
    name_class = 'DialogWindows'


class DialogLinux:
    name_class = 'DialogLinux'


class Dialgo:
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            obj = DialogWindows()
            setattr(obj, 'name', *args)
            return obj
        else:
            obj = DialogLinux()
            setattr(obj, 'name', *args)
            return obj