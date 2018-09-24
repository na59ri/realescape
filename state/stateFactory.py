class stateFactory(object):

    @classmethod
    def input_noEvent(self):
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

    class InputNoEvent(event=''):
        print("stateFactory InputNoEvent start")

    class MessageEvent(event):
        print("stateFactory MessageEvent start")

    class FollowEvent(event):
        print("stateFactory FollowEvent start")

    class UnfollowEvent(event):
        print("stateFactory UnfollowEvent start")

    class BeaconEvent(event):
        print("stateFactory BeaconEvent start")
