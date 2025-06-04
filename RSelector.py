import json
import random

class RoleSelector:
    def __init__(self, config):  # Terima config sebagai parameter
        self.config = config
    
    def select_role(self, entropy_level):
        """Pilih role berdasarkan entropy level"""
        role_weights = self.config['role_weights'][entropy_level]
        roles = self.config['roles']
        
        selected_index = random.choices(
            range(len(roles)), 
            weights=role_weights, 
            k=1
        )[0]
        
        return roles[selected_index]
    
    def select_dimensions(self, entropy_level):
        """Pilih kombinasi dimensi kognitif"""
        dim_config = self.config['dimension_weights'][entropy_level]
        
        cognitive_style = random.choices(
            ['Analytical', 'Emotive'],
            weights=[dim_config['Analytical'], dim_config['Emotive']],
            k=1
        )[0]
        
        processing_style = random.choices(
            ['Structured', 'Exploratory'],
            weights=[dim_config['Structured'], dim_config['Exploratory']],
            k=1
        )[0]
        
        return cognitive_style, processing_style