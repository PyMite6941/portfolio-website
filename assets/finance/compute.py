from pyscript import when,display

@when("click", "#run")
def handler():
    display("button clicked")