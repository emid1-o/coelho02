class Manutencao:
    def __init__(self, data, tipo_servico, custo):
        self.data = data
        self.tipo_servico = tipo_servico
        self.custo = custo

class Veiculo:
    def __init__(self, placa, modelo, ano, valor_diaria):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self.disponivel = True
        self.manutencoes = []

    def registrar_manutencao(self, data, tipo_servico, custo):
        nova_manutencao = Manutencao(data, tipo_servico, custo)
        self.manutencoes.append(nova_manutencao)

class Carro(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, portas):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.portas = portas

class Moto(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, cilindradas):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.cilindradas = cilindradas

class Caminhao(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, capacidade_carga):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.capacidade_carga = capacidade_carga

class Cliente:
    def __init__(self, telefone, endereco):
        self.telefone = telefone
        self.endereco = endereco

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, telefone, endereco):
        super().__init__(telefone, endereco)
        self.nome = nome
        self.cpf = cpf

class PessoaJuridica(Cliente):
    def __init__(self, razao_social, cnpj, telefone, endereco):
        super().__init__(telefone, endereco)
        self.razao_social = razao_social
        self.cnpj = cnpj

class Condutor:
    def __init__(self, nome, cnh):
        self.nome = nome
        self.cnh = cnh

class Contrato:
    def __init__(self, cliente, veiculo, data_inicio, data_termino, valor_total, nome_condutor, cnh_condutor):
        self.cliente = cliente
        self.veiculo = veiculo
        self.veiculo.disponivel = False
        
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.valor_total = valor_total
        self.status = "Ativo"
        
        self.condutor = Condutor(nome_condutor, cnh_condutor)

    def finalizar(self):
        self.status = "Finalizado"
        self.veiculo.disponivel = True
        print("Contrato encerrado. Veículo liberado e dados do condutor descartados.")
        del self.condutor

cliente_pj = PessoaJuridica("Empresa XYZ", "00.000.000/0001-00", "1199999999", "Rua A")
carro_sedan = Carro("ABC-1234", "Honda Civic", 2024, 250.0, 4)

carro_sedan.registrar_manutencao("01/10/2026", "Troca de óleo", 350.0)

contrato_aluguel = Contrato(
    cliente=cliente_pj, 
    veiculo=carro_sedan, 
    data_inicio="07/10/2026", 
    data_termino="15/10/2026", 
    valor_total=2000.0, 
    nome_condutor="Carlos Motorista", 
    cnh_condutor="123456789"
)

print(f"Cliente: {contrato_aluguel.cliente.razao_social}")
print(f"Veículo alugado: {contrato_aluguel.veiculo.modelo} ({contrato_aluguel.veiculo.placa})")
print(f"Condutor: {contrato_aluguel.condutor.nome}")
print(f"Valor Total: R$ {contrato_aluguel.valor_total}")
print(f"Status do veículo antes de finalizar: {'Disponível' if carro_sedan.disponivel else 'Alugado'}")

print("\n--- Finalizando o contrato ---")
contrato_aluguel.finalizar()
print(f"Status do veículo após finalizar: {'Disponível' if carro_sedan.disponivel else 'Alugado'}")