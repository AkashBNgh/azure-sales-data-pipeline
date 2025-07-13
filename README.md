# Azure Sales Data Pipeline Project 🚗📊

This repository showcases an end-to-end data engineering project to process and analyze incremental **car sales data** using Azure Data Factory, Azure Databricks, Delta Lake, and the **Medallion Architecture**.

---

## 🛠 Tech Stack
- **Azure Data Factory** – Orchestration and data movement
- **Azure Data Lake Gen2** – Scalable storage layer
- **Azure Databricks (PySpark)** – Data transformation and cleaning
- **Delta Lake & Parquet** – Optimized data storage and querying
- **Star Schema Modeling** – For analytics-ready data

---

## 🧠 Architecture: Medallion Model
- **Bronze Layer:** Raw data ingestion
- **Silver Layer:** Cleaned and enriched data
- **Gold Layer:** Star schema tables for analytics (fact & dimensions)

---

## 📁 Project Structure

| File Name             | Description                                      |
|-----------------------|--------------------------------------------------|
| `db_notebook.py`      | Ingests raw data and loads it into Bronze layer  |
| `Silver_notebook.py`  | Performs data cleaning and transformation (Silver layer) |
| `gold_dim_branch.py`  | Builds `dim_branch` dimension table              |
| `gold_dim_date.py`    | Builds `dim_date` dimension table                |
| `gold_dim_dealer.py`  | Builds `dim_dealer` dimension table              |
| `gold_dim_model.py`   | Builds `dim_model` dimension table               |
| `gold_fact_sales.py`  | Builds `fact_sales` fact table from Silver data  |

---

## 📊 Output: Star Schema

The final output consists of:
- **Fact Table:** `fact_sales`
- **Dimension Tables:** `dim_branch`, `dim_date`, `dim_dealer`, `dim_model`

---

## 📌 Problem Statement

Built a data pipeline to handle incremental car sales data and prepare it for analysis using cloud-based tools and best practices in data engineering.

---

## 🧪 Skills Gained

- Ingesting and processing incremental data with ADF
- Using Medallion architecture in real-world ETL
- Building analytics-ready data models in Databricks
- Creating fact and dimension tables using PySpark

---

## 📎 How to Use

1. Review the notebooks in order:
   - Start with `db_notebook.py` → then `Silver_notebook.py` → then the gold layer files.
2. Make sure to configure your storage paths and schemas as per your environment.
3. Run the notebooks in Azure Databricks.

---

## 🔗 Author
**Akash B N**  
📌 [LinkedIn](www.linkedin.com/in/akash-b-n-bb7844201)  
📧 Contact: akash02bn@gmail.com

