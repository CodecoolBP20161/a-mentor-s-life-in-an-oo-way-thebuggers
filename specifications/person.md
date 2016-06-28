# Person

## Description
Parent class for different types of people.

## Parent class
None.

## Attributes

* ```first_name```
 * data type: string
 * stores the first name of a person
* ```last_name```
 * data type: string
 * stores the last name of a person
* ```year_of_birth```
 * data type: integer
 * stores the birth year of a person
* ```gender```
 * data type: string
 * stores the gender of a person (male/female/notsure)
* ```energy_level```
 * data type: integer
 * stores the energy level of a person (1, 2 or 3)
* ```vegan```
 * data type: boolean
 * True if the person is a vegan, False if not

## Instance methods

### ```__init__```
The constructor.
#### Arguments
All the arguments of the class.
#### Return value
None

### ```eat```
Decides if the person eats the provided food or not, and modifies his/her energy level accordingly, then prints out the result.
#### Arguments
A Food object.
#### Return value
None
