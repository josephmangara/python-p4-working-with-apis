
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"

    response = requests.get(URL)
    return response.content
  
  def program_school(self):
    programs_list = []
    programs = json.loads(self.get_programs()) 
    for program in programs:
      programs_list.append(program["name"])
      
    return programs_list
    
programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)


    

# programs = GetPrograms().get_programs()
# print(programs)