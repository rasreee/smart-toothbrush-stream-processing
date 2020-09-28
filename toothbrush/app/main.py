"""
Main job processing handler.

"""
import logging

from toothbrush.framework.job import JobQueue
from toothbrush.framework.llamadb import LlamaDB


log = logging.getLogger()

def process_next_job():
    """
    Uses JobQueue to get the next job, connects to LlamaDB, and ingests the
    job dataset.

    This functions SHOULD NOT raise any exceptions. It must always return
    (no return value). Use the `Job` object you pull from the queue to report
    the result (success or failure).

    This function is called continuously in a loop by "the framework".

    """
    raise NotImplementedError()
