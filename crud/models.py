from django.db import models

# Create your models here.

# User Model
class User(models.Model):

    first_name = models.CharField(null = 'False', max_length=50, default = 'Leonard')
    last_name = models.CharField(null = 'False', max_length=50, default = 'Noumba')
    date_of_birth = models.DateField(null = 'False',)

    #toString method for object string representation
    def __str__(self):
        return self.first_name + ' ' + self.last_name

# Instructor Model
class Instructor(User):

    full_time = models.BooleanField(default = True)
    total_learners = models.IntegerField()

    def __str__(self):
        return "First Name: " + self.first_name + "," + \
                "Last Name: " + self.last_name + "," + \
                "Is Full Time: " + str(self.full_time) + "," + \
                "Total Learners: " + str(self.total_learners) + ","

# Learner model
class Learner(User):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    # Occupation Char field with defined enumeration choices
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT
    )
    # Social link URL field
    social_link = models.URLField(max_length=200)
    
    # Create a toString method for object string representation
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
                "Last name: " + self.last_name + ", " \
                "Date of Birth: " + str(self.dob) + ", " + \
                "Occupation: " + self.occupation + ", " + \
                "Social Link: " + self.social_link

# Enrollment model as a lookup table with additional enrollment info
class Enrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODES = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor'),
    ]
    # Add a learner foreign key
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    # Add a course foreign key
    course = models.ForeignKey("crud.Course", on_delete=models.CASCADE)
    # Enrollment date
    date_enrolled = models.DateField(auto_now = True)
    # Enrollment mode
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)

# Course Model
class Course(models.Model):

    name = models.CharField(null = False, max_length=50, default = "online couse")	
    description = models.CharField(max_length=500)
    
    #many_to_many relationship with Learner via enrollment relationship
    learners = models.ManyToManyField(Learner, through = Enrollment)
    
    #many_to_many relationship with Instructor
    instructors = models.ManyToManyField(Instructor)

    def __str__(self):
        return "Name: " + self.name + "," + \
                "Description: " + self.description

# Lesson Model
class Lesson(models.Model):
    title = models.CharField(max_length=100, default="title")
    course = models.ForeignKey(Course, null = True, on_delete=models.CASCADE)
    content = models.TextField()

