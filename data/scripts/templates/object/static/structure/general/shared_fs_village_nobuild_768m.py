#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/static/structure/general/shared_fs_village_nobuild_768m.iff"
	is_prototype = False
	
	def create(self, params):
		result = Static()
	
		result.template = "object/static/structure/general/shared_fs_village_nobuild_768m.iff"
		result.attribute_template_id = -1
		result.stfName("obj_n","unknown_object")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())