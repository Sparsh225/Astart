#!/usr/bin/env python3
"""Generate ATS-friendly PDF resumes tailored per company."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib import colors
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(BASE_DIR, "pdfs")
RESUME_DIR = os.path.join(BASE_DIR, "resumes")

CONTACT = {
    "name": "Sparsh Rawat",
    "title": "Data Engineer",
    "location": "Dehradun, Uttarakhand, India",
    "email": "rawat.sparsh@feg.eu",
    "phone": "+91-XXXXXXXXXX",
    "linkedin": "linkedin.com/in/spa22",
    "github": "github.com/Sparsh225",
}

EDUCATION = [
    "Bachelor of Technology, Computer Engineering — DIT University, Dehradun (2020–2024) | CGPA: 8.4",
]

CERTIFICATIONS = [
    "Microsoft Certified: Fabric Data Engineer Associate (DP-700)",
    "Databricks Certified Data Engineer Associate & Professional",
    "Databricks Lakehouse Fundamentals | Databricks Generative AI Fundamentals",
    "Microsoft Azure Data Fundamentals (DP-900) | Azure Fundamentals (AZ-900)",
]

EXPERIENCE_BASE = {
    "celebal": {
        "title": "Associate Data Engineer",
        "company": "Celebal Technologies",
        "dates": "August 2024 – Present",
        "location": "Pune, India (Remote/Hybrid)",
    },
    "upraised": {
        "title": "Software Developer Intern",
        "company": "Upraised",
        "dates": "May 2024 – August 2024",
        "location": "Bengaluru, India",
    },
}

COMPANY_RESUMES = {
    "sun_king": {
        "company_name": "Sun King",
        "headline": "Data Engineer | Python, SQL, PySpark, Airflow, AWS | 2+ Years",
        "summary": (
            "Data Engineer with 2+ years of experience building scalable ETL/ELT pipelines, "
            "real-time data architectures, and cloud-based data solutions. Proficient in Python, SQL, "
            "Apache Spark (PySpark), Apache Airflow, and AWS services including Glue, Lambda, S3, and EC2. "
            "Experienced in REST API integrations, data quality monitoring, alerting systems, and "
            "optimizing data storage and processing costs. Passionate about enabling data-driven "
            "decision-making in high-impact organizations."
        ),
        "skills": [
            "Python", "SQL", "PySpark", "Apache Spark", "Apache Airflow", "Apache Kafka",
            "AWS Glue", "AWS Lambda", "Amazon S3", "Amazon EC2", "Amazon Redshift",
            "ETL/ELT", "REST API Integration", "NoSQL Databases", "Data Pipeline Development",
            "Real-Time Data Processing", "Data Quality", "CI/CD", "Git",
        ],
        "bullets_celebal": [
            "Designed and implemented ETL/ELT pipelines using Azure Data Factory, PySpark, and Databricks for enterprise analytics workloads.",
            "Built scalable data processing workflows with Apache Spark handling large-scale datasets with performance optimization.",
            "Developed REST API integration pipelines for ingesting third-party and application data into centralized data platforms.",
            "Implemented data quality validation frameworks using Great Expectations to detect and alert on data discrepancies.",
            "Optimized SQL queries and pipeline performance, reducing data processing time and cloud compute costs.",
            "Managed CI/CD deployments for data pipelines using Azure DevOps and Git version control.",
            "Collaborated with BI and analytics teams to deliver clean, reliable datasets for dashboards and reporting.",
        ],
        "bullets_upraised": [
            "Developed data querying solutions using GraphQL and TypeScript, improving application data access patterns.",
            "Resolved 50+ production bugs and delivered 5 key features, strengthening software reliability.",
        ],
        "projects": [
            "Enterprise Lakehouse Pipeline — Built medallion architecture pipelines on Databricks with Delta Lake, CDC ingestion, and automated data quality checks.",
        ],
    },
    "webengage": {
        "company_name": "WebEngage",
        "headline": "Data Engineer | ETL/ELT, Python, SQL, Data Modeling | 2+ Years",
        "summary": (
            "Data Engineer with 2+ years of experience owning end-to-end data lifecycles — from ingesting "
            "raw event streams and APIs to building well-modeled, reliable datasets for analytics and ML. "
            "Strong in Python (Pandas-style scripting), SQL, ETL/ELT pipeline design, dimensional data modeling, "
            "data quality assertions, pipeline observability, and CI/CD automation. Experienced in designing for "
            "cost efficiency, maintainability, and long-term data warehouse architecture."
        ),
        "skills": [
            "Python", "SQL", "ETL/ELT", "Data Modeling", "Dimensional Modeling", "Star Schema",
            "Apache Spark", "Databricks", "Azure Data Factory", "Event Hubs", "Kafka",
            "Data Quality", "Great Expectations", "DBT", "CI/CD", "Git", "Data Warehousing",
            "Incremental Loads", "Backfills", "Pipeline Observability",
        ],
        "bullets_celebal": [
            "Owned end-to-end ETL/ELT pipelines ingesting data from APIs, databases, and event streams into centralized data warehouses.",
            "Designed dimensional and transactional data models with incremental load strategies and backfill procedures.",
            "Implemented data quality assertions and validation frameworks treating silent data failures as critical incidents.",
            "Built modular, well-tested Python and SQL transformation logic with Git-based code review workflows.",
            "Optimized complex SQL queries for performance and cost efficiency on cloud data warehouse platforms.",
            "Automated pipeline deployments via CI/CD, ensuring reproducible and maintainable data workflows.",
            "Collaborated with analytics and product teams to translate business requirements into optimized table structures.",
        ],
        "bullets_upraised": [
            "Built frontend data features using React, TypeScript, and GraphQL for recruiter and applicant applications.",
            "Improved application stability by resolving 50+ bugs and shipping 5 production features.",
        ],
        "projects": [
            "Event-Driven Ingestion Pipeline — Designed CDC-based ingestion with metadata-driven frameworks and data validation gates.",
        ],
    },
    "nps_prism": {
        "company_name": "NPS Prism",
        "headline": "Data Engineer | Databricks, PySpark, Python, SQL, Azure/AWS | 2+ Years",
        "summary": (
            "Data Engineer with 2+ years of hands-on experience in Python, SQL, and PySpark on Databricks "
            "and cloud platforms (Azure, AWS). Expert in building and optimizing ETL/ELT workflows, data lakes, "
            "and data warehouses with CI/CD automation. Strong background in Apache Spark distributed computing, "
            "data quality checks, Git version control, and cross-functional collaboration with data scientists "
            "and business stakeholders."
        ),
        "skills": [
            "Python", "SQL", "PySpark", "Databricks", "Apache Spark", "Delta Lake",
            "Azure Data Factory", "AWS Glue", "Azure", "AWS", "ETL/ELT",
            "Data Lakes", "Data Warehouses", "CI/CD", "Azure DevOps", "Git", "Jenkins",
            "Data Quality", "Unity Catalog", "DBT", "Distributed Systems",
        ],
        "bullets_celebal": [
            "Designed, built, and optimized ETL/ELT workflows using Databricks, PySpark, SQL, and Azure Data Factory.",
            "Developed scalable data pipelines on Azure and AWS cloud platforms for data lakes and data warehouses.",
            "Leveraged Apache Spark for distributed computing and complex data transformations at enterprise scale.",
            "Implemented data quality checks and validation mechanisms ensuring high availability and performance.",
            "Built CI/CD pipelines with Azure DevOps and Git for automated testing and deployment of data workflows.",
            "Created and enforced data governance policies using Unity Catalog including RLS and CLS.",
            "Collaborated with cross-functional teams to translate business requirements into technical data solutions.",
            "Maintained documentation for data workflows, pipelines, and architecture diagrams.",
        ],
        "bullets_upraised": [
            "Developed production features using Python-adjacent TypeScript stack with GraphQL data layer.",
        ],
        "projects": [
            "Databricks Lakehouse Platform — End-to-end pipeline from ADF ingestion through Delta Live Tables with governance and observability.",
        ],
    },
    "cloud202": {
        "company_name": "Cloud202",
        "headline": "Data Engineer | AWS Glue, Python, SQL, Data Quality, Lakehouse | 2+ Years",
        "summary": (
            "Data Engineer with 2+ years building production data pipelines on cloud platforms with a focus on "
            "data quality, reproducibility, and audit-ready lineage. Hands-on with AWS data services (S3, Glue, "
            "Lambda), Python, SQL, medallion lakehouse patterns, schema enforcement, and validation frameworks. "
            "Experienced in deterministic transforms, gated quality stages, and building trusted datasets for "
            "analytics and AI applications."
        ),
        "skills": [
            "Python", "SQL", "AWS Glue", "Amazon S3", "AWS Lambda", "Amazon Kinesis",
            "Apache Spark", "PySpark", "Delta Lake", "Medallion Architecture",
            "Data Quality", "Great Expectations", "Schema Enforcement", "ETL/ELT",
            "Data Lineage", "CI/CD", "Git", "Iceberg", "Step Functions",
        ],
        "bullets_celebal": [
            "Built production ETL pipelines on AWS Glue and Azure Data Factory turning raw sources into trusted analytical datasets.",
            "Implemented medallion lakehouse architecture (Bronze/Silver/Gold) with Delta Lake for governed data storage.",
            "Designed data quality gates and validation frameworks using Great Expectations as first-class pipeline stages.",
            "Developed Python and SQL transformations with schema enforcement and reproducible, auditable workflows.",
            "Created metadata-driven ingestion frameworks with end-to-end lineage tracking for enterprise compliance.",
            "Optimized S3 storage and Glue job performance for cost-efficient large-scale data processing.",
            "Collaborated with architecture teams on data platform design for analytics and AI readiness.",
        ],
        "bullets_upraised": [
            "Built API integration features and data access layers using GraphQL and REST patterns.",
        ],
        "projects": [
            "Agent-Ready Data Layer — Designed governed ingestion pipelines with quality validation and lineage for downstream AI consumption.",
        ],
    },
    "v4c_ai": {
        "company_name": "v4c.ai",
        "headline": "Data Engineer | Databricks, PySpark, Python, SQL, ADF, Spark | 2+ Years",
        "summary": (
            "Databricks-certified Data Engineer with 2+ years designing and maintaining large-scale data systems "
            "and scalable ETL pipelines. Strong proficiency in Python, SQL, PySpark, Apache Spark, Azure Data Factory, "
            "and data modeling. Experienced with Hadoop/Big Data ecosystems, Kafka, cloud platforms (Azure, AWS), "
            "and actively upskilling in Databricks Lakehouse and AI/ML enablement. 4x Databricks Certified."
        ),
        "skills": [
            "Python", "SQL", "PySpark", "Databricks", "Apache Spark", "Delta Lake",
            "Azure Data Factory", "Kafka", "Event Hubs", "Hadoop", "Big Data",
            "ETL", "Data Modeling", "Snowflake", "Azure", "AWS", "Scala",
            "CI/CD", "Git", "AI/ML Data Enablement", "Unity Catalog",
        ],
        "bullets_celebal": [
            "Designed, developed, and maintained large-scale data systems and ETL processes on Databricks and Azure.",
            "Built scalable and efficient data pipelines using PySpark, Spark, and ADF for enterprise clients.",
            "Implemented data models and collaborated with cross-functional teams on Lakehouse architecture.",
            "Troubleshot and optimized data systems for performance, scalability, and cost efficiency.",
            "Transitioned and delivered Databricks Lakehouse projects including Delta Live Tables and Asset Bundles.",
            "Worked with Kafka/Event Hubs for real-time streaming data ingestion and processing.",
            "Mentored junior engineers and conducted technical workshops on Databricks best practices.",
        ],
        "bullets_upraised": [
            "Delivered full-stack features with strong data layer integration using GraphQL.",
        ],
        "projects": [
            "Databricks Lakehouse Migration — Led pipeline development for enterprise analytics platform modernization on Databricks.",
        ],
    },
    "innovatix": {
        "company_name": "Innovatix",
        "headline": "Data Engineer | Python, Snowflake, Airflow, SQL, AWS | 2+ Years",
        "summary": (
            "Data Engineer with 2+ years developing scalable data pipelines, ETL/ELT processes, and data workflows "
            "on cloud platforms. Proficient in Python, SQL, workflow orchestration (Airflow/ADF), and AWS data services. "
            "Experienced in enterprise data sourcing, integration, transformation, and preparing high-quality data "
            "for analytics and AI initiatives."
        ),
        "skills": [
            "Python", "SQL", "Apache Airflow", "Azure Data Factory", "AWS Glue",
            "Amazon S3", "Snowflake", "Databricks", "ETL/ELT", "Data Pipelines",
            "Data Warehousing", "Data Integration", "Data Sourcing", "CI/CD", "Git",
            "Apache Spark", "PySpark", "Data Governance",
        ],
        "bullets_celebal": [
            "Developed and maintained scalable ETL/ELT data pipelines and workflows for enterprise analytics platforms.",
            "Sourced, integrated, and transformed data from complex enterprise environments using Python and SQL.",
            "Built orchestration workflows using Azure Data Factory with Airflow-equivalent scheduling and monitoring.",
            "Worked with cloud data platforms on AWS (Glue, S3) and Azure for data warehouse solutions.",
            "Implemented data quality and governance frameworks ensuring reliable, accessible enterprise data.",
            "Prepared and structured datasets to support analytics, reporting, and AI/ML use cases.",
            "Documented data workflows and maintained version-controlled pipeline code in Git.",
        ],
        "bullets_upraised": [
            "Integrated application data layers using GraphQL and REST API patterns.",
        ],
        "projects": [
            "Enterprise Data Pipeline — Built end-to-end ingestion and transformation pipeline with governance and quality controls.",
        ],
    },
    "teal_india": {
        "company_name": "Teal India",
        "headline": "Data Engineer | Python, SQL, API Ingestion, ETL Pipelines | 2+ Years",
        "summary": (
            "Data Engineer with 2+ years building data pipelines, scraping and ingesting data from external APIs, "
            "websites, and third-party providers. Strong programmatic thinker with Python and SQL skills, experienced "
            "in scoping data sources, ETL workflows, and delivering clean datasets for analytics platforms. "
            "Comfortable breaking complex problems into small, actionable steps and shipping iteratively."
        ),
        "skills": [
            "Python", "SQL", "API Integration", "Web Scraping", "ETL/ELT",
            "Data Ingestion", "REST APIs", "Data Pipelines", "Pandas",
            "Data Validation", "Git", "PostgreSQL", "MySQL", "Data Modeling",
        ],
        "bullets_celebal": [
            "Built data ingestion pipelines from APIs, databases, and external data providers into centralized platforms.",
            "Scoped and evaluated new data sources, assessing complementarity with existing datasets.",
            "Wrote clean Python and SQL code for data extraction, transformation, and integration.",
            "Implemented data validation and quality checks on ingested datasets.",
            "Designed metadata-driven frameworks for repeatable, programmatic data collection workflows.",
            "Collaborated with analytics teams to deliver structured datasets for due diligence and reporting.",
        ],
        "bullets_upraised": [
            "Built API-driven features using GraphQL and REST integrations for production applications.",
            "Resolved 50+ bugs demonstrating strong debugging and programmatic problem-solving skills.",
        ],
        "projects": [
            "Multi-Source Ingestion Framework — Automated pipeline ingesting data from APIs and flat files with validation gates.",
        ],
    },
}


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="ResumeName", fontName="Helvetica-Bold", fontSize=16,
        alignment=TA_CENTER, spaceAfter=2, textColor=colors.black,
    ))
    styles.add(ParagraphStyle(
        name="ResumeHeadline", fontName="Helvetica", fontSize=10,
        alignment=TA_CENTER, spaceAfter=4, textColor=colors.HexColor("#333333"),
    ))
    styles.add(ParagraphStyle(
        name="ResumeContact", fontName="Helvetica", fontSize=9,
        alignment=TA_CENTER, spaceAfter=10, textColor=colors.HexColor("#333333"),
    ))
    styles.add(ParagraphStyle(
        name="SectionHeader", fontName="Helvetica-Bold", fontSize=11,
        spaceBefore=8, spaceAfter=4, textColor=colors.black,
    ))
    styles.add(ParagraphStyle(
        name="BodyText2", fontName="Helvetica", fontSize=9.5,
        spaceAfter=3, leading=12, textColor=colors.black,
    ))
    styles.add(ParagraphStyle(
        name="JobTitle", fontName="Helvetica-Bold", fontSize=10,
        spaceBefore=4, spaceAfter=1, textColor=colors.black,
    ))
    styles.add(ParagraphStyle(
        name="JobMeta", fontName="Helvetica-Oblique", fontSize=9,
        spaceAfter=3, textColor=colors.HexColor("#444444"),
    ))
    styles.add(ParagraphStyle(
        name="ResumeBullet", fontName="Helvetica", fontSize=9.5,
        leftIndent=12, spaceAfter=2, leading=12, bulletIndent=0,
        textColor=colors.black,
    ))
    return styles


def section_line():
    return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#999999"), spaceAfter=4)


def company_slug(name: str) -> str:
    return name.replace(".", "_").replace(" ", "_")


def generate_pdf(company_key, resume_data):
    filename = f"Sparsh_Rawat_Resume_{company_slug(resume_data['company_name'])}.pdf"
    filepath = os.path.join(PDF_DIR, filename)

    doc = SimpleDocTemplate(
        filepath, pagesize=letter,
        leftMargin=0.65 * inch, rightMargin=0.65 * inch,
        topMargin=0.55 * inch, bottomMargin=0.55 * inch,
    )
    styles = build_styles()
    story = []

    story.append(Paragraph(CONTACT["name"], styles["ResumeName"]))
    story.append(Paragraph(resume_data["headline"], styles["ResumeHeadline"]))
    contact_line = (
        f'{CONTACT["location"]} | {CONTACT["email"]} | {CONTACT["phone"]} | '
        f'{CONTACT["linkedin"]} | {CONTACT["github"]}'
    )
    story.append(Paragraph(contact_line, styles["ResumeContact"]))
    story.append(section_line())

    story.append(Paragraph("PROFESSIONAL SUMMARY", styles["SectionHeader"]))
    story.append(Paragraph(resume_data["summary"], styles["BodyText2"]))

    story.append(Paragraph("TECHNICAL SKILLS", styles["SectionHeader"]))
    skills_text = " | ".join(resume_data["skills"])
    story.append(Paragraph(skills_text, styles["BodyText2"]))

    story.append(Paragraph("PROFESSIONAL EXPERIENCE", styles["SectionHeader"]))
    exp = EXPERIENCE_BASE["celebal"]
    story.append(Paragraph(f'{exp["title"]} | {exp["company"]}', styles["JobTitle"]))
    story.append(Paragraph(f'{exp["dates"]} | {exp["location"]}', styles["JobMeta"]))
    for bullet in resume_data["bullets_celebal"]:
        story.append(Paragraph(f"• {bullet}", styles["ResumeBullet"]))

    exp2 = EXPERIENCE_BASE["upraised"]
    story.append(Paragraph(f'{exp2["title"]} | {exp2["company"]}', styles["JobTitle"]))
    story.append(Paragraph(f'{exp2["dates"]} | {exp2["location"]}', styles["JobMeta"]))
    for bullet in resume_data["bullets_upraised"]:
        story.append(Paragraph(f"• {bullet}", styles["ResumeBullet"]))

    story.append(Paragraph("PROJECTS", styles["SectionHeader"]))
    for proj in resume_data["projects"]:
        story.append(Paragraph(f"• {proj}", styles["ResumeBullet"]))

    story.append(Paragraph("EDUCATION", styles["SectionHeader"]))
    for edu in EDUCATION:
        story.append(Paragraph(f"• {edu}", styles["ResumeBullet"]))

    story.append(Paragraph("CERTIFICATIONS", styles["SectionHeader"]))
    for cert in CERTIFICATIONS:
        story.append(Paragraph(f"• {cert}", styles["ResumeBullet"]))

    doc.build(story)
    return filepath


def generate_markdown(company_key, resume_data):
    filename = f"Sparsh_Rawat_Resume_{company_slug(resume_data['company_name'])}.md"
    filepath = os.path.join(RESUME_DIR, filename)

    lines = [
        f"# {CONTACT['name']}",
        f"## {resume_data['headline']}",
        "",
        f"**Location:** {CONTACT['location']}  ",
        f"**Email:** {CONTACT['email']}  ",
        f"**Phone:** {CONTACT['phone']}  ",
        f"**LinkedIn:** {CONTACT['linkedin']}  ",
        f"**GitHub:** {CONTACT['github']}  ",
        "",
        "---",
        "",
        "## Professional Summary",
        "",
        resume_data["summary"],
        "",
        "## Technical Skills",
        "",
        " | ".join(resume_data["skills"]),
        "",
        "## Professional Experience",
        "",
        f"### {EXPERIENCE_BASE['celebal']['title']} | {EXPERIENCE_BASE['celebal']['company']}",
        f"*{EXPERIENCE_BASE['celebal']['dates']} | {EXPERIENCE_BASE['celebal']['location']}*",
        "",
    ]
    for b in resume_data["bullets_celebal"]:
        lines.append(f"- {b}")
    lines += [
        "",
        f"### {EXPERIENCE_BASE['upraised']['title']} | {EXPERIENCE_BASE['upraised']['company']}",
        f"*{EXPERIENCE_BASE['upraised']['dates']} | {EXPERIENCE_BASE['upraised']['location']}*",
        "",
    ]
    for b in resume_data["bullets_upraised"]:
        lines.append(f"- {b}")
    lines += ["", "## Projects", ""]
    for p in resume_data["projects"]:
        lines.append(f"- {p}")
    lines += ["", "## Education", ""]
    for e in EDUCATION:
        lines.append(f"- {e}")
    lines += ["", "## Certifications", ""]
    for c in CERTIFICATIONS:
        lines.append(f"- {c}")
    lines.append("")

    with open(filepath, "w") as f:
        f.write("\n".join(lines))
    return filepath


def main():
    os.makedirs(PDF_DIR, exist_ok=True)
    os.makedirs(RESUME_DIR, exist_ok=True)
    generated = []
    for key, data in COMPANY_RESUMES.items():
        md_path = generate_markdown(key, data)
        pdf_path = generate_pdf(key, data)
        generated.append((key, md_path, pdf_path))
        print(f"Generated: {pdf_path}")

    print(f"\nTotal resumes generated: {len(generated)}")


if __name__ == "__main__":
    main()
