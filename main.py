# drill 2
from pyscript import display

X = {'Yao', 'Garabiles', 'Cortez', 'Mendoza'}
Y = {'Garabiles', 'Cortez', 'Lopez', 'Santos'}

display(f'Club ART Members: {X}', target='output')
display(f'Club SCIENCE Members: {Y}', target='output')
display(f'Students with Club/s: {X | Y}', target='output') #ATLEAST ONE CLUB
display(f'Students with 2 Clubs: {X & Y}', target='output')  # intersection || BELONGS TO BOTH CLUBS
display(f'Students in ART Club: {X - Y}', target='output') # difference || STUDENTS IN CLUB X ONLY
display(f'Students in SCIENCE Club: {Y - X}', target='output')  # difference || STUDENTS IN CLUB Y ONLY
display(f'Students in 1 Club: {X ^ Y}', target='output')  # symmetric difference || STUDENTS IN ONLY ONE CLUB
