#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/mobile/shared_carrion_spat_hue.iff"
	is_prototype = False
	
	def create(self, params):
		result = Creature()
	
		result.template = "object/mobile/shared_carrion_spat_hue.iff"
		result.attribute_template_id = 9
		result.stfName("monster_name","carrion_spat")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())