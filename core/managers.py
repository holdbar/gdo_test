# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class AnswerManager(models.Manager):
    """
    Answer model manager.
    """

    def get_answers_dict(self):
        answers_queryset = self.all()
        basic_answers_dict = { answer.question_name: answer.value for answer in answers_queryset.exclude(question_name="child_name") }
        child_name_answers_dict = { str(answer.index): answer.value for answer in answers_queryset.filter(question_name="child_name") }
        basic_answers_dict["children"] = child_name_answers_dict

        return basic_answers_dict

