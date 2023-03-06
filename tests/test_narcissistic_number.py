from unittest import TestCase

from assertpy import assert_that


class Test(TestCase):
    def test_foo(
        self,
    ):
        assert_that(False).is_false()
