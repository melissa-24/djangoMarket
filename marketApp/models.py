from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['firstName']) < 2:
            errors['firstName'] = 'First Name must be at least 2 characters'
        if len(form['lastName']) < 2:
            errors['lastName'] = 'Last Name must be at least 2 characters'
        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] = 'Username already in use'
        if len(form['password']) < 6:
            errors['password'] = 'Password must be at least 6 characters'

        return errors
    
    def authenticate(self, username, password):
        users = self.filter(username=username)
        if not users:
            return False
        
        user = users[0]
        return bcrypt.checkpw(password.encode(). user.password.encode())

    def register(self, form):
        pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            firstName = form['firstName'],
            lastName = form['lastName'],
            username = form['username'],
            password = pw,
        )

class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    username = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)

    objects = UserManager()