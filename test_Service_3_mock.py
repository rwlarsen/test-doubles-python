import unittest
from typing import List

from Service import Validator, Service


class MockValidator(Validator):
    values: List[str]

    def validate(self, values: List[str]) -> bool:
        self.values = values
        return False


class TestServiceMock(unittest.TestCase):
    def test_with_mock(self):
        validator: MockValidator = MockValidator()
        subject: Service = Service(validator)

        subject.dowork()

        expected: List[str] = ["foo", "bar"]
        self.assertEquals(expected, validator.values)
        self.assertEquals(0, subject.work_count)
