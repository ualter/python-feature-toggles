class User:
    def __init__(self, **entries):
        self.__dict__.update(entries)

    def __str__(self):
        return (
            "Owner..............: "
            + self.name
            + "\nOrganization.......: "
            + self.organization
            + "\nArea...............: "
            + self.area
            
        )