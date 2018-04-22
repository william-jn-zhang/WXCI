
class AppEntryBase:
    LABEL_EXIT = False
    # implement this method
    def do(self, session, request_dict):
        pass

    def _exit(self):
        self.LABEL_EXIT =True
        return
        
