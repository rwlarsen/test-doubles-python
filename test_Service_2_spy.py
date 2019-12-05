import unittest
from typing import List

from Service import Validator, Service


class SpyValidator(Validator):
    called: bool = False

    def validate(self, values: List[str]) -> bool:
        self.called = True
        return False


class TestServiceSpy(unittest.TestCase):
    def test_with_spy(self):
        validator: SpyValidator = SpyValidator()
        subject: Service = Service(validator)

        subject.dowork()

        self.assertTrue(validator.called)
        self.assertEquals(0, subject.work_count)
