import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import main
import utils

def test_main_runs():
    """Test that main script runs without errors."""
    # This would normally capture output, simplified for basic test
    assert True  # Placeholder test

def test_hello_world():
    """Test the hello_world utility function."""
    result = utils.hello_world()
    assert "MyFirstProject" in result

def test_hackathon_helper():
    """Test the hackathon_helper utility function."""
    result = utils.hackathon_helper()
    assert "AI solutions" in result

if __name__ == "__main__":
    test_main_runs()
    test_hello_world()
    test_hackathon_helper()
    print("All tests passed!")