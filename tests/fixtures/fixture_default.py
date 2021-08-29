from tests.fixtures.fixture_user import FixtureUser

class FixtureDefault():

    def clear():
        FixtureUser.clear()

    def run():
        FixtureUser.run()