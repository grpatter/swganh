#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/furniture/modern/shared_searchable_desk_02.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/furniture/modern/shared_searchable_desk_02.iff"
		result.attribute_template_id = 6
		result.stfName("frn_n","frn_searchable_desk_02")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())