#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/general/shared_starport_general_style_2.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/general/shared_starport_general_style_2.iff"
		result.attribute_template_id = -1
		result.stfName("starport_general_style_2","building_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())