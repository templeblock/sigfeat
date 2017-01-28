"""Implements abstract Sink class and some usefull Sink subclasses

- :py:class:`DefaultDictSink`:  Sink receiving results in dictionary.

"""

import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Sink(object):
    """Sink base class."""

    @abc.abstractclassmethod
    def receive(self, datad):
        """Shall receive dictionaries directly written to source."""
        pass  # pragma: no coverage

    @abc.abstractclassmethod
    def receive_append(self, resultd):
        """Shall receive result dictionaries appending data to fields."""
        pass  # pragma: no coverage
