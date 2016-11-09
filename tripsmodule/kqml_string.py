from io import BytesIO

class KQMLString(object):
    def __init__(self, data=None):
        if data is None:
            self.data = ''
        else:
            self.data = data

    def length(self):
        return len(self.data)

    def char_at(self, n):
        return self.data[n]

    def equals(self, obj):
        if not isinstance(obj, KQMLString):
            return False
        else:
            return obj.data == self.data

    def write(self, out):
        out.write('"'.encode())
        for ch in self.data:
            #if ch == '"' or ch == '\\':
            if ch == '"':
                out.write('\\'.encode())
            out.write(ch.encode())
        out.write('"'.encode())

    def to_string(self):
        out = BytesIO()
        self.write(out)
        res = out.getvalue()
        if type(res) is bytes:
            return res.decode()
        return res

    def string_value(self):
        return self.data

    def __str__(self):
        res = self.to_string()
        if type(res) is bytes:
            return res.decode()
        return res

    def __repr__(self):
        s = self.__str__()
        s = s.replace('\n', '\\n')
        return s
