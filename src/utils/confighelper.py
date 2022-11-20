import json

class ConfigHelper:
    # path to the config file
    config_path = 'database/config.json'

    def create_modlog_entry(self):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)

        # Check if there's an entry for the modlog channel's id in config.json, and if not, create one
        if 'modlog_channel_id' not in config:
            config['modlog_channel_id'] = None

        # Save the config file
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=4)
    
    def get_modlog_channel_id(self):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        
        # Return the modlog channel id
        return config['modlog_channel_id']
    
    def set_modlog_channel_id(self, channel_id):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        
        # Set the modlog channel id
        config['modlog_channel_id'] = channel_id

        # Save the config file
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=4)
    
    def clear_modlog_channel_id(self):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        
        # Clear the modlog channel id
        config['modlog_channel_id'] = None

        # Save the config file
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=4)