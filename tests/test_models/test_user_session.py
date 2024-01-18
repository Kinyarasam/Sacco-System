#!/usr/bin/env python3
""" Contains the TestUserSessionDocs classes
"""


import inspect
import pep8
import unittest
from models import user_session
from models.base_model import BaseModel

UserSession = user_session.UserSession


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of UserSession class
    """

    @classmethod
    def setUpClass(cls) -> None:
        """Set up for the doc tests
        """
        cls.user_f = inspect.getmembers(UserSession, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Test that models/user_session/user_session.py conforms to PEP8
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user_session/user_session.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """Test that tests/test_models/test_user_session.py conforms to PEP8
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user_session.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_session_module_docstring(self):
        """Test for the user_session.py module docstring
        """
        self.assertIsNot(user_session.__doc__, None,
                         "user_session.py needs a docstring")
        self.assertTrue(len(user_session.__doc__) >= 1,
                        "user_session.py needs a docstring")

    def test_user_session_class_docstring(self):
        """Test for the UserSession class docstring
        """
        self.assertIsNot(UserSession.__doc__, None,
                         "UserSession class needs a docstring")
        self.assertTrue(len(UserSession.__doc__) >= 1,
                        "UserSession class needs a docstring")

    def test_user_session_class_docstring(self):
        """Test for the UserSession class docstring
        """
        self.assertIsNot(UserSession.__doc__, None,
                         "UserSession class needs a docstring")
        self.assertTrue(len(UserSession.__doc__) >= 1,
                        "UserSession class needs a docstring")

    def test_user_session_func_docstring(self):
        """Test for the presence of docstrings in UserSession methods.
        """
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertIsNot(len(func[1].__doc__) >= 1,
                             "{:s} method needs a docstring".format(func[0]))
