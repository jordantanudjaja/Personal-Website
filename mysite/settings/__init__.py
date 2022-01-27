from .base import *

if os.environ.get('STATUS') == "Development":
    from .development import *
elif os.environ.get('STATUS') == "Local Production":
    from .localproduction import *
else:
    from .production import *
