
# =============================================================================
class Message():

    # -------------------------------------------------------------------------
    def __init__(self, msg, key=None):
        self.message = msg
        self.key = key
        if key:
            self.encrypt(key)

    # -------------------------------------------------------------------------
    def is_encrypted(self):
        return self.key is not None

    # -------------------------------------------------------------------------
    def encrypt(self, key):
        """ ESTO NO ES UNA FORMA DE CIFRADO. SOLO PARA DEMOSTRACION.
            NUNCA USAR PARA MANEJO DE CONTRASENIAS O SIMILARES
        """
        while len(key) < len(self.message):  # hacer la llave del mismo tamanio que el mensaje
            key += key
        self.key = key[:len(self.message)]  
        self.message = ''.join(['%s%s' % (a, b) for a, b in zip(self.message[::-1], self.key[::-1])])

    # -------------------------------------------------------------------------
    def decrypt(self):
        self.message = ''.join([c for i, c in enumerate(self.message) if i % 2 == 0])[::-1]
        self.key = None


# ============================================================================= 
if __name__ == '__main__':
    m = Message('contrasenia secreta')
    print m.message
    print m.is_encrypted()
    m.encrypt('s4bRumA+aks3eGasw?WA')
    print m.message
    print m.is_encrypted()
    m.decrypt()
    print m.message
    print m.is_encrypted()

    m2 = Message('otra contrasenia', 'WrE6age&RecHub6ph!fr')
    print m2.message
    print m2.is_encrypted()
