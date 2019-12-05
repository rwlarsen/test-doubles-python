import unittest
from typing import List

from Service import Validator, Service


class FakeValidator(Validator):
    def validate(self, values: List[str]) -> bool:
        return values.__len__() == 2


class TestServiceFake(unittest.TestCase):
    def test_with_fake(self):
        validator: FakeValidator = FakeValidator()
        subject: Service = Service(validator)

        subject.dowork()

        self.assertEquals(1, subject.work_count)


class TestFake(unittest.TestCase):
    subject: FakeValidator

    def setUp(self):
        self.subject = FakeValidator()

    def test_fake_1(self):
        args: List[str] = ["fizz"]
        self.assertFalse(self.subject.validate(args))

    def test_fake_2(self):
        args: List[str] = ["fizz", "bang"]
        self.assertTrue(self.subject.validate(args))

    def test_fake_3(self):
        args: List[str] = ["fizz", "bang", "buzz"]
        self.assertFalse(self.subject.validate(args))
