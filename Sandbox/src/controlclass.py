class controlclass:
    """Control class for form data"""

    def __init__(self, section, cycle, process, control,
                 tester, reviewer, status, effect, date, category):
        self.section = section
        self.cycle = cycle
        self.process = process
        self.control = control
        self.tester = tester
        self.reviewer = reviewer
        self.status = status
        self.effect = effect
        self.date = date
        self.category = category

    @property
    def section(self):
        return '{}'.format(self.section)

    @property
    def cycle(self):
        return '{}'.format(self.cycle)

    @property
    def process(self):
        return '{}'.format(self.process)

    @property
    def tester(self):
        return '{}'.format(self.tester)

    @property
    def reviewer(self):
        return '{}'.format(self.reviewer)

    @property
    def effect(self):
        return '{}'.format(self.effect)

    @property
    def date(self):
        return '{}'.format(self.date)

    @property
    def category(self):
        return '{}'.format(self.category)

    def __repr__(self):
        return "Control('{}', '{}', {}, '{}', {}, '{}', {}, '{}', {} ,{})" \
            .format(self.section, self.cycle, self.process, self.control, self.tester
                    , self.reviewer, self.status, self.effect, self.date, self.category)
