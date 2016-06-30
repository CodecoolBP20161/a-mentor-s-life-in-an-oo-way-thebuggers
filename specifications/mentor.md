
# Mentor

## Description
This class represents a Mentor.

## Parent class
Person

## Attributes

* ```nikcname```
  * data type: string
  * description: stores the mentors nickname

## Class methods

### ```create_by_csv```
Make a list form csv file

#### Arguments
* ```csv_file```
  * data_type: csv_file
  * description: csv file which stores all the Mentor data

#### Return value
Return back a list of Mentors

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself and arguments form parent class

#### Return value
None

### ```morning_routine```
A Method which check the argument student energy level
and the mentor do specific reactions

#### Arguments
A student object with low or high energy level

#### Return value
None

### ```open_ringing_door```
A mentor opens a ringing door, and do specific reactions based on the ringer person.

#### Arguments
A person based object

#### Return value
None
