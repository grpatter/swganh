#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/item/quest/force_sensitive/shared_fs_craft_puzzle_signal_amp.iff"
	is_prototype = False
	
	def create(self, kernel, params):
		result = Tangible()
	
		result.template = "object/tangible/item/quest/force_sensitive/shared_fs_craft_puzzle_signal_amp.iff"
		result.attribute_template_id = -1
		result.stfName("quest_item_n","fs_craft_puzzle_signal_amp")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())