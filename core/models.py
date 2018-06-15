# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from core.managers import AnswerManager

class Answer(models.Model):
    """
    Answer model.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="answers", blank=True, null=True)
    question_name = models.CharField(max_length=255)
    value = models.TextField()
    index = models.PositiveIntegerField(default=0)

    objects = AnswerManager()

    class Meta:

        app_label = "core"
        verbose_name = "answer"
        verbose_name_plural = "answers"

    def __unicode__(self):

        return "{question_name}: {value}".format(**{
            "question_name": self.question_name,
            "value": self.value,
        })

    def __str__(self):

        return self.__unicode__()

