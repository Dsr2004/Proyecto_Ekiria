from Usuarios.forms import Regitro


def registro_form(request):
    registro_form = Regitro()
    return{
        'registroForm':registro_form
    }