#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/hopper/manufacturing_facility_hopper/shared_manufacture_installation_ingredient_hopper_structure_medium.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/hopper/manufacturing_facility_hopper/shared_manufacture_installation_ingredient_hopper_structure_medium.iff"
		result.attribute_template_id = -1
		result.stfName("crafting","hopper_structure_medium")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())