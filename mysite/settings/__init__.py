from .base import *

if os.environ.get('STATUS') == "Development":
    from .development import *
else:
    from .production import *
