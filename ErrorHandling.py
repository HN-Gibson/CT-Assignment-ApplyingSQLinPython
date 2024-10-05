class MissingRequiredData(Exception):
    pass
    def handle_missing_required_data():
        print ("Error: Missing required data.")

class MemberExists(Exception):
    pass
    def handle_member_exists():
        print ("Error: Member exists with that name and age.")

class NoMemberFound(Exception):
    pass
    def handle_no_member_found():
        print ("Error: No member associated with that ID")

class NoSessionFound(Exception):
    pass
    def handle_no_session_found():
        print ("Error: No session exists with that id.")