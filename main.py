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

