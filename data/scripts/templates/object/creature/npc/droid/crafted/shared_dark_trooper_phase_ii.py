#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/creature/npc/droid/crafted/shared_dark_trooper_phase_ii.iff"
	is_prototype = False
	
	def create(self, params):
		result = Creature()
	
		result.template = "object/creature/npc/droid/crafted/shared_dark_trooper_phase_ii.iff"
		result.attribute_template_id = 3
		result.stfName("dark_trooper_phase_ii_crafted","droid_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())