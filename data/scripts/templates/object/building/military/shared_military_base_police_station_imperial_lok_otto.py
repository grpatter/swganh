#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/military/shared_military_base_police_station_imperial_lok_otto.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/military/shared_military_base_police_station_imperial_lok_otto.iff"
		result.attribute_template_id = -1
		result.stfName("building_name","military_base_police_station_imperial_otto")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())