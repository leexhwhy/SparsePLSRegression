import numpy
import PLS.simpls
from scipy import sparse
import unittest


class CompletionTests(unittest.TestCase):
    """Tests checking whether the SIMPLS code successfully returns."""

    @classmethod
    def setUpClass(cls):
        """Setup inputs needed for tests in the class."""

        pass


class CorrectnessTests(unittest.TestCase):
    """Tests checking the correctness of the output."""

    pass

    # These will primarily involve performing SIMPLS through my code and checking against Matlab results


if __name__ == '__main__':
    unittest.main()