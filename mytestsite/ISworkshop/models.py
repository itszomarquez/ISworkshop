import datetime
from django.db import models
from model_utils import Choices
from django.conf import settings
from django.utils import timezone
# Create your models here.

class ProfilePage(models.Model):
    email = models.EmailField(
			verbose_name="email", max_length=60, unique=True)
    student_number = models.CharField(
			verbose_name="student number", max_length=9, unique=True)
    first_name = models.CharField(
			verbose_name="first name", max_length=60, blank=False)
    last_name = models.CharField(
			verbose_name="last name", max_length=60, blank=False)
    graduation_year = models.IntegerField(
			verbose_name="expected year of graduation", default=datetime.date.today().year)
    date_joined = models.DateTimeField(
			verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(
			verbose_name="last login", auto_now=True)
    DEGREES = Choices("Bachelor of Arts", "Bachelor of Laws", "Bachelor of Science", "Certificate", "Diploma", "Doctor of Enginerring", "Doctor of Science", "Doctor of Philosophy", "Juris Doctor",
                      "Master of Arts", "Master of Engineering", "Master of Science", "Professional Masters")
    degree = models.CharField(
			max_length=60, choices=DEGREES, default=DEGREES.Diploma)
    PROGRAMS = Choices('Anthropology', 'Applied Mathematics', 'Applied Mathematics/Actuarial Science', 'Applied Physics', 'Applied Psychology', 'Archaeology', 'Architecture',
                       'Art Education', 'Art History', 'Art Studies', 'Asian Studies', 'Biology', 'Broadcast Communication', 'Building Technology', 'Business Administration',
                       'Business Administration and Accountancy', 'Business Economics', 'Business Economics (UPEPP)', 'Business Management (UPEPP)', 'Chemical Engineering',
                       'Chemistry', 'Chemical Education', 'Civil Engineering', 'Clothing Technology', 'Community Development', 'Communication Research', 'Community Nutrition',
                       'Community Development', 'Comparative Literature', 'Communication', 'Computer Engineering', 'Computer Science', 'Creative and Musical Performing Arts',
                       'Creative Writing', 'Demography', 'Development Economics', 'Early Childhood Development', 'Economics', 'Education', 'Electrical Engineering',
                       'Electronics Engineering', 'Elementary Education', 'English Studies: Language', 'English Studies: Literature', 'Environmental Engineering',
                       'Environmental Science', 'European Languages', 'Exercise and Sports Science', 'Family Life and Child Development', 'Filipino', 'Film', 'Finance',
                       'Fine Arts', 'Food Science', 'Food Technology', 'Geomatics Engineering', 'Geodetic Engineering', 'Geography', 'Geology', 'Hispanic Literature', 'History',
                       'Home Economics', 'Hotel, Restaurant and Institutional Management', 'Human Movement Science', 'Industrial Design', 'Industrial Engineering',
                       'Industrial Relations', 'Interior Design', 'International Studies', 'Islamic Studies', 'Journalism', 'Juris Doctor', 'Landscape Architecture',
                       'Librarianship', 'Library and Information Studies', 'Linguistics', 'Malikhaing Pagsulat', 'Management', 'Marine Science', 'Materials Engineering',
                       'Mathematics', 'Mechanical Engineering', 'Media Studies', 'Metallurgical Engineering', 'Meteorology', 'Microbiology', 'Mining Engineering',
                       'Molecular Biology and Biotechnology', 'Music',  'Nutrition', 'Painting', 'Philippine Studies', 'Philosophy', 'Physical Education', 'Physics',
                       'Political Science', 'Population Studies', 'Psychology', 'Public Administration', 'Public Management', 'Regional Development Planning', 'Sculpture',
                       'Secondary Education', 'Social Development', 'Social Work', 'Sociology', 'Speech Communication', 'Sports Science', 'Sports Studies', 'Statistics',
                       'Technology Management', 'Theatre Arts', 'Tourism', 'Tropical Landscape Architecture', 'Urban and Regional Planning', 'Visual Communication',
                       'Voluntary Sector Management', 'Women and Development', 'Zoology')
    program = models.CharField(
			max_length=60, choices=PROGRAMS, default=PROGRAMS.Anthropology)
    profile_picture = models.ImageField(
			verbose_name="profile picture", default="default.jpg", upload_to="profile_pictures")
