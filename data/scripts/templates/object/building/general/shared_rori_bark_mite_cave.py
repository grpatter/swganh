#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/general/shared_rori_bark_mite_cave.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/general/shared_rori_bark_mite_cave.iff"
		result.attribute_template_id = -1
		result.stfName("cave","building_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())