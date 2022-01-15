model_backend = 'cloudsql'
#model_backend = 'sqlite3'
#model_backend = 'pylist'

if model_backend == 'sqlite3':
    from .model_sqlite3 import model
elif model_backend == 'pylist':
    from .model_pylist import model
elif model_backend == 'cloudsql':
    from .model_cloudsql import model    
else:
    raise ValueError("No appropriate databackend configured. ")

appmodel = model()

def get_model():
    return appmodel
