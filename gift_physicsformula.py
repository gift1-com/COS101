print('welcome please choose your desired formula')
print('a- force\nb-electrical power\nc-velocity\nd-voltage\ne-potential energy')
k = input('what is your desired formula')
if k == 'a':
            print('you have chosen force')
            mass=float(input('what is your desired mass?'))
            acceleration = float(input('what is your desired acceleration?'))
            print(mass * acceleration)
if k == 'b':
          print('you have chosen electrical power')
          voltage = float(input('what is your desired voltage?'))
          current = float(input('what is your desired current?'))
          print(voltage * current)

if k=='c':
           print('you have chosen velocity')
           displacement = float(input('what is your desired displacement?'))
           time = float(input('what is your desired time?'))
           print(displacement / time)

if k == 'd':
           print('you have chosen voltage')
           current = float(input('what is your desired current?'))
           resistance = float(input('what is your desired resistance?'))
           print(resistance * current)

if k == 'e':
            print('you have chosen potential energy')
            mass = float(input('what is your desired mass?'))
            acc_due_to_gravity = float(input('what is your desired gravity?'))
            height = float(input('what is your desired height?'))
            print(mass * acc_due_to_gravity * height)

else:
            print('please click among the available formulae')