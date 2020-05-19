"""
Extension classes enhance TouchDesigner components with python. An
extension is accessed via ext.ExtensionClassName from any operator
within the extended component. If the extension is promoted via its
Promote Extension parameter, all its attributes with capitalized names
can be accessed externally, e.g. op('yourComp').PromotedFunction().

Help: search "Extensions" in wiki
"""

from TDStoreTools import StorageManager
TDF = op.TDModules.mod.TDFunctions

class Knob:
	"""
	Knob description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.valueOp = op('constant2')

		# properties
		TDF.createProperty(self, 'Value', value=op('out1')[0], dependable=True,
						   readOnly=True)


	def ResetValue(self):
		self.ownerComp.store('currentValue', 0.48)
		self.valueOp.par.value0 = 0.48
