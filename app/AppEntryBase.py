
class AppEntryBase:

    # implement this method
    def do(self, session, request_dict):
        pass

    def _exit(self):
        self.LABEL_EXIT =True
        return
        
