#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/naboo/shared_filler_building_naboo_style_10.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/naboo/shared_filler_building_naboo_style_10.iff"
		result.attribute_template_id = -1
		result.stfName("building_name","filler_building_naboo_style_10")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())