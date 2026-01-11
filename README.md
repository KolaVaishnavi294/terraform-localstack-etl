# 🚀 Automated Data Pipeline with Terraform, Docker & LocalStack

![CI](https://github.com/KolaVaishnavi294/terraform-localstack-etl/actions/workflows/pipeline.yml/badge.svg)

---

## 📌 Project Overview
This project implements a fully automated data pipeline using **Terraform**, **Docker**, **LocalStack**, and **GitHub Actions**.  
It demonstrates how cloud infrastructure and data processing workflows can be defined, provisioned, and executed automatically using Infrastructure as Code (IaC) and CI/CD.

All AWS services are emulated locally using **LocalStack**, so no real AWS account is required.

The pipeline performs the following:
1. Terraform creates an S3 bucket inside LocalStack  
2. A Python ETL application runs in Docker  
3. The ETL reads a CSV from `raw/` in S3  
4. It transforms the data  
5. The result is written to `processed/` in S3  
6. GitHub Actions automates everything on every push  

---

## 🏗 Architecture
```bash
GitHub Push
↓
GitHub Actions
↓
LocalStack (AWS S3)
↓
Terraform → Create S3 Bucket
↓
Docker → Run Python ETL
↓
raw/sample_data.csv → processed/output.csv
```

---

## 🧩 Technology Stack

| Component | Purpose |
|--------|---------|
Terraform | Infrastructure as Code (S3 creation) |
LocalStack | Local AWS Cloud Emulator |
Docker | Containerize ETL |
Python (Pandas, Boto3) | ETL logic |
GitHub Actions | CI/CD automation |

---

## 🗂 Project Structure
```bash
terraform-localstack-etl/
│
├── etl/
│   ├── etl.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
│
├── terraform/
│   ├── provider.tf
│   ├── main.tf
│   └── variables.tf
│
├── .github/workflows/
│   └── pipeline.yml
│
├── docker-compose.yml
├── README.md
└── sample_data.csv
```

---

## ⚙️ Local Setup (Docker Compose)

This lets you run everything locally.

### Start LocalStack and ETL

```bash
docker-compose up --build
```

This will:

- Start LocalStack

- Build ETL container

- Run ETL against LocalStack S3

### 🔄 ETL Logic

The ETL script performs:

- Reads raw/sample_data.csv from S3

- Filters rows where age > 30

- Adds a tax column (10% of salary)

- Saves the result as:
```bash
s3://etl-bucket/processed/output.csv
```

### 🧪 CI/CD Pipeline (GitHub Actions)

On every push to the main branch:

- Starts LocalStack

- Runs Terraform (terraform init & terraform apply)

- Uploads CSV to S3

- Builds Docker image

- Runs ETL container

- Verifies output file exists in processed/

- You can view this in:
```bash
GitHub → Actions tab
```

### ✅ Verification

The pipeline verifies success by checking:
```bash
s3://etl-bucket/processed/output.csv
```

If it exists, the ETL was successful.

## 🎯 What This Project Demonstrates

- Infrastructure as Code using Terraform

- Cloud service emulation using LocalStack

- Containerized ETL using Docker

- Automated CI/CD using GitHub Actions

- End-to-end DataOps workflow

## 🏁 Conclusion

This project shows how modern data pipelines can be fully automated, reproducible, and cloud-ready without requiring real cloud resources.