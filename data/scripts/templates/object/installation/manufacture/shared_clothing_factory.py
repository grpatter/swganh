#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/installation/manufacture/shared_clothing_factory.iff"
	is_prototype = False
	
	def create(self, kernel, params):
		result = Installation()
	
		result.template = "object/installation/manufacture/shared_clothing_factory.iff"
		result.attribute_template_id = -1
		result.stfName("installation_n","clothing_factory")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())