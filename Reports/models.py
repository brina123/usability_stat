from django.db import models
from django.contrib import admin

class Tester (models.Model):
    name_testerja = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name_testerja


class Testiranec (models.Model):
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    MATURITY_MODEL = (
        (1, 'Use it every day'),
        (2, 'Sometimes use it'),
        (3, 'Use it only at work'),
    )
    name_testiranca = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    age = models.IntegerField(blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True)
    digital_maturity_level = models.PositiveIntegerField(choices=MATURITY_MODEL)

    def __unicode__(self):
        return unicode(self.name_testiranca)


class Product (models.Model):
    product_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.product_name

class Product_part (models.Model):
    product_part_name = models.CharField(max_length=200)
    part_of_project = models.ForeignKey(Product)

    def __unicode__(self):
        return '%s %s' % (self.product_part_name, self.part_of_project)


class Test (models.Model):
    test_testiranec = models.ForeignKey(Testiranec)
    test_tester = models.ForeignKey(Tester)
    test_product = models.ForeignKey(Product)
    test_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.test_testiranec)

class Task (models.Model):
    task_product = models.ForeignKey(Product, null=True, blank=True)
    task_product_part = models.ForeignKey(Product_part, null=True, blank=True)
    task_description = models.TextField()

    def __unicode__(self):
        return self.task_description


class Tag (models.Model):
    tag_description = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.tag_description)


class Grade (models.Model):
    GRADE_CHOICES = (
        (1, 'Easy with no help'),
        (2, 'With a little help'),
        (3, 'With a lot help'),
        (4, 'Did not finnish'),
    )

    grade_task = models.ForeignKey(Task)
    grade_testiranec = models.ForeignKey(Testiranec)
    grade_explained = models.PositiveSmallIntegerField(choices=GRADE_CHOICES, blank=True, null=True)
    grade_description = models.TextField(blank=True, null=True)
    grade_tag = models.ManyToManyField(Tag, blank=True)

    def __unicode__(self):
        return '%s %s' % (unicode(self.grade_task), unicode(self.grade_testiranec))


