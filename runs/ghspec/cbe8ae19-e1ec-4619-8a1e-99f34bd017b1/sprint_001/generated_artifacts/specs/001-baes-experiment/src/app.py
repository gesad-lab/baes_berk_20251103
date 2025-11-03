import os
import sys
import pytest

if __name__ == "__main__":
    # Set the environment variable for the Flask app
    os.environ["FLASK_APP"] = "app.py"

    # Run tests located in tests/all_tests.py using pytest
    # Exit with the appropriate exit code based on test results
    exit_code = pytest.main(["tests/all_tests.py"])
    sys.exit(exit_code)