
# 🛠️ Anomaly Detection System for Manufacturing Sensor Data 🚀


Welcome to the **Anomaly Detection System for Manufacturing Sensor Data**! This project leverages Microsoft Fabric and a suite of Azure services to monitor manufacturing equipment in real-time, detect anomalies, and provide actionable insights to optimize maintenance and reduce downtime.

---

## 📚 Table of Contents

- [🔍 Overview](#-overview)
- [✨ Features](#-features)
- [🛠️ Technologies Used](#️️️️️️️️️️-technologies-used)
- [⚙️ Setup & Installation](#️️️️️️️️️️-setup--installation)
- [🚀 Usage](#-usage)
- [🗂️ Project Structure](#️️️️️️️️️️-project-structure)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [📞 Contact](#-contact)

---

## 🔍 Overview

Manufacturing industries rely heavily on sensor data to monitor equipment health and ensure smooth operations. Detecting anomalies early can prevent costly downtimes and extend the lifespan of machinery. This project integrates various Azure services to create a comprehensive anomaly detection pipeline:

1. **Data Ingestion:** Collects sensor data and stores it in Azure Data Lake.
2. **Anomaly Detection:** Processes data using machine learning models in Azure Machine Learning.
3. **Visualization:** Provides real-time dashboards with Power BI.
4. **Orchestration:** Automates workflows using Azure Functions.
5. **Security & Monitoring:** Ensures data security with Azure Key Vault and monitors system health with Azure Monitor.

---

## ✨ Features

- **Secure Data Storage:** Utilizes Azure Data Lake Storage Gen2 for scalable and secure data storage.
- **Machine Learning Integration:** Implements Isolation Forest algorithm for effective anomaly detection with Azure Machine Learning.
- **Automated Workflows:** Orchestrates data ingestion, processing, and reporting using Azure Functions.
- **Real-Time Visualization:** Interactive Power BI dashboards for monitoring sensor data and detected anomalies.
- **Proactive Monitoring:** Azure Monitor alerts to notify stakeholders of system issues or detected anomalies.
- **Secure Credentials Management:** Manages sensitive information with Azure Key Vault.

---

## 🛠️ Technologies Used

- **Azure Services:**
  - [Azure Data Lake Storage Gen2](https://azure.microsoft.com/en-us/services/storage/data-lake-storage/)
  - [Azure Machine Learning](https://azure.microsoft.com/en-us/services/machine-learning/)
  - [Azure Functions](https://azure.microsoft.com/en-us/services/functions/)
  - [Azure Key Vault](https://azure.microsoft.com/en-us/services/key-vault/)
  - [Azure Monitor](https://azure.microsoft.com/en-us/services/monitor/)
  - [Power BI](https://powerbi.microsoft.com/)
  
- **Programming Languages & Libraries:**
  - [Python](https://www.python.org/)
  - [Pandas](https://pandas.pydata.org/)
  - [Scikit-learn](https://scikit-learn.org/)
  - [Azure SDK for Python](https://azure.github.io/azure-sdk-for-python/)
  - [Joblib](https://joblib.readthedocs.io/)
  - [MSAL](https://github.com/AzureAD/microsoft-authentication-library-for-python)

---

## ⚙️ Setup & Installation

Follow these steps to set up and run the Anomaly Detection System locally and deploy it to Azure.

### 📋 Prerequisites

- **Azure Account:** Ensure you have an active [Azure subscription](https://azure.microsoft.com/en-us/free/).
- **Azure CLI:** Install the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) for managing Azure resources.
- **Python 3.8+:** Install [Python](https://www.python.org/downloads/) and ensure it's added to your system's PATH.
- **Git:** Install [Git](https://git-scm.com/downloads) for version control.
- **Azure Functions Core Tools:** Install [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local) for local development.

### 🔧 Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/anomaly-detection-system.git
   cd anomaly-detection-system
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Azure Services**

   - **Azure Data Lake Storage Gen2:**
     - Create a Storage Account with Data Lake Storage Gen2 enabled.
     - Note down the **Storage Account Name** and **Access Key**.
   
   - **Azure Key Vault:**
     - Create a Key Vault to store secrets.
     - Add the following secrets:
       - `storage-account-key`: Your Storage Account Access Key.
       - `azure-subscription-id`
       - `azure-resource-group`
       - `azure-ml-workspace-name`
       - `azure-ml-workspace-secret`
       - `powerbi-client-secret`
   
   - **Azure Machine Learning Workspace:**
     - Set up an Azure ML Workspace.
     - Note down the workspace details for configuration.
   
   - **Power BI:**
     - Register an application in Azure AD for Power BI API access.
     - Obtain the **Client ID**, **Client Secret**, and **Tenant ID**.

5. **Set Up Environment Variables**

   Create a `.env` file in the project root and add the necessary environment variables:

   ```env
   VAULT_URL=https://your-key-vault-name.vault.azure.net/
   STORAGE_ACCOUNT_NAME=your_storage_account_name
   STORAGE_ACCOUNT_KEY_SECRET=storage-account-key
   AZURE_SUBSCRIPTION_ID=your_subscription_id
   AZURE_RESOURCE_GROUP=your_resource_group
   AZURE_ML_WORKSPACE_NAME=your_azure_ml_workspace
   AZURE_ML_WORKSPACE_SECRET=azure-ml-workspace-secret
   POWERBI_CLIENT_ID=your_powerbi_client_id
   POWERBI_CLIENT_SECRET=your_powerbi_client_secret
   TENANT_ID=your_tenant_id
   POWERBI_WORKSPACE_ID=your_powerbi_workspace_id
   POWERBI_DATASET_ID=your_powerbi_dataset_id
   ```

6. **Run Setup Scripts**

   - **Set Up Azure Monitor Alerts**

     ```bash
     python setup_alerts.py
     ```

---

## 🚀 Usage

### 🔄 Running the Pipeline Locally

1. **Data Ingestion**

   ```bash
   python data_ingestion.py
   ```

2. **Anomaly Detection**

   ```bash
   python anomaly_detection.py
   ```

3. **Power BI Report Refresh**

   ```bash
   python powerbi_refresh.py
   ```

4. **Orchestrate the Workflow**

   Run the orchestrator script to execute all steps sequentially:

   ```bash
   python orchestrator.py
   ```

### ☁️ Deploying to Azure

1. **Deploy Azure Functions**

   ```bash
   func azure functionapp publish your-function-app-name
   ```

2. **Configure Azure Functions**

   - Ensure all environment variables are set in the Azure Function App settings.
   - Set up Timer Triggers to automate the workflow execution.

3. **Monitor and Manage**

   - Use Azure Monitor to track the health and performance of your functions.
   - View logs and set up alerts as configured.

---

## 🗂️ Project Structure

```plaintext
anomaly-detection-system/
├── data_ingestion.py           # Script for data ingestion
├── anomaly_detection.py        # Script for anomaly detection
├── powerbi_refresh.py          # Script to refresh Power BI reports
├── orchestrator.py             # Orchestrator script to run all steps
├── setup_alerts.py             # Script to set up Azure Monitor alerts
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .env                        # Environment variables (not committed)
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the Repository**

   Click the **Fork** button at the top right of this page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/yourusername/anomaly-detection-system.git
   cd anomaly-detection-system
   ```

3. **Create a Feature Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Commit Your Changes**

   ```bash
   git commit -m "Add your descriptive commit message"
   ```

5. **Push to Your Fork**

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**

   Navigate to the original repository and click **Compare & pull request**.

---

## 📜 License

This project is licensed under the [Apache 2.0 License](LICENSE).

---

## 📞 Contact

For any inquiries or support, please contact:

- **Your Name**
- **Email:** your.email@example.com
- **LinkedIn:** [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)

---

## 📝 Acknowledgements

- [Azure Documentation](https://docs.microsoft.com/en-us/azure/)
- [Power BI Documentation](https://docs.microsoft.com/en-us/power-bi/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/)

---
```
