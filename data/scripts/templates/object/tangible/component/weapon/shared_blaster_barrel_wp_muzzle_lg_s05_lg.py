#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/component/weapon/shared_blaster_barrel_wp_muzzle_lg_s05_lg.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/component/weapon/shared_blaster_barrel_wp_muzzle_lg_s05_lg.iff"
		result.attribute_template_id = -1
		result.stfName("blaster_barrel_l_t5","craft_weapon_ingredients_n")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())