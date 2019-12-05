import unittest
from typing import List

from Service import Validator, Service


class StubValidator(Validator):
    def validate(self, values: List[str]) -> bool:
        return False


class TestServiceStub(unittest.TestCase):
    def test_with_stub(self):
        subject: Service = Service(StubValidator())

        subject.dowork()

        self.assertEquals(0, subject.work_count)
