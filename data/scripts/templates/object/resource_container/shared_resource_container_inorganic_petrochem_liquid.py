#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/resource_container/shared_resource_container_inorganic_petrochem_liquid.iff"
	is_prototype = False
	
	def create(self, params):
		result = ResourceContainer()
	
		result.template = "object/resource_container/shared_resource_container_inorganic_petrochem_liquid.iff"
		result.attribute_template_id = -1
		result.stfName("resource_container_n","organic_food_small")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())