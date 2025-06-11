class HierarchicalMemoryStore:
    def __init__(self):
        self.anomaly_memory = {}
        self.game_memory = {}
        self.symbolic_memory = {}
        self.token_distributions = {}
        
    def update_token_distribution(self, task_type, tokens):
        """Update token distribution for specific task type"""
        if task_type not in self.token_distributions:
            self.token_distributions[task_type] = {}
            
        for token in tokens:
            self.token_distributions[task_type][token] = \
                self.token_distributions[task_type].get(token, 0) + 1
        
        # Normalize
        total = sum(self.token_distributions[task_type].values())
        for token in self.token_distributions[task_type]:
            self.token_distributions[task_type][token] /= total

    def detect_anomaly(self, tokens):
        """Detect anomaly based on token distribution"""
        if not self.token_distributions.get('anomaly'):
            return False  # Belum ada baseline
            
        anomaly_score = 0
        for token in tokens:
            expected = self.token_distributions['anomaly'].get(token, 0)
            actual = tokens.count(token) / len(tokens)
            anomaly_score += abs(expected - actual)
            
        return anomaly_score > 0.3  # Threshold empiris

    def store_game_strategy(self, game_type, strategy, outcome):
        """Store game theory strategy"""
        if game_type not in self.game_memory:
            self.game_memory[game_type] = []
            
        self.game_memory[game_type].append({
            "strategy": strategy,
            "outcome": outcome,
            "token_distribution": self.calculate_token_distribution(strategy)
        })
        
    def get_optimal_strategy(self, game_type):
        """Retrieve best strategy based on historical outcomes"""
        if game_type not in self.game_memory or not self.game_memory[game_type]:
            return None
            
        # Cari strategi dengan outcome terbaik
        best_strategy = max(self.game_memory[game_type], 
                           key=lambda x: x['outcome'])
        return best_strategy['strategy']
    
    def symbolic_reasoning(self, symbolic_expression):
        """Manipulate symbolic expressions using token distribution"""
        tokens = self.tokenize_symbolic(symbolic_expression)
        normalized = []
        
        for token in tokens:
            # Manipulasi token berdasarkan distribusi historis
            if token in self.token_distributions.get('symbolic', {}):
                if self.token_distributions['symbolic'][token] > 0.1:
                    normalized.append(token)
            else:
                normalized.append(token)
                
        return " ".join(normalized)
    
    def tokenize_symbolic(self, expression):
        """Tokenize symbolic expressions"""
        # Implementasi khusus untuk symbolic tasks
        return re.findall(r'[a-zA-Z]+|\d+|\S', expression)
    
    def calculate_token_distribution(self, text):
        """Calculate token distribution for text"""
        tokens = re.findall(r'\w+', text.lower())
        total = len(tokens)
        dist = {}
        
        for token in tokens:
            dist[token] = dist.get(token, 0) + 1
        
        for token in dist:
            dist[token] /= total
            
        return dist