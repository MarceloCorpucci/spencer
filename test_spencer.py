import os
from errbot.backends.test import testbot


class TestSpencer(object):
    extra_plugin_dir = '.'

    def test_listen(self, testbot):
        testbot.push_message('!feature')
        assert "Got it, don't forget the feature name." in testbot.pop_message()