#!/usr/bin/env python3
"""Generate tailored ATS-friendly markdown resumes per company."""

from pathlib import Path

RESUMES_DIR = Path(__file__).parent / "resumes"

CONTACT = """Dehradun, Uttarakhand, India | Open to Remote India
sparshrawat34@gmail.com | +91-7441161610 | linkedin.com/in/spa22 | github.com/Sparsh225"""

EXPERIENCE_CELEBAL = """### Associate Data Engineer | Celebal Technologies | Pune, India
**August 2024 – Present**

- Built and maintained production ETL/ELT pipelines using Azure Data Factory, Databricks, and PySpark processing large-scale enterprise datasets.
- Implemented Delta Lake lakehouse architecture with Bronze/Silver/Gold medallion layers, Unity Catalog governance, and row/column-level security.
- Developed CDC-based ingestion and metadata-driven pipeline frameworks for reliable batch data movement across Azure Data Lake and curated layers.
- Applied data quality checks using Great Expectations and validation frameworks, reducing silent data failures in downstream analytics.
- Optimized Spark jobs and SQL transformations for performance, cost efficiency, and scalability on Azure Databricks.
- Created dbt models, architecture documentation, and solution proposals; mentored junior engineers on data engineering best practices.
- Contributed to POCs involving Delta Live Tables (DLT), Asset Bundles, and modern lakehouse platform design."""

EXPERIENCE_INTERN = """### Software Developer Intern | Upraised | Bengaluru, India
**May 2024 – August 2024**

- Delivered production features using React, TypeScript, and GraphQL; resolved 50+ bugs and shipped 5 key product enhancements.
- Worked with data querying patterns via GraphQL/Apollo in a monorepo microfrontend architecture."""

EDUCATION = """**Bachelor of Technology in Computer Engineering**
DIT University, Dehradun | 2020 – 2024 | CGPA: 8.4"""

CERTS = """- 5x Microsoft Certified (including Azure Data Engineer Associate DP-203)
- 4x Databricks Certified (Data Engineer, Lakehouse, Fundamentals, Generative AI)"""

JOBS = {
    "x-rite": {
        "summary": (
            "Data Engineer with 2+ years of experience building scalable data pipelines, data lake "
            "architectures, and analytics-ready datasets using Python, SQL, Spark, and cloud platforms. "
            "Skilled in API/database ingestion, ETL/ELT, data modeling, data quality, monitoring, and "
            "delivering reliable datasets for product analytics, engineering metrics, and reporting."
        ),
        "skills": (
            "**Languages:** Python, SQL, PySpark, JavaScript/TypeScript exposure\n"
            "**Data Engineering:** ETL/ELT, data modeling, data warehousing, API ingestion, telemetry pipelines\n"
            "**Cloud:** Microsoft Azure (ADF, Databricks, Data Lake), AWS (Redshift, Glue concepts)\n"
            "**BI & Tools:** Power BI, dbt, Git, Azure DevOps, Great Expectations, Delta Lake\n"
            "**Practices:** Data quality, governance, monitoring/alerting, documentation, cross-functional collaboration"
        ),
        "bullets_extra": [
            "Integrated data from APIs, databases, and batch sources into curated analytics layers with traceability and validation.",
            "Built monitoring and data quality checks for production pipelines supporting engineering and product analytics use cases.",
        ],
    },
    "firmable": {
        "summary": (
            "Data Engineer with 2+ years of experience building scalable data pipelines, orchestration "
            "workflows, and reliable data platforms using Python, SQL, PySpark, Airflow, and Kafka. "
            "Experienced in data quality, observability, cost-aware pipeline design, and delivering "
            "trustworthy datasets for analytics and downstream consumers."
        ),
        "skills": (
            "**Languages:** Python, SQL, PySpark\n"
            "**Data Engineering:** ETL/ELT, Airflow, Kafka, Spark, pipeline orchestration, data quality\n"
            "**Cloud:** Microsoft Azure, AWS exposure, cloud-native data platforms\n"
            "**Databases:** PostgreSQL concepts, data warehouse/lakehouse patterns\n"
            "**Tools:** Git, CI/CD, Great Expectations, observability and cost optimization practices"
        ),
        "bullets_extra": [
            "Designed reliable ingestion and transformation pipelines with validation, monitoring, and documentation for production data products.",
            "Optimized Spark jobs and SQL workflows for performance, reliability, and cost efficiency across large-scale datasets.",
        ],
    },
    "hyper-lychee-labs": {
        "summary": (
            "Data Engineer with 2+ years of hands-on experience in Azure Data Factory, dbt, Snowflake-adjacent "
            "lakehouse workflows, and CI/CD for data platforms. Strong background building ADF pipelines, "
            "transformation layers, and data quality checks on Microsoft Azure with PySpark and SQL."
        ),
        "skills": (
            "**Languages:** Python, SQL, PySpark\n"
            "**Cloud & ETL:** Azure Data Factory, Azure Data Lake (ADLS Gen2), Azure DevOps, CI/CD\n"
            "**Transformation:** dbt, Delta Lake, ETL/ELT pipeline design\n"
            "**Warehousing:** Snowflake concepts, dimensional modeling, incremental loads\n"
            "**Tools:** Git, Databricks, Great Expectations, data validation frameworks"
        ),
        "bullets_extra": [
            "Built ADF orchestration workflows with parameterized pipelines, error handling, and deployment via Azure DevOps.",
            "Developed dbt transformation models with testing and documentation for analytics-ready curated datasets.",
        ],
    },
    "brightedge": {
        "summary": (
            "Backend/Data Engineer with 2+ years of experience designing scalable, reliable data-intensive "
            "systems using Python, SQL, and cloud platforms. Experienced in building automated data pipelines, "
            "API-driven ingestion, and AI-assisted development workflows for faster, cleaner delivery."
        ),
        "skills": (
            "**Languages:** Python, SQL, JavaScript/TypeScript\n"
            "**Backend & Data:** REST APIs, ETL/ELT pipelines, data automation, PostgreSQL/SQL databases\n"
            "**Cloud:** Azure (ADF, Databricks, Data Lake), distributed data processing with Spark\n"
            "**Tools:** Git, Azure DevOps, CI/CD, AI coding assistants (Cursor, Claude)\n"
            "**Practices:** Data quality, observability, scalable backend architecture"
        ),
        "bullets_extra": [
            "Designed metadata-driven ingestion frameworks and automated data workflows reducing manual pipeline maintenance.",
            "Used AI-assisted coding tools to accelerate development, debugging, and code review in production environments.",
        ],
    },
    "bdiplus": {
        "summary": (
            "Data Engineer with 2+ years of experience supporting data platform quality, certification, "
            "and pipeline reliability on Azure and Databricks. Skilled in Python, SQL, PySpark, data "
            "validation, governance, and building testable ETL/ELT workflows for enterprise analytics."
        ),
        "skills": (
            "**Languages:** Python, SQL, PySpark\n"
            "**Data Engineering:** ETL/ELT, Azure Data Factory, Databricks, Delta Lake\n"
            "**Quality & Governance:** Great Expectations, data validation, Unity Catalog, metadata management\n"
            "**Cloud:** Microsoft Azure (Data Lake, ADF, DevOps)\n"
            "**Tools:** Git, CI/CD, dbt, data modeling, pipeline monitoring"
        ),
        "bullets_extra": [
            "Implemented automated data quality checks and certification workflows for production pipeline releases.",
            "Supported data platform testing, validation, and documentation for analytics and certification use cases.",
        ],
    },
    "unitedhealth-group": {
        "summary": (
            "Data Engineer with 2+ years of experience in cloud data engineering, big data processing, "
            "and pipeline architecture on Azure and Spark. Proficient in Python, SQL, Java, ETL/ELT, "
            "data modeling, and agile delivery of scalable data solutions for enterprise platforms."
        ),
        "skills": (
            "**Languages:** Python, SQL, Java, PySpark\n"
            "**Big Data:** Apache Spark, Hadoop, Databricks, distributed data processing\n"
            "**Cloud:** Microsoft Azure (ADF, Databricks, Data Lake), AWS exposure\n"
            "**Data Engineering:** ETL/ELT, data modeling, data warehousing, pipeline migration\n"
            "**Tools:** Git, Azure DevOps, Agile/Scrum, troubleshooting, CI/CD"
        ),
        "bullets_extra": [
            "Designed extensible pipeline architectures with data quality, security, and governance controls using Unity Catalog.",
            "Executed POCs and production migrations for cloud-native data platform modernization on Azure.",
        ],
    },
    "century-health": {
        "summary": (
            "Data Engineer with 2+ years of experience building scalable data pipelines and analytics "
            "infrastructure using Python, SQL, Spark, and cloud platforms. Experienced in ETL/ELT, data "
            "modeling, data quality, and remote collaboration on production data platform delivery."
        ),
        "skills": (
            "**Languages:** Python, SQL, PySpark\n"
            "**Data Engineering:** ETL/ELT, Apache Spark, Databricks, Delta Lake\n"
            "**Cloud:** Microsoft Azure, distributed data systems\n"
            "**Tools:** Git, dbt, Great Expectations, CI/CD, data observability\n"
            "**Practices:** Data modeling, pipeline reliability, remote team collaboration"
        ),
        "bullets_extra": [
            "Delivered end-to-end data pipelines from ingestion through curated analytics layers on Azure.",
            "Implemented data quality monitoring and validation to ensure reliable datasets for downstream consumers.",
        ],
    },
}


def build_resume(company: str, config: dict) -> str:
    bullets = config.get("bullets_extra", [])
    extra_bullets = "\n".join(f"- {b}" for b in bullets)

    return f"""# Sparsh Rawat

{CONTACT}

---

## PROFESSIONAL SUMMARY

{config['summary']}

---

## TECHNICAL SKILLS

{config['skills']}

---

## PROFESSIONAL EXPERIENCE

{EXPERIENCE_CELEBAL}
{extra_bullets}

{EXPERIENCE_INTERN}

---

## EDUCATION

{EDUCATION}

---

## CERTIFICATIONS

{CERTS}
"""


def main() -> None:
    RESUMES_DIR.mkdir(parents=True, exist_ok=True)
    for company, config in JOBS.items():
        path = RESUMES_DIR / f"{company}-resume.md"
        path.write_text(build_resume(company, config), encoding="utf-8")
        print(f"Generated: {path}")


if __name__ == "__main__":
    main()
