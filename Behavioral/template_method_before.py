# Template Method Pattern

class Builder():
    def __init__(self, device: str) -> None:
        self._device = device

    def build(self):
        self.test()
        self.lint()
        self.assemble()
        self.deploy()

    def test(self):
        if self._device == 'android':
            print('Running android tests')
        else:
            print('Running ios tests')

    def lint(self):
        if self._device == 'android':
            print('Linting the android code')
        else:
            print('Linting the ios code')

    def assemble(self):
        if self._device == 'android':
            print('Assembling the android build')
        else:
            print('Assembling the ios build')

    def deploy(self):
        if self._device == 'android':
            print('Deploying android build to server')
        else:
            print('Deploying ios build to server')


androidBuilder = Builder('android')
androidBuilder.build()

# Output:
# Running android tests
# Linting the android code
# Assembling the android build
# Deploying android build to server

iosBuilder = Builder('ios')
iosBuilder.build()

# Output:
# Running ios tests
# Linting the ios code
# Assembling the ios build
# Deploying ios build to server
