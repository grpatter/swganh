#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/corellia/shared_filler_building_corellia_style_06.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/corellia/shared_filler_building_corellia_style_06.iff"
		result.attribute_template_id = -1
		result.stfName("filler_building_corellia_style_6","building_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())