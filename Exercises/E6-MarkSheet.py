''' This marksheet based on 5 subjects if you want to add
more so, you can easily add more by this method '''

#taking input of all subjects from user
physics = float(input('Enter the marks of Physics: '))
maths = float(input('Enter the marks of Maths: '))
english = float(input('Enter the marks of English: '))
urdu = float(input('Enter the marks of Urdu: '))
chemistry = float(input('Enter the marks of Chemistry: '))

#this condition is for making our output more efficient
if((physics < 0 and physics >100) or (maths < 0 and maths >100) or (urdu < 0 and urdu >100) or (english < 0 and english >100) or (chemistry < 0 and chemistry > 100)):
    print('Invalid input')
else:
    obtainedMarks = physics + maths + english + urdu + chemistry
    percentage = (obtainedMarks * 100) / 500
    print('Marks obtained = ' + str(obtainedMarks) + '/500','percentage = ' + str(percentage) + '%',sep='\n')
