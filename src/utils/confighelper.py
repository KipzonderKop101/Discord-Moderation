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
    
    def create_mute_role_entry(self):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)

        # Check if there's an entry for the mute role's id in config.json, and if not, create one
        if 'mute_role_id' not in config:
            config['mute_role_id'] = None

        # Save the config file
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=4)

    def get_mute_role_id(self):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        
        # Return the mute role id
        return config['mute_role_id']
    
    def set_mute_role_id(self, role_id):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        
        # Set the mute role id
        config['mute_role_id'] = role_id

        # Save the config file
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=4)
        
    def clear_mute_role_id(self):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        
        # Clear the mute role id
        config['mute_role_id'] = None

        # Save the config file
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=4)
    
    def create_mod_role_entry(self):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)

        # Check if there's an entry for the mod role's id in config.json, and if not, create one
        if 'mod_role_id' not in config:
            config['mod_role_id'] = None

        # Save the config file
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=4)
    
    def get_mod_role_id(self):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        
        # Return the mod role id
        return config['mod_role_id']
    
    def set_mod_role_id(self, role_id):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        
        # Set the mod role id
        config['mod_role_id'] = role_id

        # Save the config file
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=4)
    
    def clear_mod_role_id(self):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        
        # Clear the mod role id
        config['mod_role_id'] = None

        # Save the config file
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=4)
    
    def create_admin_role_entry(self):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)

        # Check if there's an entry for the admin role's id in config.json, and if not, create one
        if 'admin_role_id' not in config:
            config['admin_role_id'] = None

        # Save the config file
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=4)
    
    def get_admin_role_id(self):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        
        # Return the admin role id
        return config['admin_role_id']
    
    def set_admin_role_id(self, role_id):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        
        # Set the admin role id
        config['admin_role_id'] = role_id

        # Save the config file
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=4) 
    
    def clear_admin_role_id(self):
        # Open the config file
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        
        # Clear the admin role id
        config['admin_role_id'] = None

        # Save the config file
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=4)