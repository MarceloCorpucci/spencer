from errbot import BotPlugin, botcmd


class Spencer(BotPlugin):
    """Spencer basic plugin for Errbot"""

    @botcmd
    def feature(self, msg, args):
        """Minimal implementation"""
        return "Got it, don't forget the feature name."