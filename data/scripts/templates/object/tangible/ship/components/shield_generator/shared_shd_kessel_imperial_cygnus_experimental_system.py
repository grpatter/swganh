#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/ship/components/shield_generator/shared_shd_kessel_imperial_cygnus_experimental_system.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/ship/components/shield_generator/shared_shd_kessel_imperial_cygnus_experimental_system.iff"
		result.attribute_template_id = 8
		result.stfName("space/space_item","shd_kessel_imperial_cygnus_experimental_system_n")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())