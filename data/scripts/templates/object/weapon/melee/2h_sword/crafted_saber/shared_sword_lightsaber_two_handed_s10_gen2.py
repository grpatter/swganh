#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/weapon/melee/2h_sword/crafted_saber/shared_sword_lightsaber_two_handed_s10_gen2.iff"
	is_prototype = False
	
	def create(self, params):
		result = Weapon()
	
		result.template = "object/weapon/melee/2h_sword/crafted_saber/shared_sword_lightsaber_two_handed_s10_gen2.iff"
		result.attribute_template_id = 10
		result.stfName("weapon_name","sword_lightsaber_2h_type10")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())