class Pet:
    
    #Class variable
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=""):
        self.name = name
        self.pet_type = pet_type 
        self.owner = owner
        Pet.all.append(self)
        
    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    # Validate that the pet_type is one of those PET_TYPES, raise Exception if this check fails
    def pet_type(self, n_pet_type):
        if n_pet_type in self.PET_TYPES:
            self._pet_type = n_pet_type
        else:
            raise Exception
        
class Owner:
    def __init__(self, name):
        self.name = name
    
    #Returns a full list of the owner's pets
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    #Checks that the pet is of type Pet and adds the owner to the pet
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance or of type Pet")
        pet.owner = self
        
    #Returns a sorted list of pets by their names
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    
