from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from pornstar import Pornstar
from robber import Robber
from lunch import Food


def init_school():
    # create school
    codecool_bp = CodecoolClass.generate_local()
    input()
    # create mentors
    mentor_tomi = codecool_bp.find_mentor_by_full_name("Tamás Tompa")
    mentor_miki = codecool_bp.find_mentor_by_full_name("Miklós Beöthy")
    mentor_dani = codecool_bp.find_mentor_by_full_name("Dániel Salamon")
    mentors = [mentor_miki, mentor_tomi, mentor_dani]
    # creates list of 3 random students
    students = []
    for i in range(3):
        students.append(codecool_bp.find_student_by_full_name(codecool_bp.get_random_student()))
    while students[0].energy_level == students[1].energy_level:     # to have students with different energy levels
        students[1] = codecool_bp.find_student_by_full_name(codecool_bp.get_random_student())
    return [students, mentors]


def door_ringing(opener, ringer):
    opener.open_ringing_door(ringer)


def lunchbreak(school):
    print("It's lunchbreak time! Finally...")
    steak = Food("bloody beef steak", False, True)
    school[1][1].eat(steak)
    input()
    chichken = Food("chicken @csirkés", False, False)
    school[0][2].eat(chichken)


def main():
    school = init_school()
    input()
    school[1][2].morning_routine(school[0][0])
    input()
    school[1][2].morning_routine(school[0][1])
    input()
    pornstar = Pornstar("Crystal Ray", "One big black Dildo")
    opener = school[1][0]
    door_ringing(opener, pornstar)
    input()
    lunchbreak(school)
    input()
    pornstar = Pornstar("Riley Reid", "a Whip")
    door_ringing(opener, pornstar)
    input()
    robber = Robber("Viszkis", "Robbermask", "Bottle")
    opener = school[1][1]
    door_ringing(opener, robber)
    input()
    school[0][0].ending_routine(school[1][2])

main()
