from models import *

# Course has instructors reference field so can be used directly via forward access
courses = Course.objects.filter(instructors__first_name='Yan')
print("1. Get courses taught by Instructor `Yan`, forward")
print(courses)

print("\n")
# For each instructor, Django creates a implicit course_set. This is caleld backward access
instructor_yan = Instructor.objects.get(first_name='Yan')
print("1. Get courses taught by Instructor `Yan`, backward")
print(instructor_yan.course_set.all())

print("\n")
instructors = Instructor.objects.filter(course__name__contains='Cloud')
print("2. Get the instructors of Cloud app dev course")
print(instructors)

print("\n")
courses = Course.objects.filter(instructors__first_name='Yan')
occupation_list = set()
for course in courses:
    for learner in course.learners.all():
        occupation_list.add(learner.occupation)
print("3. Check the occupations of the courses taught by instructor Yan'")
print(occupation_list)


learner_david = Learner.objects.get(first_name="David")
print("1. Get the user information about learner `David`")
print(learner_david.user_ptr)
user_david = User.objects.get(first_name="David")
print("2. Get learner `David` information from user")
print(user_david.learner)

course = Course.objects.get(name='Introduction to Python')
learners = course.learners.all()
print("3. Get all learners for `Introduction to Python` course")
print(learners)

courses = Course.objects.filter(instructors__first_name='Yan')
occupation_list = set()
for course in courses:
    for learner in course.learners.all():
        occupation_list.add(learner.occupation)
print("4. Check the occupation list for the courses taught by instructor `Yan`")
print(occupation_list)

enrollments = Enrollment.objects.filter(date_enrolled__month=8,
                                            date_enrolled__year=2020,
                                            learner__occupation='developer')
courses_for_developers = set()
for enrollment in enrollments:
    course = enrollment.course
    courses_for_developers.add(course.name)
print("5. Check which courses developers are enrolled in Aug, 2020")    
print(courses_for_developers)