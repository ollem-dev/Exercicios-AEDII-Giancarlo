from tadCAFE import Cafeteira

minha_maquina = Cafeteira(500)

''''minha_maquina.fazer_cafe()''' #testando se esta ligada ou desligada

minha_maquina.ligar()
minha_maquina.abastecer_agua(300)
minha_maquina.abastecer_cafe(30)
#minha_maquina.ver_status()

minha_maquina.fazer_cafe()
minha_maquina.ver_status()

minha_maquina.desligar()