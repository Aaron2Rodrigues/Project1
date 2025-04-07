## End to End DataScience Project

### Workflow Pipeline

1. Data Ingestion 
2. Data Validation 
3. Data Transformation 
4. Model Training
5. Model Evaluation 

## Workflows

1. Update schema.yaml
2. Update params.yaml
3. Update config.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py

![Workflow](assets/diagram1.png)

# 🧠 End-to-End Data Science Project 🚀

This repository is a comprehensive implementation of an end-to-end data science project. It includes everything from data ingestion and validation to model training, evaluation, and deployment using a modular and production-grade structure.

---

## 📁 Project Structure

The project follows a clean and modular structure to promote scalability and readability:

```bash
pp/
├── .github/workflows/          # CI/CD workflows
├── assets/                     # Contains project diagrams and images
│   ├── diagram1.png            # Project directory structure
│   ├── diagram2.png            # Output sample 1
│   └── diagram3.png            # Output sample 2
├── config/                     # Configuration files
├── research/                   # Jupyter notebooks or experiments
├── src/Project1/               # Main source code
│   ├── components/             # Modular ML components (e.g., ingestion, training)
│   ├── config/                 # Configuration management
│   ├── pipeline/               # End-to-end pipeline
│   └── utils/                  # Utility functions
├── templates/                  # HTML templates (if any)
├── app.py                      # App entry point (for Streamlit/FastAPI/etc.)
├── main.py                     # Main pipeline execution script
├── Dockerfile                  # Docker support
├── requirements.txt            # Python dependencies
├── setup.py                    # Installable package setup
├── params.yaml                 # Hyperparameters configuration
├── schema.yaml                 # Data schema definition
├── template.py                 # Template config generator
└── README.md                   # You're here!

![Workflow](assets/output1.png)
![Workflow](assets/output4.png)
![Workflow](assets/output2.png)
![Workflow](assets/output3.png)
![Workflow](assets/dagshub-output.png)