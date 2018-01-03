# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s my.content -t test_folklore.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src my.content.testing.MY_CONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_folklore.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Folklore
  Given a logged-in site administrator
    and an add folklore form
   When I type 'My Folklore' into the title field
    and I submit the form
   Then a folklore with the title 'My Folklore' has been created

Scenario: As a site administrator I can view a Folklore
  Given a logged-in site administrator
    and a folklore 'My Folklore'
   When I go to the folklore view
   Then I can see the folklore title 'My Folklore'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add folklore form
  Go To  ${PLONE_URL}/++add++Folklore

a folklore 'My Folklore'
  Create content  type=Folklore  id=my-folklore  title=My Folklore


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the folklore view
  Go To  ${PLONE_URL}/my-folklore
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a folklore with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the folklore title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
