# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Pesquisador(models.Model):

	class Meta:
		db_table = 'pesquisador'
		verbose_name = 'pesquisador'
		verbose_name_plural = 'pesquisadores'

	opcoes_sexo = (
		('M', 'Masculino'),
		('F', 'Feminino'),
	)

	nome = models.CharField('nome do pesquisador', max_length=200, unique=True)
	nome_cientifico = models.CharField('nome de referência científica do pesquisador', max_length=200)
	sexo = models.CharField('sexo do pesquisador', max_length=1, choices=opcoes_sexo)
	email = models.EmailField('e-mail do pesquisador', unique=True)

	titulos = models.ManyToManyField('Titulo', through='Titulacao', verbose_name='títulos do pesquisador')
	formacoes = models.ManyToManyField('AreaFormacao', through='Formacao', verbose_name='áreas de formação do pesquisador')
	cursos_vinculados = models.ManyToManyField('Curso', through='CursoVinculado', verbose_name='cursos vinculados')
	url_lates = models.CharField('URL curriculo do LATES', max_length=200, blank=True)

	def __unicode__(self):
		return self.nome


class Titulo(models.Model):
	nome = models.CharField('título acadêmico', max_length=200)

	class Meta:
		db_table = 'titulo'
		verbose_name = 'título'
		verbose_name_plural = 'títulos'

	def __unicode__(self):
		return self.nome

class Titulacao(models.Model):

	class Meta:
		db_table = 'pesquisador_titulo'
		verbose_name = 'titulação'
		verbose_name_plural = 'titulações'

	pesquisador = models.ForeignKey('Pesquisador')
	titulo = models.ForeignKey('Titulo')
	ano = models.IntegerField('ano de aquisição do título', null=True)


	def __unicode__(self):
		if self.pesquisador.sexo == 'M':
			return u'{self.pesquisador.nome} é um {self.titulo} desde {self.ano}'.format(self=self)
		else:
			return u'{self.pesquisador.nome} é uma {self.titulo} desde {self.ano}'.format(self=self)


class AreaFormacao(models.Model):

	class Meta:
		db_table = 'area_formacao'
		verbose_name = 'área de formação'
		verbose_name_plural = 'áreas de formação'

	nome = models.CharField('área de formação', max_length=200)

	def __unicode__(self):
		return self.nome

class Formacao(models.Model):

	class Meta:
		db_table = 'pesquisador_area_formacao'
		verbose_name = 'área de formação'
		verbose_name_plural = 'áreas de formação'

	pesquisador = models.ForeignKey('Pesquisador')
	area_formacao = models.ForeignKey('AreaFormacao')
	ano = models.IntegerField('ano de formação', null=True)

	def __unicode__(self):
		return u'{self.pesquisador.nome} é formado(a) em {self.area_formacao.nome}'.format(self=self)

class Curso(models.Model):

	class Meta:
		db_table = 'curso'
		verbose_name = 'curso'
		verbose_name_plural = 'cursos'

	nome = models.CharField('nome do curso', max_length=200)

	def __unicode__(self):
		return self.nome

class CursoVinculado(models.Model):

	class Meta:
		db_table = 'pesquisador_curso'
		verbose_name = 'curso vinculado'
		verbose_name_plural = 'cursos vinculados'

	pesquisador = models.ForeignKey('Pesquisador')
	curso = models.ForeignKey('Curso')

	def __unicode__(self):
		return u'{self.pesquisador.nome} tem vínculo com {self.curso.nome}'.format(self=self)


class Pesquisa(models.Model):

	class Meta:
		db_table = 'pesquisa'
		verbose_name = 'pesquisa'
		verbose_name_plural = 'pesquisas'

	opcoes_tipo_pesquisa = (
		(u'PURA', 'Pesquisa pura'),
		(u'APLICADA', 'Pesquisa aplicada'),
	)

	opcoes_status_pesquisa = (
		(u'CONCLUÍDA', 'Pesquisa concluída'),
		(u'NÂO CONCLUÍDA', 'Pesquisa não concluída'),
		(u'EM ANDAMENTO', '	Pesquisa em andamento'),
	)

	opcoes_qualificacao_pesquisa = (
		(u'PROJETO', 'Projeto'),
		(u'TCC', 'Trabalho de Conclusão de Curso'),
		(u'MONOGRAFIA', 'Monografia'),
		(u'DISSERTAÇÃO', 'Dissertação'),
	)

	opcoes_tempo_duracao_pesquisa = (
		(u'ATÉ 6 MESES', 'Até 6 (seis) meses'),
		(u'1 ANO', '1 (Um) ano'),
		(u'2 ANOS', '2 (Um) anos'),
		(u'MAIS DE 2 ANOS', 'Mais de 2 anos'),
	)

	opcoes_impacto_pesquisa = (
		(u'DIFUSÃO', 'Difusão'),
		(u'ADOÇÃO', 'Adoção'),
	)
		
	titulo = models.CharField('título da pesquisa', max_length=200)
	tipo = models.CharField('tipo de pesquisa', choices=opcoes_tipo_pesquisa, max_length=45)
	status = models.CharField('status da pesquisa', choices=opcoes_status_pesquisa, max_length=45)
	qualificacao = models.CharField('qualificação da pesquisa', choices=opcoes_qualificacao_pesquisa, max_length=45)
	tempo_duracao = models.CharField('tempo de duração da pesquisa', choices=opcoes_tempo_duracao_pesquisa, max_length=45)
	data_submissao = models.DateField('data de submissão')
	impacto_pesquisa = models.CharField('impacto da pesquisa',choices=opcoes_impacto_pesquisa, max_length=45)
	gerou_patente = models.BooleanField('gerou patente?', default=False)
	instituicao_submissao = models.ForeignKey('InstituicaoSubmissao')
	fonte_financiamento = models.ForeignKey('FonteFinanciamento')
	resumo = models.TextField('resumo da pesquisa', 
		help_text='O resumo deve conter: Objetivo geral da pesquisa; Breve referencial teórico; Metodologia; Resultados.'
	)
	url_submissao = models.CharField('Link para a pesquisa', max_length=200,
		help_text='O endereço da web para o documento da pesquisa.'
	)

	instituicoes_cooperadoras = models.ManyToManyField('InstituicaoCooperadora', through='Cooperacao', verbose_name='instituição cooperadora')
	areas_conhecimento = models.ManyToManyField('AreaConhecimento', through='AreaRelacionada', verbose_name='áreas do conhecimento')
	locais = models.ManyToManyField('Local', through='LocalPesquisa', verbose_name='locais de pesquisa')
	palavras_chave = models.ManyToManyField('PalavraChave', through='PalavraChavePesquisa', verbose_name='palavras-chave')
	pesquisadores = models.ManyToManyField('Pesquisador', through='ParticipacaoAutoral', verbose_name='pesquisadores')

class InstituicaoSubmissao(models.Model):

	class Meta:
		db_table = 'instituicao_submissao'
		verbose_name = 'instituição de submissão'
		verbose_name_plural = 'instituições de submissão'

	nome = models.CharField('nome da instituição de submissão', max_length=200)

	def __unicode__(self):
		return self.nome

class FonteFinanciamento(models.Model):

	class Meta:
		db_table = 'fonte_financiamento'
		verbose_name = 'fonte de financiamento'
		verbose_name_plural = 'fontes de financiamento'

	nome = models.CharField('nome da fonte de financiamento', max_length=45)

	def __unicode__(self):
		return self.nome

class InstituicaoCooperadora(models.Model):

	class Meta:
		db_table = 'instituicao_cooperadora'
		verbose_name = 'instituição cooperadora'
		verbose_name_plural = 'instituições cooperadoras'

	nome = models.CharField('nome da instituição', max_length=200)

	def __unicode__(self):
		return self.nome

class Cooperacao(models.Model):

	class Meta:
		db_table = 'pesquisa_instituicao_cooperadora'
		verbose_name = 'cooperação'
		verbose_name_plural = 'cooperações'

	pesquisa = models.ForeignKey('Pesquisa')
	instituicao_cooperadora = models.ForeignKey('InstituicaoCooperadora', verbose_name='Instituição cooperadora')

	def __unicode__(self):
		return '{self.instituicao_cooperadora.nome}'.format(self=self)

class AreaConhecimento(models.Model):
	
	class Meta:
		db_table = 'area_conhecimento'
		verbose_name = 'área do conhecimento'
		verbose_name_plural = 'áreas do conhecimento'

	nome = models.CharField('nome da área de conhecimento', max_length=45)
	ciencia = models.CharField('ciência', max_length=45)
	area_avaliacao = models.CharField('área de avaliação', max_length=45)

	def __unicode__(self):
		return self.nome

class AreaRelacionada(models.Model):

	class Meta:
		db_table = 'pesquisa_area_conhecimento'
		verbose_name = 'área do conhecimento relacionada'
		verbose_name_plural = 'áreas do conhecimento relacionadas'

	pesquisa = models.ForeignKey('Pesquisa')
	area_conhecimento = models.ForeignKey('AreaConhecimento', verbose_name='área do conhecimento')

	def __unicode__(self):
		return '{self.area_conhecimento.nome}'.format(self=self)

class Local(models.Model):

	class Meta:
		db_table = 'local'
		verbose_name = 'local'
		verbose_name_plural = 'locais'

	descricao = models.TextField('descrição', max_length=200, 
		help_text='Descrição do local.'
	)
	nome_cidade = models.CharField('nome da cidade', max_length=200)
	codigo_ibge = models.CharField('código IBGE da cidade', max_length=45)
	pais = models.CharField('país', max_length=45)

	def __unicode__(self):
		return '{0} {1}'.format(self.descricao,self.nome_cidade)

class LocalPesquisa(models.Model):

	class Meta:
		db_table = 'pesquisa_local'
		verbose_name = 'local da pesquisa'
		verbose_name_plural = 'locais de pesquisa'

	pesquisa = models.ForeignKey('Pesquisa')
	local = models.ForeignKey('Local', verbose_name='local da pesquisa')

	def __unicode__(self):
		return '{self.local.descricao}; {self.local.cidade}/{self.local.pais}'.format(self=self)


class PalavraChave(models.Model):

	class Meta:
		db_table = 'palavra_chave'
		verbose_name = 'palavra-chave'
		verbose_name_plural = 'palavras-chave'

	palavra = models.CharField('palavra-chave', max_length=45)

	def __unicode__(self):
		return self.palavra

class PalavraChavePesquisa(models.Model):

	class Meta:
		db_table = 'pesquisa_palavra_chave'
		verbose_name = 'palavra-chave'
		verbose_name_plural = 'palavras-chave'

	pesquisa = models.ForeignKey('Pesquisa')
	palavra_chave = models.ForeignKey('PalavraChave', verbose_name='palavra-chave')

	def __unicode__(self):
		return self.palavra_chave.palavra

class ParticipacaoAutoral(models.Model):

	class Meta:
		db_table = 'pesquisador_pesquisa'
		verbose_name = 'colaboração'
		verbose_name_plural = 'colaborações'

	opcoes_tipo_participacao = (
		('PESQUISADOR PRINCIPAL', 'Pesquisador principal'),
		('PESQUISADOR COLABORADOR', 'Pesquisador coolaborador'),
		('ORIENTADOR', 'Orientador'),
	)

	pesquisador = models.ForeignKey('Pesquisador', verbose_name='colaboração do pesquisador')
	pesquisa = models.ForeignKey('Pesquisa', verbose_name='pesquisa')
	tipo_participacao = models.CharField('tipo de colaboração para a pesquisa', choices=opcoes_tipo_participacao, max_length=45)

	def __unicode__(self):
		return '{self.pesquisador.nome} ({self.tipo_participacao})'.format(self=self)
