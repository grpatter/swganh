#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/resource_container/shared_resource_container_inorganic_water.iff"
	is_prototype = False
	
	def create(self, params):
		result = ResourceContainer()
	
		result.template = "object/resource_container/shared_resource_container_inorganic_water.iff"
		result.attribute_template_id = -1
		result.stfName("resource_container_n","inorganic_water_small")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())