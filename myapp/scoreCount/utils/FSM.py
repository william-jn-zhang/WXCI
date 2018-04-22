# memory of a finite stat machine
# mem the present stat
from wxapi.FieldName import FieldName

class FSM:
    current_state = None
    state_handlers = {}

    def __init__(self):
        pass

    def regist_state_handler(self, sh):
        self.state_handlers[sh.name] = sh

    def get_message(self, session, msg_dict):
        #print("%s, %s" % (__file__, self.current_state))
        if self.current_state is None:
            print("Unstarted FSM, using FSM.set() to set FSM current state!")
            return None
        if not self.state_handlers.has_key(self.current_state):
            print("invalid state: %s", str(self.current_state))
            return None
        sh = self.state_handlers[self.current_state]
        (new_state, output) = sh.transition(session, msg_dict)
        self.current_state = new_state
        #print("%s, %s" % (__file__, self.current_state))
        #print("%s, %s" % (__file__, output))
        return output

    def set_state(self, state):
        self.current_state = state

    def get_state(self):
        return self.current_state
