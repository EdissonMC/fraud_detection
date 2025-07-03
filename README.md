# Fraudulent Transaction Detection System

This project is focused on building a robust anomaly and fraud detection system for financial transactions, following a multi-stage approach. The initial phase centers on the generation of high-quality synthetic data, which will serve as the foundation for subsequent risk analysis and the development of advanced detection models, including LLM-based (Large Language Model) systems.

## Current Stage: Synthetic Data Generation

At this stage, we have implemented a modular Python system that programmatically generates synthetic datasets emulating real-world financial transactions. The core components are:

- **TransactionConfig**: A dataclass that encapsulates all configuration parameters for data generation, such as the number of customers, transaction frequency, available cities, channels, and merchants.
- **SyntheticDataGenerator**: This class is responsible for creating synthetic customer profiles, generating realistic transaction records (including both normal and anomalous transactions), and simulating device metadata associated with each customer. Methods like `generate_customers`, `generate_transactions`, and `generate_device_data` provide a flexible and extensible way to produce diverse datasets for experimentation and testing.

The internal structure is designed for clarity and extensibility. As the project evolves, this architecture will adapt to incorporate new analytical modules and AI components.

## Next Steps

Future phases will include:
- Implementing risk analysis algorithms on the generated data.
- Integrating LLM-based models to enhance fraud detection capabilities.
- Expanding the system to handle real-world data and more complex fraud scenarios.

The codebase and its structure will continue to evolve as we progress through these stages.

For a detailed explanation of the methodology, code, and design decisions, please refer to my blog post:  
https://medium.com/@edisson.mogolloncorrea/detecting-financial-fraud-with-python-and-pandas-part-1-a-practical-approach-92aa58b89ea4