#!/usr/bin/env python3
"""Generate tailored ATS-friendly markdown resumes per company."""

from pathlib import Path

RESUMES_DIR = Path(__file__).parent / "resumes"

CONTACT = """Dehradun, Uttarakhand, India | Open to Remote India
+91-738992221 | linkedin.com/in/spa22 | github.com/Sparsh225"""

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
    "synthires": {
        "summary": (
            "Data Engineer with 2+ years of experience building ETL/ELT pipelines, data warehouses, "
            "and distributed data systems using Python, SQL, Apache Spark, and Azure. Skilled in "
            "evaluating pipeline quality, optimizing data transformations, and applying modern data "
            "engineering practices including dbt, CDC, and cloud-native architectures. Regular user "
            "of AI coding tools (Cursor, Claude) for accelerated development and code review."
        ),
        "skills": (
            "**Languages:** Python, SQL, PySpark\n"
            "**Data Engineering:** ETL/ELT, Apache Spark, Azure Data Factory, dbt, CDC, Medallion Architecture\n"
            "**Cloud:** Microsoft Azure (Databricks, Data Lake, ADF), AWS exposure\n"
            "**Tools:** Git, Azure DevOps, Great Expectations, Delta Lake, Unity Catalog\n"
            "**Practices:** Data quality validation, pipeline optimization, distributed data systems, CI/CD"
        ),
        "bullets_extra": [
            "Experience operating production data platforms with automated validation, monitoring, and fault-tolerant ingestion patterns.",
            "Proficient in evaluating technical tradeoffs in pipeline design, schema evolution, and incremental load strategies.",
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
    "nice-software-solutions": {
        "summary": (
            "Data Integration Engineer with 2+ years of experience in ETL development, SQL, Python, "
            "and enterprise data pipeline delivery on Azure. Experienced in data transformations, "
            "pipeline testing (SIT/UAT), CI/CD deployments, and data quality governance practices."
        ),
        "skills": (
            "**Languages:** Python, SQL, PL/SQL concepts\n"
            "**ETL/Integration:** ETL/ELT development, Azure Data Factory, data transformation, API ingestion\n"
            "**Databases:** SQL Server concepts, PostgreSQL, relational data modeling\n"
            "**Cloud:** Microsoft Azure, large-scale data platform experience\n"
            "**Tools:** Git, Azure DevOps, CI/CD, data quality frameworks, test-driven pipeline development"
        ),
        "bullets_extra": [
            "Delivered production ETL pipelines with parameterized transformations, incremental loads, and deployment automation.",
            "Supported testing cycles, data validation, and production release processes for enterprise data integration projects.",
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
    "tech-solutions-ae": {
        "summary": (
            "Data Engineer with 2+ years of experience building Python-based ETL pipelines, API integrations, "
            "and cloud data workflows on Azure and AWS. Skilled in PySpark, Pandas, pipeline monitoring, "
            "troubleshooting, and delivering reliable data processing solutions for high-volume datasets."
        ),
        "skills": (
            "**Languages:** Python, SQL, PySpark\n"
            "**AWS:** AWS Glue, AWS Lambda, EMR concepts, S3, boto3 exposure\n"
            "**Data Engineering:** ETL/ELT, API integrations (JSON, REST), Pandas, large-scale data processing\n"
            "**Cloud:** Microsoft Azure (ADF, Databricks), AWS pipeline development\n"
            "**Tools:** Git, Jupyter Notebook, pipeline monitoring, troubleshooting, technical documentation"
        ),
        "bullets_extra": [
            "Developed Python ETL pipelines with API ingestion, JSON parsing, and automated data transformations.",
            "Monitored and troubleshot production pipelines, optimizing Spark jobs and data workflows for reliability.",
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
