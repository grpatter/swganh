#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/weapon/ranged/creature/shared_creature_spit_spray_red.iff"
	is_prototype = False
	
	def create(self, params):
		result = Weapon()
	
		result.template = "object/weapon/ranged/creature/shared_creature_spit_spray_red.iff"
		result.attribute_template_id = 10
		result.stfName("unknown_weapon","obj_n")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())