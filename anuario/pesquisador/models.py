from django.db import models
from django.contrib.auth.models import User

class Pesquisador(models.Model):

	class Meta:
		db_table = 'pesquisador'
		verbose_name = 'pesquisador'
		verbose_name_plural = 'pesquisadores'

	usuario = models.ForeignKey(User)

	nome_do_pesquisador = models.CharField('nome do pesquisador', max_length=200, unique=True)
	nome_cientifico = models.CharField('nome de referência científica do pesquisador', max_length=200)

	opcoes_sexo = (
		('M', 'Masculino'),
		('F', 'Feminino'),
	)

	sexo = models.CharField('sexo do pesquisador', max_length=1, choices=opcoes_sexo)
	email = models.EmailField('e-mail do pesquisador', unique=True)

	opcoes_titulo = (
		('graduado_bacharel', 'Graduado em Bacharelado'),
		('graduado_licenciatura', 'Graduado em Licenciatura'),
		('especialita', 'Especialista'),
		('mestre', 'Mestre'),
		('doutor', 'Doutor'),
		
	)

	titulo = models.CharField('título do pesquisador', max_length=100, choices=opcoes_titulo)

	opcoes_tipo_pesquisador = (
		('estudante', 'Estudante'),
		('professor', 'Professor'),
		('tecnico', 'Técnico'),
	)

	tipo_pesquisador = models.CharField('sexo do pesquisador', max_length=15, choices=opcoes_tipo_pesquisador)

	curso = models.ForeignKey('Curso')

#	formacoes = models.ManyToManyField('AreaFormacao', through='Formacao', verbose_name='áreas de formação do pesquisador')
#	cursos_vinculados = models.ManyToManyField('Curso', through='CursoVinculado', verbose_name='cursos vinculados')
	url_lates = models.CharField('URL curriculo do LATES', max_length=200, blank=True)

	def __str__(self):
		return self.nome_do_pesquisador

class Instituicao(models.Model):

	nome_da_instituicao = models.CharField('nome da instituição', max_length=200)
	sigla = models.CharField('sigla da instituição', max_length=20)
	cidade = models.CharField('cidade da instituição', max_length=200)
	nome_da_unidade = models.CharField('nome da unidade', max_length=200, blank=True)
	#estado = models.CharField('estado da instituição', max_length=20)

	def __str__(self):
		return "%s/%s" % (self.sigla, self.nome_da_unidade)

class Curso(models.Model):

	nome_do_curso = models.CharField('nome do curso', max_length=200)
	instituicao = models.ForeignKey('Instituicao')


	def __str__(self):
		return "%s" % (self.nome_do_curso)

