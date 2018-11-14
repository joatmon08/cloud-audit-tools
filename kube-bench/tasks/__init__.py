from invoke import Collection
from . import logs

ns = Collection()
ns.add_collection(logs, "logs")
