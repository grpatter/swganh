#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/poi/shared_dathomir_nightsisterpatrol_large2.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/poi/shared_dathomir_nightsisterpatrol_large2.iff"
		result.attribute_template_id = -1
		result.stfName("base_poi_building","poi_n")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())