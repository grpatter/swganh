#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/poi/shared_tatooine_dim_u_large1.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/poi/shared_tatooine_dim_u_large1.iff"
		result.attribute_template_id = -1
		result.stfName("poi_n","base_poi_building")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())