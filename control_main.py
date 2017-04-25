class Person:
    def __init__(self, f_name, l_name, id):
        self.f = f_name
        self.l = l_name
        self.id = id

class Student(Person):
    def __init__(self, f_name, l_name, id, c_list = [], c_marks = []):
        Person.__init__(self, f_name, l_name, id)
        if c_list is None:
            c_list = []
        self.c_list = c_list
        self.c_marks = c_marks
    def enroll_course(self, user, course):
        if isinstance(user, Student) and course.run == 'true':
            user.c_list.append(self, course.title)
            course.s_list.append(self, user.id)
    def get_cources(self):
        return self.c_list
    def get_marks(self):
        return self.c_marks


class Teacher(Person):
    def __init__(self, f_name, l_name, id, c_list = []):
        Person.__init__(self, f_name, l_name, id)
        self.c_list = c_list
    def enroll_course(self, user, course):
        if isinstance(user, Teacher):
            user.c_list.append(self, course.title)
            course.t_list.append(self, user.id)
    def get_cources(self):
        return self.cources

class TA(Teacher, Student):
    def __init__(self, f_name, l_name, id, c_list = [], c_marks = []):
        Student.__init__(self, f_name, l_name, id, c_list, c_marks)
        def enroll_course(self, user, course):
            if isinstance(user, TA):
                user.c_list.append(self, course.title)
                course.t_list.append(self, user.id)
        def get_cources(self):
            return self.c_list
        def get_marks(self):
            return self.c_marks

class Course:
    def __init__(self, title, desc, run='false', t_list = [], s_list = [], ta_list = []):
        self.title = title
        self.desc = desc
        self.run = run
        self.t_list = t_list
        self.s_list = s_list
        self.ta_list = ta_list
    def get_list(self, type):
        if type=='students':
            return self.s_list
        elif type=='teachers':
            return self.t_list
        elif type=='tas':
            return self.ta_list
    def course_start(self):
        self.run = 'true'
