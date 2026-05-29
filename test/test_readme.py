import os
import unittest

class TestREADME(unittest.TestCase):
    """Test cases for README.md"""
    
    def test_readme_exists(self):
        """Test that README.md exists"""
        self.assertTrue(os.path.exists('README.md'), "README.md should exist")
    
    def test_readme_not_empty(self):
        """Test that README.md is not empty"""
        self.assertGreater(os.path.getsize('README.md'), 0, "README.md should not be empty")
    
    def test_readme_contains_title(self):
        """Test that README.md contains the expected title"""
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn('Best-websites-a-programmer-should-visit', content, 
                         "README.md should contain the project title")

if __name__ == '__main__':
    unittest.main()