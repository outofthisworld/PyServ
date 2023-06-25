def EventHandler(*args, **kwargs):
    event_key = kwargs.get('event')
    
    if event_key is None:
        raise ValueError("Missing event key")
    
    def handler(func):
        nonlocal event_key
        func._is_event_handler = True
        func._event_key = event_key
        return func

    return handler