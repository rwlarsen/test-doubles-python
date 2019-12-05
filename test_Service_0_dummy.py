import unittest
from typing import List

from Service import Validator, Service


class DummyValidator(Validator):
    def validate(self, values: List[str]) -> bool:
        assert False, "a dummy should never be called"


class TestServiceDummy(unittest.TestCase):
    def test_with_dummy(self):
        subject: Service = Service(DummyValidator())

        # subject.dowork()

        self.assertEquals(0, subject.work_count)
