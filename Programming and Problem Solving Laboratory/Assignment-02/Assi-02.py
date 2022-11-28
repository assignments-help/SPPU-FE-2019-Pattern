# Problem Statement:
# To accept an object mass in kilograms and velocity in meters per second and display its
# momentum. Momentum is calculated as e=mc2 where m is the mass of the object and c is
# its velocity.


mass = int(input('Enter mass of object (in Kg): '))
velocity = int(input('Enter velocity of object (in m/s): '))

momentum = mass * velocity * velocity

print('Momentum of object:', momentum)