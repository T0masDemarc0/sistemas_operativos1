def dinerillo_gastado(importe) :
    impuestos = 75
    impuestos_del_importe = importe * impuestos / 100
    costo_del_juego = importe + impuestos_del_importe
    print("Con los impuestos el juego te sale:", costo_del_juego)

