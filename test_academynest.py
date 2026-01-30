# test_academynest.py
"""
Tests for AcademyNest module.
"""

import unittest
from academynest import AcademyNest

class TestAcademyNest(unittest.TestCase):
    """Test cases for AcademyNest class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AcademyNest()
        self.assertIsInstance(instance, AcademyNest)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AcademyNest()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
