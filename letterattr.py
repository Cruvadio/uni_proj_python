class LetterAttr:
    def __getattr__(self, attr):
        return attr

    def __setattr__(self, key, value):
        self.__dict__[key] = "".join([c for c in value if c in key])


