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
    "hyper-lychee-labs": {
        "summary": (
            "Data Engineer with 2+ years of hands-on experience in Azure Data Factory, dbt, "
            "lakehouse workflows, and CI/CD for data platforms. Strong background building ADF "
            "pipelines, transformation layers, and data quality checks on Microsoft Azure with "
            "PySpark and SQL."
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
    "saaf-finance": {
        "summary": (
            "Data Engineer with 2+ years of experience in Python, SQL, PySpark, and cloud data warehouse "
            "platforms including Databricks and Azure. Hands-on building ETL pipelines, query optimization, "
            "dbt/Airflow exposure, and Git-based delivery in agile data teams."
        ),
        "skills": (
            "**Languages:** Python, SQL, PySpark\n"
            "**Data Engineering:** ETL/ELT, Databricks, Delta Lake, dbt, pipeline orchestration\n"
            "**Cloud:** Microsoft Azure, AWS exposure, lakehouse and warehouse patterns\n"
            "**Tools:** Git, GitHub, Airflow exposure, Power BI, data validation\n"
            "**Practices:** Agile delivery, performance tuning, version-controlled data workflows"
        ),
        "bullets_extra": [
            "Built production SQL and PySpark transformations with joins, aggregations, and performance-aware tuning.",
            "Maintained reliable batch pipelines with documentation and code review practices on Azure Databricks.",
        ],
    },
    "irth-solutions": {
        "summary": (
            "Data Engineer with 2+ years of hands-on Databricks, Apache Spark, PySpark, and Azure lakehouse "
            "experience. Skilled in SQL transformations, Delta Lake medallion architecture, ETL development, "
            "and implementing production-ready pipelines aligned with platform standards and governance."
        ),
        "skills": (
            "**Languages:** Python, SQL, PySpark\n"
            "**Big Data:** Databricks, Apache Spark, Delta Lake, medallion architecture\n"
            "**Cloud:** Microsoft Azure (preferred), ADF, Data Lake, Unity Catalog\n"
            "**Certifications:** Databricks Data Engineer Associate, Azure Data Engineer Associate (DP-203)\n"
            "**Tools:** Git, CI/CD, data modeling, pipeline monitoring, technical documentation"
        ),
        "bullets_extra": [
            "Translated architecture patterns into reliable batch pipelines with structured transformations and quality checks.",
            "Partnered with senior architects on lakehouse implementations, CDC ingestion, and platform hardening on Azure.",
        ],
    },
    "x-rite": {
        "summary": (
            "Data Engineer with 2+ years of experience building scalable data platforms, ETL pipelines, and "
            "analytics infrastructure. Proficient in SQL, Python, cloud data services, data modeling, and "
            "collaborating with distributed engineering and product teams across time zones."
        ),
        "skills": (
            "**Languages:** Python, SQL, PySpark\n"
            "**Data Engineering:** ETL/ELT, data warehousing, telemetry and product analytics pipelines\n"
            "**Cloud:** AWS exposure (Glue, S3 concepts), Azure (ADF, Databricks, Redshift-adjacent patterns)\n"
            "**BI & Quality:** Power BI, dbt exposure, data validation, engineering metrics\n"
            "**Tools:** Git, GitHub, Jira/Azure DevOps, CI/CD, distributed team collaboration"
        ),
        "bullets_extra": [
            "Engineered ingestion and transformation workflows supporting analytics, quality metrics, and operational reporting.",
            "Documented pipelines and data models for cross-functional consumers in global, remote-first teams.",
        ],
    },
    "harris-gbs": {
        "summary": (
            "Software Engineer focused on data systems and ETL with 2+ years of experience in SQL, Python, "
            "multi-step ETL processes, and cloud data warehouse environments. Comfortable owning pipeline "
            "reliability, billing-adjacent data flows, APIs, and containerized services with strong communication."
        ),
        "skills": (
            "**Languages:** Python, SQL\n"
            "**Data Systems:** ETL/ELT, high-volume SQL processing, pipeline troubleshooting, data quality\n"
            "**Cloud:** Azure, AWS Redshift concepts, cloud security fundamentals\n"
            "**Engineering:** REST/GraphQL API exposure, Git, unit testing, technical documentation\n"
            "**Tools:** Docker/container basics, CI/CD, AI-assisted development (Cursor)"
        ),
        "bullets_extra": [
            "Maintained end-to-end ETL workflows with error handling, monitoring, and performance tuning on cloud warehouses.",
            "Produced unit tests, specs, and peer-reviewed code for production data systems in agile delivery.",
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
