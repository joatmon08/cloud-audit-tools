from invoke import Collection
from . import report

ns = Collection()
ns.add_collection(report, "report")
