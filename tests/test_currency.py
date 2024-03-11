"""
    Trying out pytest for HW5
    Author: Heather Marriott
"""

import pytest
from unittest import TestCase #used for Unit Tests
from streamlit.testing.v1 import AppTest #library from streamlit to help test UIs


class Test(TestCase):    
        def test_ui_title_and_header(self):
                """
                find out more about how to test streamlit apps:
                https://docs.streamlit.io/library/api-reference/app-testing
                AppTest simulates running Streamlit app for testing
                """
                
                at = AppTest.from_file("./main.py")
                at.run()

                print(f"Title of App is {at.title[0].value}")
                assert at.title[0].value.startswith("All the Data")
                assert 2==2


        def test_ui(self):
                print("oops: I did not really do TDD")
                assert 1==1
