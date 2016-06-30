from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from pornstar import Pornstar
from lunch import Food


def print_find_mentor(someone):
    print("{0} {1} was found between the mentors with {2} energy".format(
        someone.first_name, someone.last_name, someone.energy_level))


def init_school():
    # create school
    codecool_bp = CodecoolClass.generate_local()
    print("School @ {0}, in year {1} is created, with {2} mentors and 58 students".format(
        codecool_bp.location, codecool_bp.year, len(codecool_bp.mentors)))
    # create mentors
    mentor_tomi = codecool_bp.find_mentor_by_full_name("Tamás Tompa")
    print_find_mentor(mentor_tomi)
    mentor_miki = codecool_bp.find_mentor_by_full_name("Miklós Beöthy")
    print_find_mentor(mentor_miki)
    mentor_dani = codecool_bp.find_mentor_by_full_name("Dániel Salamon")
    print_find_mentor(mentor_dani)
    teachers = [mentor_miki, mentor_tomi, mentor_dani]
    # create list of 5 students
    students = []
    for i in range(5):
        students.append(codecool_bp.get_random_student())
    return [students, teachers]


def morning_routine(school):
    print("Student {0} energy level is high in the morning".format(school[0][0]))
    school[1][2].morning_routine(school[0][0])
    print("Student {0} energy level is low in the morning".format(school[0][1]))
    school[1][0].morning_routine(school[0][1])


def door_ringing(opener, ringer):
    opener.open_ringing_door(ringer)


def lunchbreak(school):
    steak = Food("chicken steak", False, True)
    school[1][1].eat(steak)
    chichken = Food("chichken @csirkés", False, False)
    school[0][2].eat(chichken)


def main():
    school = init_school()
    init_school()
    morning_routine(school)
    pornstar = Pornstar("Crystal Ray", "One big black Dildo")
    opener = school[1][0]
    door_ringing(opener, pornstar)
    lunchbreak(school)
    robber = Robber("Viszkis", "Robbermask", "Bottle")
    opener = school[1][1]
    door_ringing(opener, robber)



main()
