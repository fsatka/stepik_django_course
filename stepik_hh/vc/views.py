from django.db.models import Count
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404

# Create your views here.
from django.views.generic import TemplateView

from vc.models import Vacancy, Company


class MainView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["specializations"] = self._specializations
        context["companies"] = self._companies
        return context

    @property
    def _specializations(self):
        return Vacancy.objects.values(
            'specialty__code', 'specialty__title', 'specialty__specty'
        ).annotate(count=Count('specialty__title'))

    @property
    def _companies(self):
        return Vacancy.objects.values(
            'company__id', 'company__title', 'company__logo'
        ).annotate(count=Count('company__title'))


class VacanciesView(TemplateView):
    template_name = "vacancies.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies"] = self._vacancies
        return context

    @property
    def _vacancies(self):
        return Vacancy.objects.all()


class VacanciesBySpecialization(TemplateView):
    template_name = "vacancies.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies"] = self._get_vacancies(kwargs["spec"])
        return context

    @staticmethod
    def _get_vacancies(specialization):
        return Vacancy.objects.filter(specialty__code=specialization)


class VacancyView(TemplateView):
    template_name = "vacancy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancy"] = self._get_vacancy(kwargs["id"])
        return context

    @staticmethod
    def _get_vacancy(id):
        return get_object_or_404(Vacancy, id=id)


class CompanyView(TemplateView):
    template_name = "company.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["company"] = self._get_company(kwargs["id"])
        context["vacancies"] = self._get_vacancies(context["company"])
        return context

    @staticmethod
    def _get_company(id):
        return get_object_or_404(Company, id=id)

    @staticmethod
    def _get_vacancies(company):
        return Vacancy.objects.filter(company=company)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Не верный запрос к серверу =(')


def custom_handler500(request):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')
