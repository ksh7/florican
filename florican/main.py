from huey import SqliteHuey, crontab

import os

from .config import SCHEDULER_DIR
from .gatekeeper import GateKeeper

huey = SqliteHuey(filename=os.path.join(SCHEDULER_DIR, "huey.db"))


@huey.periodic_task(crontab(minute='*/5'))
def tick_tick():
    """Is triggered once every 5 minutes and performs the checks."""
    gatekeeper = GateKeeper()
    gatekeeper.tick()


@huey.periodic_task(crontab(day='*'))
def am_i_alive():
    """Is triggered once every day and lets the user know it's still alive."""
    gatekeeper = GateKeeper()
    gatekeeper.heartbeat()
