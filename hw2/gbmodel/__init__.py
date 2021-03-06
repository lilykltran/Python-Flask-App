"""Executed upon import from app.py to instantiate model returned by
    get_model().  Uses sqlite3 backend model."""
model_backend = 'sqlite3'

if model_backend == 'sqlite3':
    from .model_sqlite3 import model
else:
    raise ValueError("No appropriate databackend configured. ")

appmodel = model()

def get_model():
    return appmodel
