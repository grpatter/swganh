#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/factory/shared_factory_crate_generic_items.iff"
	is_prototype = False
	
	def create(self, params):
		result = FactoryCrate()
	
		result.template = "object/factory/shared_factory_crate_generic_items.iff"
		result.attribute_template_id = 4
		result.stfName("factory_n","generic_items_crate")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())