#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/medicine/shared_medpack_dizzy.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/medicine/shared_medpack_dizzy.iff"
		result.attribute_template_id = 7
		result.stfName("medicine_name","medic_dizzy")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())