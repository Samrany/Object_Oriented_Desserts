"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __init__(self, name, flavor, price):
    	self.name = name
    	self.flavor = flavor
    	self.price = price
    	self.qty = 0
    	self.cache(self.name)


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


    # @classmethod
    # def cache(cls, name):
    # 	"""store all cupcake instances by name"""

 
    	
    def get_cupcake(cls, name):
    	cls.cache(name)

    def add_stock(self, amount):	
     	self.qty += amount

    def sell(self, amount):
    	if amount < self.qty:
    		self.qty = self.qty - amount
    	elif self.qty == 0:
    		print("Sorry, these cupcakes are sold out")
    	else:
    		print("there are only {} of these left".format(self.qty))
    		self.qty = 0


    # @staticmethod
    # def scale_recipe(ingredients, amount):
    # 	for ingredient in ingredients:
    # 		[(ingredient, qty * amount)]

    # 	return ingredients	





if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
