# Creating Integration Tests with Pytest

I mainly use `pytest` for unit tests. But I also want to use it for integration tests. The main difference for me is that I don't want to run integration tests every time. Today I leaaned that you can add `markers` to your tests and then run only the tests with that marker.

## Adding a Marker

Just mark one test with a marker like this:

```python
import pytest

@pytest.mark.integration
def test_integration_example():
    assert True
```

To mark all tests in a file, you can add the marker to the `pytest` decorator at the top of the file:

```python
import pytest

pytestmark = pytest.mark.integration

def test_integration_example_1():
    assert True

def test_integration_example_2():
    assert True
```

## Allow custom markers

The mark `integration` is not recognized by default. You need to add it to your `pytest.ini` file to allow custom markers. Create or edit the `pytest.ini` file in your project root directory and add the following:

```ini
[pytest]
markers =
    integration: mark test as an integration test
```

## Running Tests with a Marker

To run only the tests with a specific marker, you can use the `-m` option with `pytest`. For example, to run only the integration tests, you can use:

```bash
pytest -m integration
```

## Skip Integration Tests by Default

I want `pytest` to run only unit tests by default and skip integration tests. 

This is accomplished with:

```bash
pytest -m "not integration"
```

To make this easier, I modified `pytest.ini`

```ini
[pytest]
addopts = -m "not integration"
```



