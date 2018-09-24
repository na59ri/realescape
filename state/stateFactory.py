class stateFactory(object):

    @classmethod
    def input_noEvent(self, event=''):
        return self.InputNoEvent(event)

    @classmethod
    def input_messageEvent(self, event):
        return self.MessageEvent(event)

    @classmethod
    def input_followEvent(self, event):
        return self.FollowEvent(event)

    @classmethod
    def input_unfollow(self, event):
        return self.UnfollowEvent(event)

    @classmethod
    def input_beacon(self, event):
        return self.BeaconEvent(event)

    class InputNoEvent:
        def __init__(self, event):
            print("stateFactory InputNoEvent start")

    class MessageEvent:
        def __init__(self, event):
            print("stateFactory MessageEvent start")

    class FollowEvent:
        def __init__(self, event):
            print("stateFactory FollowEvent start")

    class UnfollowEvent:
        def __init__(self, event):
            print("stateFactory UnfollowEvent start")

    class BeaconEvent:
        def __init__(self, event):
            print("stateFactory BeaconEvent start")
