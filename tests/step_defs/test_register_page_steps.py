from pytest_bdd import scenarios, when, then, given, parsers

#Scenarios
scenarios('..tests/features/test_register_page.feature')

#Steps
    @Given('open the register page')
    def open_page(browser):
        register_page = RegisterPage(browser)
        register_page.load_page()

    @when(parsers.cfparse('the user type email "{email}"'))
    def type_email(browser, email):
        register_page = RegisterPage_(browser)
        register_page.type_firstname(browser, firstname)

    when(parsers.cfparse('the user type name "{name}"'))
    def type_email(browser, email):
        print()

    when(parsers.cfparse('the user type password "{password}"'))
    def type_email(browser, email):
        print()

    when('the user Click Create Account button')
    def type_email(broweser):
        print()

    then('the account has been created successfully')
    def check_resgister_with_success(browser):
        print()