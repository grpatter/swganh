#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/factory/shared_factory_crate_installation.iff"
	is_prototype = False
	
	def create(self, params):
		result = FactoryCrate()
	
		result.template = "object/factory/shared_factory_crate_installation.iff"
		result.attribute_template_id = 4
		result.stfName("installation_crate","factory_n")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())