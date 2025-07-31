# PyTest options in pyproject.toml

You can configure pytest directly from pyproject.toml, so not needing a separate pytest.ini.
```toml
[tool.pytest.ini_options]
filterwarnings = [
    "ignore::DeprecationWarning",
    "ignore::PendingDeprecationWarning",
    "ignore::ImportWarning",
]
```
