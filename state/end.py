import stateFactory


class endFactory(stateFactory):

    class InputNoEvent(event):
        print("stateFactory InputNoEvent start")

    class MessageEvent(event):
        print("stateFactory MessageEvent start")

    class FollowEvent(event):
        print("stateFactory FollowEvent start")

    class UnfollowEvent(event):
        print("stateFactory UnfollowEvent start")

    class BeaconEvent(event):
        print("stateFactory BeaconEvent start")
