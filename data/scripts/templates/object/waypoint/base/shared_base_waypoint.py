#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/waypoint/base/shared_base_waypoint.iff"
	is_prototype = False
	
	def create(self, params):
		result = Waypoint()
	
		result.template = "object/waypoint/base/shared_base_waypoint.iff"
		result.attribute_template_id = -1
		result.stfName("obj_n","waypoint")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())