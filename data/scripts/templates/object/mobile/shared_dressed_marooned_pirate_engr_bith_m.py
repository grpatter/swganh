#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/mobile/shared_dressed_marooned_pirate_engr_bith_m.iff"
	is_prototype = False
	
	def create(self, params):
		result = Creature()
	
		result.template = "object/mobile/shared_dressed_marooned_pirate_engr_bith_m.iff"
		result.attribute_template_id = 9
		result.stfName("npc_name","bith_base_male")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())