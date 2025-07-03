"""
Fraudulent Transaction Detection System
======================================

This system generates synthetic financial transaction data and detects
anomalous patterns that could indicate fraudulent activity.

Author: [Your Name]
Date: July 2025
"""

import pandas as pd
import numpy as np
import random
import warnings
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import matplotlib.pyplot as plt
import seaborn as sns



@dataclass
class TransactionConfig:
    """Configuration for transaction generation"""
    num_customers: int = 10
    transactions_per_customer: int = 10
    base_date: datetime = datetime(2025, 6, 1)
    time_window_days: int = 30
    cities: List[str] = None
    channels: List[str] = None
    merchants: List[str] = None
    
    def __post_init__(self):
        if self.cities is None:
            self.cities = ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Pereira',
                          'Bucaramanga', 'Ibagué', 'Espinal', 'Cartagena','Buga']
        if self.channels is None:
            self.channels = ['web', 'app', 'tarjeta_fisica', 'transferencia']
        if self.merchants is None:
            self.merchants = ['Netflix', 'Éxito', 'Amazon', 'Spotify', 
                             'MercadoLibre', 'Banco_ATM', 'Supermercado_Local']

class SyntheticDataGenerator:
    """This class generates synthetic financial transaction data based on configuration."""
    def __init__(self, config:TransactionConfig):
        self.config = config
        self.customers=None
        self.transactions = None
        self.devices= None
        
    def generate_transactions(self) -> pd.DataFrame:
        """
        Generates synthetic transactions for all customers
        """
        transaction_data = []

        # Iterar directamente sobre los pares (customer_id, city)
        for customer_id, customer_city in zip(self.customers['customer_id'], self.customers['city']):
            
            # Normal transactions
            for _ in range(self.config.transactions_per_customer):
                transaction = self._generate_normal_transaction(customer_id, customer_city)
                transaction_data.append(transaction)

        # Add a few anomalous ones
        anomalous_transactions = self._generate_anomalous_transactions()
        transaction_data.extend(anomalous_transactions)

        self.transactions = pd.DataFrame(transaction_data)
        return self.transactions
    
    
    def _generate_normal_transaction(self, customer_id: int, customer_city: str) -> Dict:
        """Generates a normal transaction for a customer"""
        delta_days = np.random.randint(0, self.config.time_window_days)
        delta_hours = np.random.randint(0, 24)
        delta_minutes = np.random.randint(0, 60)

        # Amounts follow an exponential distribution (most values small)
        amount = round(np.random.exponential(scale=100), 2)

        return {
            'customer_id': customer_id,
            'timestamp': self.config.base_date + timedelta(
                days=delta_days, hours=delta_hours, minutes=delta_minutes
            ),
            'amount': amount,
            'city': customer_city,
            'channel': random.choice(self.config.channels),
            'merchant': random.choice(self.config.merchants),
            'transaction_type': 'normal'
        }