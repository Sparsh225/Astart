# Data Engineer Job Search & Tailored Resumes

Automated daily search for **Data Engineer** roles in **India / Remote** (2+ years experience) with ATS-friendly, job-description-tailored resumes.

## Latest Run: August 31, 2026

### Quick Links
- [Job List (Aug 31, 2026)](jobs-list-2026-08-31.md)
- [Job List (Aug 30, 2026)](jobs-list-2026-08-30.md)
- [Job List (Aug 29, 2026)](jobs-list-2026-08-29.md)
- [Job List (Aug 26, 2026)](jobs-list-2026-08-26.md)
- [Base Profile](base-profile.md)

### Companies & Resumes

| Company | Role | Resume (MD) | Resume (PDF) |
|---------|------|-------------|--------------|
| Sun King | Data Engineer (2+ yrs, Remote India) | [MD](resumes/sun-king-resume.md) | [PDF](pdfs/sun-king-resume.pdf) |
| WebEngage | Data Engineer (1–3 yrs, Mumbai/Remote) | [MD](resumes/webengage-resume.md) | [PDF](pdfs/webengage-resume.pdf) |
| Cloud202 | Data Engineer (1–2 yrs, Remote India) | [MD](resumes/cloud202-resume.md) | [PDF](pdfs/cloud202-resume.pdf) |
| Zensar Technologies | GCP BigQuery Data Engineer | [MD](resumes/zensar-resume.md) | [PDF](pdfs/zensar-resume.pdf) |
| Circles.Life (Jetpac) | Data Engineer – Platform (Remote India) | [MD](resumes/jetpac-circles-resume.md) | [PDF](pdfs/jetpac-circles-resume.pdf) |
| NPS Prism | Data Engineer II (3–6 yrs, Remote) | [MD](resumes/nps-prism-resume.md) | [PDF](pdfs/nps-prism-resume.pdf) |
| Innovatix | Data Engineer (Python, Snowflake, Airflow) | [MD](resumes/innovatix-resume.md) | [PDF](pdfs/innovatix-resume.pdf) |
| Particle41 | Data Engineer – Power BI (3+ yrs, Remote) | [MD](resumes/particle41-resume.md) | [PDF](pdfs/particle41-resume.pdf) |
| NTT DATA | Data Engineer (Snowflake, Databricks) | [MD](resumes/ntt-data-resume.md) | [PDF](pdfs/ntt-data-resume.pdf) |
| Maersk | Data Engineer (Pune/Bangalore) | [MD](resumes/maersk-resume.md) | [PDF](pdfs/maersk-resume.pdf) |
| Teal India | Data Engineer (0–2 yrs, ₹9–12L) | [MD](resumes/teal-india-resume.md) | [PDF](pdfs/teal-india-resume.pdf) |
| Hired (Contract) | Data Engineer I (Remote, Contract) | [MD](resumes/hired-contract-resume.md) | [PDF](pdfs/hired-contract-resume.pdf) |
| Jobgether Partner | Data & Analytics Engineer (3–4 yrs) | [MD](resumes/jobgether-resume.md) | [PDF](pdfs/jobgether-resume.pdf) |

## Folder Structure

```
data-engineer-jobs/
├── README.md
├── base-profile.md          # Master profile for Sparsh Rawat
├── jobs-list-YYYY-MM-DD.md  # Daily job search results
├── generate_pdfs.py         # PDF generator script
├── resumes/                 # ATS-friendly markdown resumes (one per company)
└── pdfs/                    # Company-specific PDF resumes
```

## Regenerate PDFs

```bash
cd data-engineer-jobs
pip install reportlab
python3 generate_pdfs.py
```

## ATS Resume Tips Applied

- Simple single-column layout (no tables or graphics)
- Standard section headers: Summary, Skills, Experience, Education
- Keywords matched to each job description
- Quantified achievements where possible
- Contact info at top in plain text

## Note

Update placeholder contact details (email, phone, LinkedIn) in `base-profile.md` and resume files before submitting applications.
