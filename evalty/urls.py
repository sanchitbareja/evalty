from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from classes.views import home, student, professor, student_evaluation_form, student_evaluation_select_team, student_evaluation_report, professor_evaluation_report

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^student/$', student, name='student'),
    url(r'^student/evaluate/form/$', student_evaluation_form, name='student_evaluation_form'),
    url(r'^student/evaluate/report/$', student_evaluation_report, name='student_evaluation_report'),
    url(r'^student/evaluate/select-team/$', student_evaluation_select_team, name='student_evaluation_select_team'),
    url(r'^professor/$', professor, name='professor'),
    url(r'^professor/evaluate/report/$', professor_evaluation_report, name='professor_evaluation_report'),
    url(r'^admin/', include(admin.site.urls)),
)