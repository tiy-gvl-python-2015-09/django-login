# Django Login

## Description

Create a Django project/app to create a user of different types

## Objectives

### Learning Objectives

After completing this assignment, you should be able to:

* Create a django app that implements user registration
* Understand user authentication
* Understand user profile types

## Details

### Deliverables

* A Git repo called django-login containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * a Django project

### Requirements

* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Create a Django project that implements the ability to create a user for themselves. This is commonly
kwown as user registration.  A user should be able to fill out a registration form to create an authenticated
user in the database.  They should be directed to their profile page where they can decide what type of user
they want to be.  The two options are `Student` and `Teacher`. Your app should remember their preference of
user type.

After they have decided the type of user they want to be - when they go to the `/` url of your app
they should be redirected to either a `/student` or a `/teacher` url where it should at minimum
say "Welcome <username> i'm glad you're a <user type>".

## Hard Mode

Enforce rules that keep a `student` user from being able to access the `/teacher` route but do not
restrict `teacher` users from accessing the `/student` route
