#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/general/shared_cave_01_damprock.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/general/shared_cave_01_damprock.iff"
		result.attribute_template_id = -1
		result.stfName("Cave Style 02","building_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())