from behave import given, when, then
from fabric import AnimalFactory

@given('an animal factory')
def step_given_factory(context):
    context.factory = AnimalFactory()

@when('I create a dog')
def step_create_dog(context):
    context.animal = context.factory.create_animal("dog")

@when('I create a cat')
def step_create_cat(context):
    context.animal = context.factory.create_animal("cat")

@then('the sound should be "{sound}"')
def step_check_sound(context, sound):
    assert context.animal.sound() == sound
