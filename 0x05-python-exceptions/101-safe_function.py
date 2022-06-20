#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    result = 0
    try:
        result += fct(*args)
        return result
    except Exception as err:
        print("Exception: " + str(err), file=sys.stderr)
        return None
