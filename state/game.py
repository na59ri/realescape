import stateFactory


class gameFactory(stateFactory):

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
