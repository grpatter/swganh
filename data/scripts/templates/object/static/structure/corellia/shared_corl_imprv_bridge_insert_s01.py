#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/static/structure/corellia/shared_corl_imprv_bridge_insert_s01.iff"
	is_prototype = False
	
	def create(self, params):
		result = Static()
	
		result.template = "object/static/structure/corellia/shared_corl_imprv_bridge_insert_s01.iff"
		result.attribute_template_id = -1
		result.stfName("obj_n","unknown_object")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())