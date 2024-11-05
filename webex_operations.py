import requests
import json

"""
This script in its totality walks through basic Webex Teams API operations. This will need to 
be modularized and remove elements common to each operation (e.g. token, headers). -MG, 11.4.24
"""

# token obtained from https://developer.webex.com/docs/getting-your-personal-access-token
token = 'YTQ4ZjY2OGEtOGYxZC00NjdmLWJkY2ItNmY0MzkzZmI4ZDUxNzk5ZTk4NzEtMTg3_P0A1_024cf1cc-0fff-4459-9d22-2bf3b7018d17'

################ Create Webex Team ##################

# note: the 3 variables/fields below are necessary to acquire & save team ID values for 
# subsequent operations.
url = 'https://api.ciscospark.com/v1/teams'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'  }

body = {
    'name': 'Team Testing'   }

# uncomment next line for new team creation
# opus = requests.post(url, headers=headers, data=json.dumps(body)).json()
get_response = requests.get(url, headers=headers).json()

# teamId = get_response['items'][0]['id']  
# print(teamId)

# obtain your active team IDs! <3 
teams = get_response['items']
for team in teams:
    if team['name'] == 'Team Personal':
        teamPersonalId = team['id']
    elif team['name'] == 'Team School':
        teamSchoolId = team['id']
    elif team['name'] == 'Team Testing':
        teamTestId = team['id']

# uncomment to see if team-ID variables are being pulled correctly
# print(f'Team Personal ID: {teamPersonalId}')
# print(f'Team School ID: {teamSchoolId}')
# print(f'Team Testing ID: {teamTestId}')

########## DELETE A TEAM #############

# remove_team_endpoint = f'https://api.ciscospark.com/v1/teams/{teamTestId}'
# opus = requests.delete(remove_team_endpoint, headers=headers)
# print(f'output: {opus}')  # successful response is 204; "successful request without body"

########## CREATE A ROOM #############
"""
The script below creates a new room and acquires a "room ID" needed for operations within a room.
"""
room_endpoint = 'https://api.ciscospark.com/v1/rooms'
room_name = 'School_DevNet room'
room_body = {
    'title' : room_name,
    'teamId' : teamSchoolId     }

# uncomment next line for new room creation
# post_newRoom = requests.post(room_endpoint, headers=headers, data=json.dumps(room_body)).json()
room_response = requests.get(room_endpoint, headers=headers).json()

room_id = room_response['items']
for room in room_id:
    if room['title'] == room_name:
        roomId = room['id']

# uncomment next line to confirm roomId variable exists
# print(roomId)

########## DELETE A ROOM #############

remove_room_endpoint = f'https://api.ciscospark.com/v1/rooms/{roomId}'
opus = requests.delete(remove_room_endpoint, headers=headers)
print(f'output: {opus}')  # successful response is 204; "successful request without body"