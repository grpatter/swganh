#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/ship/components/engine/shared_eng_mission_reward_imperial_cygnus_megadrive.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/ship/components/engine/shared_eng_mission_reward_imperial_cygnus_megadrive.iff"
		result.attribute_template_id = 8
		result.stfName("space/space_item","eng_mission_reward_imperial_cygnus_megadrive_n")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())