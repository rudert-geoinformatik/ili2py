"""Run `python -m ili2py`.

Allow running ili2py, also by invoking
the python module:

`python -m ili2py`

This is an alternative to directly invoking the cli that uses python as the
"entrypoint".
"""
from __future__ import absolute_import

from ili2py.cli import main

if __name__ == "__main__":  # pragma: no cover
    main(prog_name="ili2py")
