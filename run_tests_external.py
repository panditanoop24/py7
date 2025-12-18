import os
import sys
import tempfile

# Avoid parsing local pyproject.toml by switching cwd to a safe temp dir
os.chdir(tempfile.gettempdir())

# Ensure project src is importable
sys.path.insert(0, r"C:\Client\py7\src")

import pytest

raise SystemExit(pytest.main([r"C:\Client\py7\tests\test_main2.py", "-q"]))
