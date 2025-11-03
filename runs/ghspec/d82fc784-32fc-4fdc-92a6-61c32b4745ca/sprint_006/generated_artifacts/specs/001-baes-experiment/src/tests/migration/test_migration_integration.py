```ini
# pytest.ini

[pytest]
# Set the coverage thresholds for the tests to ensure critical paths are adequately covered
minversion = 6.0
addopts = --cov=app --cov-report=html --cov-report=term --cov-fail-under=70
# Ensuring critical paths have higher coverage requirement
# Aim for 90% coverage on code paths related to assigning and updating course-teacher relations
# Remove unnecessary entries and retain only what is essential
```
