def log_move(func):
    def wrapper(*args, **kwargs):
        print("[LOG] Executing player's move")
        return func(*args, **kwargs)
    return wrapper
