#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/installation/battlefield/destructible/barracks/shared_bfield_nightsister_barracks.iff"
	is_prototype = False
	
	def create(self, params):
		result = Installation()
	
		result.template = "object/installation/battlefield/destructible/barracks/shared_bfield_nightsister_barracks.iff"
		result.attribute_template_id = -1
		result.stfName("battlefield","gungan_barracks")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())