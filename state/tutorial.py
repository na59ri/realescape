import stateFactory


class tutorialFactory(stateFactory):

    class InputNoEvent(event=null):
        print "stateFactory InputNoEvent start"

    class MessageEvent(event):
        print "stateFactory MessageEvent start"

    class FollowEvent(event):
        print "stateFactory FollowEvent start"

    class UnfollowEvent(event):
        print "stateFactory UnfollowEvent start"

    class BeaconEvent(event):
        print "stateFactory BeaconEvent start"
