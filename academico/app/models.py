from django.db import models

class Ocupacaodepessoas(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nome}"
    
class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    def __str__(self):
        return f"{self.nome_cidade}, {self.uf}"
    
class Turmas(models.Model):
    nome = models.CharField(max_length=100)
    periodo_semestre = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.nome_cidade}, {self.periodo_semestre}"

class Tipodeavaliacao(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nome}"

class Semestredecursos(models.Model):
    periodo = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.periodo}"
    
class Areasdosaber(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nome}"
    
class Instituicaodeensino(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=25)
    telefone = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.nome}, {self.site} , {self.telefone}"

class Pessoas(models.Model):
    nome = models.CharField(max_length=100)
    pai = models.CharField(max_length=25)
    mae = models.CharField(max_length=25)
    cpf = models.CharField(max_length=25)
    data_nasc = models.DateField()
    email = models.CharField(max_length=100)
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacaodepessoas, on_delete=models.CASCADE) 
    def __str__(self):
        return f"{self.nome}, {self.cpf}, {self.ocupacao}"
    
class Cursos(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.CharField(max_length=25)
    duracao_meses = models.CharField(max_length=25)
    area_saber = models.CharField(max_length=25)
    instituicao = models.DateField()
    def __str__(self):
        return f"{self.nome}, {self.cpf}, {self.ocupacao}"
    
class Discipinas(models.Model):
    nome = models.CharField(max_length=100)
    area_saber = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.nome}, {self.area_saber}"
    
class Matriculas(models.Model):
    instituicao = models.CharField(max_length=100)
    curso = models.CharField(max_length=25)
    pessoa = models.CharField(max_length=25)
    data_inicio = models.CharField(max_length=25)
    data_previsao_termino= models.CharField(max_length=25)
    def __str__(self):
        return f"{self.instituicao}, {self.curso}, {self.pessoa}"
    
class Avaliacoes(models.Model):
    descricao = models.CharField(max_length=100)
    curso = models.CharField(max_length=25)
    disciplina= models.CharField(max_length=100)
    tipo_avaliacao= models.CharField(max_length=25)
    def __str__(self):
        return f"{self.nome}, {self.area_saber}"
    
class Frequencia(models.Model):
    curso = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=25)
    numero_faltas= models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nome}, {self.area_saber}"

class Ocorrencias_advertencias(models.Model):
    descricao = models.CharField(max_length=100)
    data = models.CharField(max_length=25)
    curso = models.CharField(max_length=100)
    discipina = models.CharField(max_length=25)
    pessoa = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nome}, {self.area_saber}"
    
class Ocorrencias_advertencias(models.Model):
    nome= models.CharField(max_length=100)
    carga_horaria = models.CharField(max_length=25)
    cursos = models.CharField(max_length=100)
    periodo = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.nome}, {self.area_saber}"