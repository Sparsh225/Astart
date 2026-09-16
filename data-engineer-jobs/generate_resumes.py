#!/usr/bin/env python3
"""Generate tailored ATS-friendly markdown resumes per company."""

from pathlib import Path

RESUMES_DIR = Path(__file__).parent / "resumes"

CONTACT = """Dehradun, Uttarakhand, India | Open to Remote India
sparshrawat34@gmail.com | 7441161610 | linkedin.com/in/spa22 | github.com/Sparsh225"""

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
    "deepsource": {
        "summary": (
            "Data Engineer with 2+ years of experience designing scalable ETL/ELT pipelines on Azure Data "
            "Factory and Databricks using PySpark, Python, and SQL. Hands-on with Delta Lake, data quality "
            "validation, pipeline monitoring, and Databricks-certified lakehouse delivery for analytics use cases."
        ),
        "skills": (
            "**Languages:** Python, SQL, PySpark\n"
            "**Data Engineering:** ETL/ELT, ADF, Databricks Workflows, incremental processing\n"
            "**Big Data:** Apache Spark, Delta Lake, structured streaming exposure\n"
            "**Cloud:** Microsoft Azure (ADF, Databricks, Data Lake)\n"
            "**Tools:** Git, CI/CD, Great Expectations, pipeline documentation, root-cause troubleshooting"
        ),
        "bullets_extra": [
            "Optimized complex SQL and Spark workloads for performance and maintainability on production datasets.",
            "Collaborated with architects on governed data models, data dictionaries, and engineering standards.",
        ],
    },
    "atlassian": {
        "summary": (
            "Data Engineer with 2+ years of experience building batch ETL/ELT pipelines, automated data "
            "quality checks, and analytics-ready datasets on Databricks and Azure. Strong Python, SQL, dbt "
            "exposure, and Spark optimization with a focus on reliable, observable data platform delivery."
        ),
        "skills": (
            "**Languages:** Python, SQL, PySpark\n"
            "**Data Engineering:** ETL/ELT, dimensional modeling, incremental loads, dbt exposure\n"
            "**Big Data:** Databricks, Apache Spark, Delta Lake, query and partition tuning\n"
            "**Quality:** Great Expectations, validation frameworks, pipeline monitoring and alerting\n"
            "**Tools:** Git, CI/CD (Azure DevOps), technical documentation, cross-functional collaboration"
        ),
        "bullets_extra": [
            "Implemented automated data quality checks and monitoring to reduce silent failures in production pipelines.",
            "Delivered curated marts and documented transformations supporting reporting and operational analytics.",
        ],
    },
    "verve": {
        "summary": (
            "Data Engineer with 2+ years of experience writing SQL, building ETL workflows, and delivering "
            "analytics-ready datasets for reporting and dashboards. Comfortable collaborating with product, "
            "QA, and engineering teams on customer-facing data solutions and schema design for large datasets."
        ),
        "skills": (
            "**Languages:** Python, SQL\n"
            "**Analytics:** Reporting datasets, dashboard support, Power BI exposure, BI tool familiarity\n"
            "**Data Engineering:** ETL/ELT, schema design, query optimization, unstructured + structured data\n"
            "**Cloud:** Azure (ADF, Databricks, Data Lake), pipeline automation\n"
            "**Tools:** Git, data visualization concepts (Looker/Tableau-class tools), remote collaboration"
        ),
        "bullets_extra": [
            "Built SQL pipelines and validated datasets supporting operational reporting and business analytics.",
            "Partnered with cross-functional teams to troubleshoot data issues and document transformation logic.",
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
