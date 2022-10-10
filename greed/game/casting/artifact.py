from game.casting.actor import Actor

class Artifact(Actor):
    """Objects which are randomly placed, and which have particular points depending on the artifiact, and in which the player can collect.

    Attributes:
        super().__init__() = Attributes from the parent class (Actor).
        _points (int): Initial points belonging to the Artifact.
    """

    def __init__(self):
        """ Constructs a new Artifact. """
        super().__init__()
        self._points = 0

    def get_points(self):
        """ Gets the artifact's points.

            Returns:
            _points (int): The artifact's collected points.
        """
        if (self.get_text() == '*'):
            self._points += 1   
        elif (self.get_text() == 'O'):
            self._points -= 1

        return self._points