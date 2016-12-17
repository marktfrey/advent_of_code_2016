import d1
 
path = input('Enter the problem input: ')
final = d1.ending_distance_from_origin(path)
revis = d1.first_revisited_distance_from_origin(path)
print('ANSWER: \n my final distance is %(final)d from origin.\n My first revisited position was %(revis)s' % locals())
