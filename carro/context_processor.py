def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:  # No se deben usar paréntesis
        # Verifica que 'carro' esté en la sesión
        #if 'carro' in request.session:
        for key, value in request.session['carro'].items():
            total += float(value["precio"])
    else:
        total = "Debes hacer login "
    return {'importe_total_carro': total}
