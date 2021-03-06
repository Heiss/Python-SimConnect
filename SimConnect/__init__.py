from .SimConnect import SimConnect, Request, millis, DWORD
from .Entities import Plane
from .Events import Event
from .Measurements import Measurement


def int_or_str(value):
    try:
        return int(value)
    except TypeError:
        return value


__version__ = "0.1"
VERSION = tuple(map(int_or_str, __version__.split(".")))

__all__ = ["SimConnect", "Request", "millis", "DWORD", "Plane", "Event", "Measurement"]
