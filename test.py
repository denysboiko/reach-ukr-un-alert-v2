def somefunc(fields):
    if fields is not None:
        allowed = set(fields)
        existing = set(fields.keys())

        print allowed
        for field_name in existing - allowed:
            fields.pop(field_name)