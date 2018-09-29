# -*- coding: UTF-8 -*-
#from __future__ import unicode_literals
from django.db import models
from DjangoUeditor.models import UEditorField

class Article(models.Model):
    title = models.CharField(u'标题', max_length=25)
    category = models.CharField(u"博客标签", max_length=50, blank=True)  # 博客标签
    jianshu = models.CharField(u"概要", max_length=200, blank=True)
    content = UEditorField(u"文章正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __unicode__(self):
        return self.title



