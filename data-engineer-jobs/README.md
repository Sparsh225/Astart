# Data Engineer Job Search — Sparsh Rawat

Automated job tracking and **ATS-friendly, job-description-tailored resumes** for Data Engineer roles in **India or remote**, focused on **recent postings (last 7 days)**.

## Latest run

- **Date:** 2026-09-12
- **Job list:** [jobs-list-2026-09-12.md](jobs-list-2026-09-12.md)
- **Contact:** sparshrawat34@gmail.com | +91-7441161610

## Regenerate resumes & PDFs

```bash
pip install reportlab
python3 data-engineer-jobs/generate_resumes.py
python3 data-engineer-jobs/generate_pdfs.py
```

## Structure

| Path | Description |
|------|-------------|
| `base-profile.md` | Master profile (Celebal Technologies, DIT University, certifications) |
| `jobs-list-YYYY-MM-DD.md` | Dated snapshot of verified recent jobs |
| `resumes/*-resume.md` | One tailored markdown resume per company |
| `pdfs/*-resume.pdf` | ATS-friendly PDF per company |
