

def packet(*args, **kwargs):
    def transformer(cls):
        cls.id = kwargs.get('id', None)
        return cls
        
    return transformer