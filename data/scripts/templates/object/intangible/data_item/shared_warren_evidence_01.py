#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/intangible/data_item/shared_warren_evidence_01.iff"
	is_prototype = False
	
	def create(self, params):
		result = Intangible()
	
		result.template = "object/intangible/data_item/shared_warren_evidence_01.iff"
		result.attribute_template_id = -1
		result.stfName("warren_item_n","warren_evidence_01")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())