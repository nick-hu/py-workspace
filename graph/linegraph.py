print 'Welcome to Grapher 1.0!\n'

while True:
    print
    '''Please enter the information of your equation of the form y=mx+b.
    Note: Grapher will only plot points (x, y) if x AND y are integers.\n'''
    m = float(raw_input('Please enter m (slope): '))
    b = float(raw_input('Please enter b (y-intercept): '))

    yval = 10

    while yval > -11:
        xval = (yval-b) / m
        nleft, nright = int(10 + xval), int(-1 - xval)
        # Dashes left/right of the point if x is negative
        pleft, pright = int(xval - 1), int(10 - xval)
        # Dashes left/right of the point if x is positive

        if xval % 1 != 0:  # If xval is not an integer, don't plot
            if yval == 0:
                print 10*' = ', '|', 10*' = ', yval
            else:
                print 10*' - ', '|', 10*' - ', yval

        elif nright > 9 or pleft > 9:  # If point is off graph, don't ploy
            if yval == 0:
                print 10*' = ', '|', 10*' = ', yval
            else:
                print 10*' - ', '|', 10*' - ', yval

        elif yval == 0:  # Special plotting if point crosses x-axis
            if nleft == 10:
                print 10*' = ', 'o', 10*' = ', yval
            elif nleft < 10:
                print nleft*' = ', 'o', nright*' = ', '|', 10*' = ', yval
            else:
                print 10*' = ', '|', pleft*' = ', 'o', pright*' = ', yval

        elif nleft == 10:  # Special plotting if point crosses y-axis
            print 10*' - ', 'o', 10*' - ', yval

        elif nleft < 10:  # Plotting for a negative xval
            print nleft*' - ', 'o', nright*' - ', '|', 10*' - ', yval

        else:  # Plotting for a positive xval
            print 10*' - ', '|', pleft*' - ', 'o', pright*' - ', yval

        yval = yval - 1

    for x in range(-10, 11):  # x-scale markings
        if x < 1:
            print x,
        else:
            print '', x,

    print '\n\n-------------------------------------------'
    rep = raw_input('Another graph? Enter for yes or type q to quit: ')
    if rep == 'q':
        break
    else:
        print '\n-------------------------------------------'
        continue

print '\nGoodbye and thank you for choosing Grapher 1.0!'
