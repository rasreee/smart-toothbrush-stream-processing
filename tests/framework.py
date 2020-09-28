"""
Placeholder unit test.

This is just an example. Add more .py module files to this directory, and
write your unit tests there.

"""
from unittest import TestCase

from toothbrush.framework.queue import JobQueue



class TestFramework(TestCase):
    """
    Tests over the framework.

    """


    def test_job_queue(self):
        """
        Test polling the queue for a job.

        """
        with self.assertRaises(NotImplementedError):
            JobQueue.poll()
