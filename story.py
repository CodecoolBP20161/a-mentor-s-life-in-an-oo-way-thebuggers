from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from pornstar import Pornstar

codecool_bp = CodecoolClass.generate_local()
print("Mentors are initialized from CSV")
print("Students are initialized from CSV")
print("School @ {0}, in year {1} is created, with {2} mentors and 58 students".format(codecool_bp.location, codecool_bp.year, len(codecool_bp.mentors)))
mentor_tomi = codecool_bp.find_mentor_by_full_name("Tamás Tompa")
print("{0} {1} was found between the mentors with {2} energy".format(mentor_tomi.first_name, mentor_tomi.last_name, mentor_tomi.energy_level))
mentor_miki = codecool_bp.find_mentor_by_full_name("Miklós Beöthy")
print("{0} {1} was found between the mentors with {2} energy".format(mentor_miki.first_name, mentor_miki.last_name, mentor_miki.energy_level))
mentor_dani = codecool_bp.find_mentor_by_full_name("Dániel Salamon")
print("{0} {1} was found between the mentors with {2} energy".format(mentor_dani.first_name, mentor_dani.last_name, mentor_dani.energy_level))
student_franka = codecool_bp.find_student_by_full_name("Franka Böröcfi")
student_gyuri = codecool_bp.find_student_by_full_name("György Marha")
student_owen = codecool_bp.find_student_by_full_name("Ou Wee")
student_dani = codecool_bp.find_student_by_full_name("Dániel Kincses")
student_miki = codecool_bp.find_student_by_full_name("Who What")
print("Student {0} energy level is high in the morning".format(student_franka.first_name))
mentor_dani.morning_routine(student_franka)
print("Student {0} energy level is low in the morning".format(student_gyuri.first_name))
mentor_miki.morning_routine(student_gyuri)
print("Someone ring the doorbell")
pornstar = Pornstar("Crystal Ray", "One big black Dildo")
mentor_miki.open_ringing_door(pornstar)
