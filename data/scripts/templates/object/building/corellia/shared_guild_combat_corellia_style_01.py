#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/corellia/shared_guild_combat_corellia_style_01.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/corellia/shared_guild_combat_corellia_style_01.iff"
		result.attribute_template_id = -1
		result.stfName("guild_combat_corellia","building_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())