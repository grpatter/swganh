#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/base/shared_base_capitol.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/base/shared_base_capitol.iff"
		result.attribute_template_id = -1
		result.stfName("base_palace","building_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())