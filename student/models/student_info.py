from odoo import models, fields, api


class StudentInfo(models.Model):
    _name = 'student.student_info'
    _description = 'student info'

    name = fields.Char(string="Name")
    age = fields.Char(string="Age")
    class_name = fields.Char(string="Class")
