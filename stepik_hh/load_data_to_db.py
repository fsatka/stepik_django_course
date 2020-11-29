import os
import django

from vc import data


def setup_db():
    os.environ["DJANGO_SETTINGS_MODULE"] = 'stepik_hh.settings'
    django.setup()


if __name__ == "__main__":
    setup_db()
    from vc import models

    for specialization in data.specialties:
        specialization_object = models.Specialty(**specialization)
        specialization_object.save()

    for company in data.companies:
        company_object = models.Company(**company)
        company_object.save()

    for job in data.jobs:
        company_object = models.Company.objects.get(id=job["company"])
        specialization_object = models.Specialty.objects.get(code=job["specialty"])
        job_object = models.Vacancy(
            title=job["title"],
            specialty=specialization_object,
            company=company_object,
            skills=job["skills"],
            description=job["description"],
            salary_min=job["salary_from"],
            salary_max=job["salary_to"],
            published_at=job["posted"],
        )
        job_object.save()
