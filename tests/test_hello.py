from pytest_bdd import scenario, given, then


@scenario("hello.feature", "Assert Hello World")
def test_hello():
    pass


@given("I have a message", target_fixture="message")
def message():
    return "Hello World"


@then("Should return Hello World")
def message_should_be_hello_world(message):
    assert message == 'Hello World'
