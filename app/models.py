from django.db import models

class Cidades(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.uf} - {self.nome}'

class Ocupacoes(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Pessoas(models.Model):
    nome = models.CharField(max_length=50)
    pai = models.CharField(max_length=50)
    mae = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)
    ocupacoes = models.ForeignKey(Ocupacoes, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome
    

class Instituicoes(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
class Areas_do_Saber(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Cursos(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria_total = models.PositiveIntegerField()
    duracao_meses = models.PositiveIntegerField()
    area_saber = models.ForeignKey(Areas_do_Saber, on_delete=models.CASCADE)
    instituicoes = models.ForeignKey(Instituicoes, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.area_saber} - {self.nome}'
    
class Periodos(models.Model):
    nome = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Diciplinas(models.Model):
    nome = models.CharField(max_length=50)
    area_saber = models.ForeignKey(Areas_do_Saber, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Matriculas(models.Model):
    instituicao = models.ForeignKey(Instituicoes, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

    def __str__(self):
        return f'{self.pessoa} - {self.curso} - {self.instituicao}'
    
class Avaliacoes(models.Model):
    descricao = models.CharField(max_length=50)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Diciplinas, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.curso} - {self.descricao}'
    
class Frequencias(models.Model):
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Diciplinas, on_delete=models.CASCADE)
    numero_faltas = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.pessoa} - {self.disciplina} - {self.numero_faltas}'
    
class Turmas(models.Model):
    nome = models.CharField(max_length=50)
    periodo = models.CharField(max_length=50)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.periodo} - {self.curso}'
    
class Ocorrencias(models.Model):
    descricao = models.CharField(max_length=50)
    data = models.DateField()
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Diciplinas, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.data} - {self.pessoa} - {self.descricao}'
    
class Disciplinas_Cursos(models.Model):
    disciplina = models.ForeignKey(Diciplinas, on_delete=models.CASCADE)
    carga_horaria = models.PositiveIntegerField()
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodos, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.curso} - {self.disciplina}' 
    
class Tipos_Avaliacoes(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

# Create your models here.