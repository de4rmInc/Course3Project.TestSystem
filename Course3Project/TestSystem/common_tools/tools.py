class Test:
    def __init__(self, testName='', func = None, params = []):
        self.testName = testName
        self.func = func
        self.params = params
        self.answer = Answer(testName)

class Answer:
    def __init__(self, testName=''):
        self.testName = testName
        self.OK = 'Done'
        self.Fail = 'Failed'