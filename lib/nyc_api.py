import requests
import json

class GetPrograms:
    def __init__(self, app_token):
        self.app_token = app_token

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        headers = {
            'X-App-Token': self.app_token
        }
        response = requests.get(URL, headers=headers)
        
        # Print response content for debugging
        print("Response content:", response.content)
        
        try:
            response_json = response.json()
            if isinstance(response_json, list):
                return response_json
            else:
                print("Unexpected response format:", response_json)
                return []
        except json.JSONDecodeError as e:
            print("JSON decoding error:", e)
            return []

    def program_agencies(self):
        programs_list = []
        programs = self.get_programs()
        
        if programs:
            print("First program:", programs[0])
        
        for program in programs:
            if isinstance(program, dict):
                agency_name = program.get("agency")
                if agency_name:
                    programs_list.append(agency_name)
        
        return programs_list

# Replace 'your_api_token_here' with your actual API token from NYC Open Data
api_token = 'your_api_token_here'
programs = GetPrograms(api_token)
agencies = programs.program_agencies()

# Print out unique agencies
for agency in set(agencies):
    print(agency)