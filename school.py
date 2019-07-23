#!/usr/bin/env python
# coding: utf-8

# In[1]:


class School():
    def __init__(self, name, roster = {}):
        self.name = name
        self.roster = roster

    def add_student(self, name, grade):
        if grade in self.roster:
            self.roster[grade].append(name)
        else:
            self.roster[grade] = [name]

    def grade(self, grade):
        return self.roster[grade]

    def sort_roster(self):
        sorted_roster = sorted(self.roster.items(), key = lambda x: x[1])
        print(sorted_roster)