class Course:
    def __init__(self, details):
        self.title  = (details[0]).rstrip()
        self.crn    = (details[1])[1:-1]
        self.course = (details[2])[1:-1]

        self.type = details[3].rstrip()
        self.time = details[4] #2 arguments, (start, end) tuple
        self.time_m = self.convert_time(self.time)
        self.days = details[5]

        if details[6] != "(TBA)":
            self.location = details[6].split(',')
            self.room = self.location[1].split()[-1]
            self.campus = self.location[0]
        else:
            self.location = self.room = self.campus = "(TBA)"

        self.qlength = details[7] #quarter length
        self.detail  = details[8] #added details
        self.professor = details[9].split()

    def convert_time(self, time):
        if time == 'TBA':
            start = end = -1
        else:
            separate = time.split(' ')
            start = self.to_mins(separate[0])
            if separate[1] == 'pm':
                start += 720
            end = self.to_mins(separate[3])
            if separate[4] == 'pm':
                end += 720
        return (start, end)

    def to_mins(self, time):
        mins = time.split(':')
        if mins[0] == '12':
            mins[0] = 0
        return int(mins[0])*60 + int(mins[1])

    def print_all(self):
        print 'title: %r' % self.title
        print 'crn: %r' % self.crn
        print 'course: %r' % self.course
        print 'type: %r' % self.type
        print 'time: %r' % self.time
        print 'hrs: %r, %r' % (self.time_m[0]/60., self.time_m[1]/60.)
        print 'days: %r' % self.days
        print 'location: %r' % self.location
        print 'qlength: %r' % self.qlength
        print 'detail: %r' % self.detail
        print 'professor: %r' % self.professor
        print ""
