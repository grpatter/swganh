#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/mobile/shared_warren_janna_bel_arde.iff"
	is_prototype = False
	
	def create(self, kernel, params):
		result = Creature()
	
		result.template = "object/mobile/shared_warren_janna_bel_arde.iff"
		result.attribute_template_id = 9
		result.stfName("npc_name","warren_janna_bel_arde")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())