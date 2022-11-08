"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array."""
    return np.min(data, axis=0)

def patient_normalise(data):
    """Normalise patient data from a 2D inflammation data array."""
    maxes = np.max(data, axis=0)
    return data / maxes[:, np.newaxis]


def standard_deviation(data):
    """Calculate the standard deviation of a 2D inflammation data array."""
    return np.std(data, axis=0)


# file: inflammation/models.py

class Observation:
    def __init__(self, day, value):
        self.day=day
        self.value=value

    def __str__(self):
        return str(self.value)

class Person:
    #anything that all people have in common defined here
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name: str):
        
        super().__init__(name) #super accesses the parent class that you've inherited from (Person)
        self.observations = []

    @property
    def last_observation(self):
        return self.observations[-1]

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)

        self.observations.append(new_observation)
        return new_observation

    def __str__(self):
        return self.name

class Doctor(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.patients=[]

    @property
    def add_patient(self):
        return [p.name for p in self.patients]

    def add_patient(self, new_patient):
        #check pateint is not already assigned to this doctor
        for patient in self.patients:
            if patient.name == new_patient.name:
                return
        self.patients.append(new_patient)



alice = Patient('Alice')

alice.add_observation(3)
alice.add_observation(4)

obs = alice.last_observation
print('last observation was: ', obs)

print(alice.observations)

