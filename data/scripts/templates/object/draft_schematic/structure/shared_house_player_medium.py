#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/draft_schematic/structure/shared_house_player_medium.iff"
	is_prototype = False
	
	def create(self, params):
		result = Intangible()
	
		result.template = "object/draft_schematic/structure/shared_house_player_medium.iff"
		result.attribute_template_id = -1
		result.stfName("string_id_table","")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())