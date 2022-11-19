import json

class WarningStore:
    def __init__(self):
        # Load the warnings from the file
        self.load_warnings()

    # Function to create entry in warnings.json for a member
    def create_entry(self, member_id):
        # Check if there already is an entry for this member in warnings.json, and if not, create one
        if str(member_id) not in self.warnings:
            self.warnings[str(member_id)] = []

    # Function to add a warning to a member's warnings
    def add_warning(self, member_id, reason):
        # Add the warning to the list of warnings for this member
        self.warnings[str(member_id)].append(reason)

        # Save the warnings to the file
        self.save_warnings()
    
    # Function to save the warnings to the file
    def save_warnings(self):
        with open('database/warnings.json', 'w') as f:
            json.dump(self.warnings, f, indent=4)

    # Function to load the warnings from the file
    def load_warnings(self):
        with open('database/warnings.json', 'r') as f:
            self.warnings = json.load(f)
    
    # Function to get the warnings for a member
    def get_warnings(self, member_id):
        return self.warnings[str(member_id)]
    
    # Function to clear the warnings for a member
    def clear_warnings(self, member_id):
        self.warnings[str(member_id)] = []
        self.save_warnings()
    
    # Function to remove a warning from a member's warnings
    def remove_warning(self, member_id, warning):
        self.warnings[str(member_id)].remove(warning)
        self.save_warnings()
    
    # Function to remove a warning from a member's warnings by index
    def remove_warning_by_index(self, member_id, index):
        self.warnings[str(member_id)].pop(index)
        self.save_warnings()
    
    # Function to get the number of warnings for a member
    def get_warning_count(self, member_id):
        return len(self.warnings[str(member_id)])
    
    # Function to get the index of a warning for a member
    def get_warning_index(self, member_id, warning):
        return self.warnings[str(member_id)].index(warning)
    
    # Function to get the warning for a member by index
    def get_warning_by_index(self, member_id, index):
        return self.warnings[str(member_id)][index]
    
    # Function to check if a member has any warnings
    def has_warnings(self, member_id):
        return len(self.warnings[str(member_id)]) > 0
    
    # Function to check if a member has a specific warning
    def has_warning(self, member_id, warning):
        return warning in self.warnings[str(member_id)]